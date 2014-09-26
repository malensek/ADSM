/** @file infection_monitor.c
 * Tracks the cause of infections.
 *
 * @author Neil Harvey <nharve01@uoguelph.ca><br>
 *   School of Computer Science, University of Guelph<br>
 *   Guelph, ON N1G 2W1<br>
 *   CANADA
 * @version 0.1
 * @date August 2004
 *
 * Copyright &copy; University of Guelph, 2004-2009
 * 
 * This program is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the Free
 * Software Foundation; either version 2 of the License, or (at your option)
 * any later version.
 */

#if HAVE_CONFIG_H
#  include "config.h"
#endif

/* To avoid name clashes when multiple modules have the same interface. */
#define new infection_monitor_new
#define run infection_monitor_run
#define to_string infection_monitor_to_string
#define local_free infection_monitor_free
#define handle_before_each_simulation_event infection_monitor_handle_before_each_simulation_event
#define handle_new_day_event infection_monitor_handle_new_day_event
#define handle_infection_event infection_monitor_handle_infection_event
#define handle_detection_event infection_monitor_handle_detection_event

#include "module.h"

#if STDC_HEADERS
#  include <string.h>
#endif

#if HAVE_MATH_H
#  include <math.h>
#endif


#include "infection_monitor.h"

#include "general.h"

#ifdef USE_SC_GUILIB
#  include <sc_adsm_outputs.h>
#endif

#if !HAVE_ROUND && HAVE_RINT
#  define round rint
#endif

double round (double x);

/** This must match an element name in the DTD. */
#define MODEL_NAME "infection-monitor"



/** Specialized information for this model. */
typedef struct
{
  GPtrArray *production_types;
  RPT_reporting_t   *num_units_infected;
  RPT_reporting_t  **num_units_infected_by_cause;
  RPT_reporting_t  **num_units_infected_by_prodtype;
  RPT_reporting_t ***num_units_infected_by_cause_and_prodtype;
  RPT_reporting_t   *cumul_num_units_infected;
  RPT_reporting_t  **cumul_num_units_infected_by_cause;
  RPT_reporting_t  **cumul_num_units_infected_by_prodtype;
  RPT_reporting_t ***cumul_num_units_infected_by_cause_and_prodtype;
  RPT_reporting_t   *num_animals_infected;
  RPT_reporting_t  **num_animals_infected_by_cause;
  RPT_reporting_t  **num_animals_infected_by_prodtype;
  RPT_reporting_t ***num_animals_infected_by_cause_and_prodtype;
  RPT_reporting_t   *cumul_num_animals_infected;
  RPT_reporting_t  **cumul_num_animals_infected_by_cause;
  RPT_reporting_t  **cumul_num_animals_infected_by_prodtype;
  RPT_reporting_t ***cumul_num_animals_infected_by_cause_and_prodtype;
  GPtrArray *daily_outputs; /**< Daily outputs, in a list to make it easy to
    zero them all at once. */
  GPtrArray *cumul_outputs; /**< Cumulative outputs, is a list to make it easy
    to zero them all at once. */
  gboolean detection_occurred;
  int detection_day;
  RPT_reporting_t *first_det_u_inf;
  RPT_reporting_t *first_det_a_inf;
  RPT_reporting_t *ratio;
  unsigned int nrecent_days; /**< The time period over which to compare recent
    infections.  A value of 14 would mean to report the number of new
    infections in the last 2 weeks over the number of new infections in the
    2 weeks before that. */
  unsigned int *nrecent_infections; /**< The number of new infections on each
    day in the recent past.  The length of this array is nrecent_days * 2. */
  unsigned int recent_day_index; /**< The current index into the
    nrecent_infections array.  The index "rotates" through the array, arriving
    back at the beginning and starting to overwrite old values every
    nrecent_days * 2 days. */
  unsigned int numerator, denominator;
}
local_data_t;



/**
 * Before each simulation, zero the cumulative counts of infections.
 *
 * @param self this module.
 */
void
handle_before_each_simulation_event (struct adsm_module_t_ *self)
{
  local_data_t *local_data;
  unsigned int i;

  #if DEBUG
    g_debug ("----- ENTER handle_before_each_simulation_event (%s)", MODEL_NAME);
  #endif

  local_data = (local_data_t *) (self->model_data);
  g_ptr_array_foreach (local_data->cumul_outputs, RPT_reporting_zero_as_GFunc, NULL);
  local_data->detection_occurred = FALSE;
  /* The output variables for units and animals infected at first detection
   * have no value until there is a detection. */
  RPT_reporting_set_null (local_data->first_det_u_inf);
  RPT_reporting_set_null (local_data->first_det_a_inf);
  RPT_reporting_set_null (local_data->ratio);
  for (i = 0; i < local_data->nrecent_days * 2; i++)
    local_data->nrecent_infections[i] = 0;

  #if DEBUG
    g_debug ("----- EXIT handle_before_each_simulation_event (%s)", MODEL_NAME);
  #endif

  return;
}



/**
 * On each new day, zero the daily counts of infections and does some setup for
 * calculating the reproduction number R.
 *
 * @param self the model.
 * @param event a new day event.
 */
void
handle_new_day_event (struct adsm_module_t_ *self, EVT_new_day_event_t * event)
{
  local_data_t *local_data;
  unsigned int current, hi, i, count;
#if DEBUG
  GString *s;
#endif

#if DEBUG
  g_debug ("----- ENTER handle_new_day_event (%s)", MODEL_NAME);
#endif

  local_data = (local_data_t *) (self->model_data);

  /* Zero the daily counts. */
  if (event->day > 1)
    {
      g_ptr_array_foreach (local_data->daily_outputs, RPT_reporting_zero_as_GFunc, NULL);
    }

  /* Move the pointer for the current day's infection count ahead. */
  hi = local_data->nrecent_days * 2;
  if (event->day == 1)
    {
      current = local_data->recent_day_index;
    }
  else
    {
      current = (local_data->recent_day_index + 1) % hi;
      local_data->recent_day_index = current;
      /* Zero the current day's count. */
      local_data->nrecent_infections[current] = 0;
    }

  /* Compute the denominator of the infection ratio for today. */
  local_data->denominator = 0;
  /* The numbers that sum to the denominator start at 1 past the current point
   * and continue for the period defined by nrecent_days. */
  for (i = (current + 1) % hi, count = 0;
       count < local_data->nrecent_days; i = (i + 1) % hi, count++)
    local_data->denominator += local_data->nrecent_infections[i];

  /* Compute the numerator, minus the current day's infections (which are yet
   * to happen). */
  local_data->numerator = 0;
  for (count = 0; count < local_data->nrecent_days; i = (i + 1) % hi, count++)
    local_data->numerator += local_data->nrecent_infections[i];

#if DEBUG
  s = g_string_new (NULL);
  g_string_append_printf (s, "at beginning of day %i counts of recent infections = [", event->day);
  for (i = 0; i < hi; i++)
    {
      if (i > 0)
        g_string_append_c (s, ',');
      g_string_append_printf (s, i == current ? "(%u)" : "%u", local_data->nrecent_infections[i]);
    }
  g_string_append_c (s, ']');
  g_debug ("%s", s->str);
  g_string_free (s, TRUE);
  g_debug ("denominator = sum from %u to %u (inclusive) = %u",
           (current + 1) % hi, (current + local_data->nrecent_days) % hi, local_data->denominator);
#endif

  /* Set the ratio of recent infections to infections before that.  If there
   * are no detections in the current day, this will be the value that will be
   * reported at the end of the day.  Note that the value is undefined until a
   * certain number of days has passed, e.g., if we are reporting new infection
   * this week over new infections last week, the value will be undefined until
   * 2 weeks have passed. */
  if (event->day >= (local_data->nrecent_days * 2) && local_data->denominator > 0)
    RPT_reporting_set_real (local_data->ratio,
                            1.0 * local_data->numerator / local_data->denominator);

#if DEBUG
  g_debug ("----- EXIT handle_new_day_event (%s)", MODEL_NAME);
#endif
}



/**
 * Responds to the first detection event by recording the day on which it
 * occurred.
 *
 * @param self this module.
 * @param event a detection event.
 */
void
handle_detection_event (struct adsm_module_t_ *self, 
                        EVT_detection_event_t * event)
{
  local_data_t *local_data;

#if DEBUG
  g_debug ("----- ENTER handle_detection_event (%s)", MODEL_NAME);
#endif

  local_data = (local_data_t *) (self->model_data);

  if (!local_data->detection_occurred)
    {
      #if DEBUG
        g_debug ("recording first detection on day %i", event->day);
      #endif
      local_data->detection_occurred = TRUE;
      local_data->detection_day = event->day;
      /* Copy the current value from infcU to firstDetUInf and from
       * from infcA to firstDetAInf.  Any subsequent infections on the
       * day of first detection will also be included in the firstDet output
       * variables. */
      RPT_reporting_set_integer (
        local_data->first_det_u_inf,
        RPT_reporting_get_integer(local_data->cumul_num_units_infected)
      );
      RPT_reporting_set_real (
        local_data->first_det_a_inf,
        RPT_reporting_get_real(local_data->cumul_num_animals_infected)
      );
    }

#if DEBUG
  g_debug ("----- EXIT handle_detection_event (%s)", MODEL_NAME);
#endif
  return;
}



/**
 * Responds to an infection event by recording it.
 *
 * @param self the model.
 * @param event an infection event.
 */
void
handle_infection_event (struct adsm_module_t_ *self, EVT_infection_event_t * event)
{
  local_data_t *local_data;
  UNT_unit_t *infecting_unit, *infected_unit;
  UNT_infect_t update;
  ADSM_contact_type cause;
  UNT_production_type_t prodtype;
  double nanimals;
  unsigned int count;
#if DEBUG
  GString *s;
#endif

#if DEBUG
  g_debug ("----- ENTER handle_infection_event (%s)", MODEL_NAME);
#endif

  local_data = (local_data_t *) (self->model_data);
  infecting_unit = event->infecting_unit;
  infected_unit = event->infected_unit;

  cause = event->contact_type;
  prodtype = infected_unit->production_type;
  nanimals = (double)(infected_unit->size);

  update.unit_index = infected_unit->index;
  update.infection_source_type = event->contact_type;
  
#ifdef USE_SC_GUILIB
  sc_infect_unit( event->day, infected_unit, update );
#else
  if (NULL != adsm_infect_unit)
    {
      adsm_infect_unit (update);
    }
#endif
#if UNDEFINED
  printf ("unit at index %d INFECTED by method %s\n", infected_unit->index, cause);
#endif

  /* Update the counts of infections.  Note that initially infected units are
   * not included in many of the counts.  They will not be part of infnU or
   * infnU broken down by production type.  They will be part of infnUIni and
   * infnUIni broken down by production type. */
  if (event->contact_type != ADSM_InitiallyInfected)
    {
      RPT_reporting_add_integer (local_data->num_units_infected, 1);
      RPT_reporting_add_integer (local_data->num_units_infected_by_prodtype[prodtype], 1);
      RPT_reporting_add_real (local_data->num_animals_infected, nanimals);
      RPT_reporting_add_real (local_data->num_animals_infected_by_prodtype[prodtype], nanimals);
      RPT_reporting_add_integer (local_data->cumul_num_units_infected, 1);
      RPT_reporting_add_integer (local_data->cumul_num_units_infected_by_prodtype[prodtype], 1);
      RPT_reporting_add_real (local_data->cumul_num_animals_infected, nanimals);
      RPT_reporting_add_real (local_data->cumul_num_animals_infected_by_prodtype[prodtype], nanimals);
    }
  RPT_reporting_add_integer (local_data->num_units_infected_by_cause[cause], 1);
  RPT_reporting_add_real (local_data->num_animals_infected_by_cause[cause], nanimals);
  RPT_reporting_add_integer (local_data->cumul_num_units_infected_by_cause[cause], 1);
  RPT_reporting_add_real (local_data->cumul_num_animals_infected_by_cause[cause], nanimals);
  RPT_reporting_add_integer (local_data->num_units_infected_by_cause_and_prodtype[cause][prodtype], 1);
  RPT_reporting_add_real (local_data->num_animals_infected_by_cause_and_prodtype[cause][prodtype], nanimals);
  RPT_reporting_add_integer (local_data->cumul_num_units_infected_by_cause_and_prodtype[cause][prodtype], 1);
  RPT_reporting_add_real (local_data->cumul_num_animals_infected_by_cause_and_prodtype[cause][prodtype], nanimals);

  /* Infections that occur on the same day as the first detection are included
   * in the value of the firstDet output variables. */
  if (local_data->detection_occurred
      && (local_data->detection_day == event->day))
    {
      RPT_reporting_add_integer (local_data->first_det_u_inf, 1);
      RPT_reporting_add_real (local_data->first_det_a_inf, nanimals);
    }

  /* Update the ratio of recent infections to infections before that.  Note
   * that the value is undefined until a certain number of days has passed,
   * e.g., if we are reporting new infection this week over new infections last
   * week, the value will be undefined until 2 weeks have passed. */
  local_data->nrecent_infections[local_data->recent_day_index]++;
  count = local_data->nrecent_infections[local_data->recent_day_index];
#if DEBUG
  s = g_string_new (NULL);
  g_string_append_printf (s, "recent infection[%u] now = %u", local_data->recent_day_index, count);
#endif
  if (event->day >= local_data->nrecent_days * 2)
    {
      if (local_data->denominator > 0)
        {
          RPT_reporting_set_real (local_data->ratio,
                                  1.0 * (local_data->numerator + count) / local_data->denominator);
#if DEBUG
          g_string_append_printf (s, ", ratio %u/%u = %g",
                                  local_data->numerator + count,
                                  local_data->denominator,
                                  RPT_reporting_get_real (local_data->ratio));
#endif
        }
      else
        {
#if DEBUG
          g_string_append_printf (s, ", denominator=0, ratio remains at old value of %g",
                                  RPT_reporting_get_real (local_data->ratio));
#endif
          ;
        }
    }
  else
    {
#if DEBUG
      g_string_append_printf (s, ", no ratio before day %u", local_data->nrecent_days * 2);
#endif
      ;
    }
#if DEBUG
  g_debug ("%s", s->str);
  g_string_free (s, TRUE);
#endif

#if DEBUG
  g_debug ("----- EXIT handle_infection_event (%s)", MODEL_NAME);
#endif
}



/**
 * Runs this model.
 *
 * @param self the model.
 * @param units a unit list.
 * @param zones a zone list.
 * @param event the event that caused the model to run.
 * @param rng a random number generator.
 * @param queue for any new events the model creates.
 */
void
run (struct adsm_module_t_ *self, UNT_unit_list_t * units, ZON_zone_list_t * zones,
     EVT_event_t * event, RAN_gen_t * rng, EVT_event_queue_t * queue)
{
#if DEBUG
  g_debug ("----- ENTER run (%s)", MODEL_NAME);
#endif

  switch (event->type)
    {
    case EVT_BeforeAnySimulations:
      adsm_declare_outputs (self, queue);
      break;
    case EVT_BeforeEachSimulation:
      handle_before_each_simulation_event (self);
      break;
    case EVT_NewDay:
      handle_new_day_event (self, &(event->u.new_day));
      break;
    case EVT_Infection:
      handle_infection_event (self, &(event->u.infection));
      break;
    case EVT_Detection:
      handle_detection_event (self, &(event->u.detection));
      break;
    default:
      g_error
        ("%s has received a %s event, which it does not listen for.  This should never happen.  Please contact the developer.",
         MODEL_NAME, EVT_event_type_name[event->type]);
    }

#if DEBUG
  g_debug ("----- EXIT run (%s)", MODEL_NAME);
#endif
}



/**
 * Returns a text representation of this model.
 *
 * @param self the model.
 * @return a string.
 */
char *
to_string (struct adsm_module_t_ *self)
{
  local_data_t *local_data;
  GString *s;
  char *chararray;

  local_data = (local_data_t *) (self->model_data);
  s = g_string_new (NULL);
  g_string_sprintf (s, "<%s ratio-period=%u>", MODEL_NAME, local_data->nrecent_days);

  /* don't return the wrapper object */
  chararray = s->str;
  g_string_free (s, FALSE);
  return chararray;
}



/**
 * Frees this model.
 *
 * @param self the model.
 */
void
local_free (struct adsm_module_t_ *self)
{
  local_data_t *local_data;

#if DEBUG
  g_debug ("----- ENTER free (%s)", MODEL_NAME);
#endif

  /* Free the dynamically-allocated parts. */
  local_data = (local_data_t *) (self->model_data);
  g_ptr_array_free (local_data->daily_outputs, /* free_seg = */ TRUE);
  g_ptr_array_free (local_data->cumul_outputs, /* free_seg = */ TRUE);
  g_free (local_data->nrecent_infections);
  g_free (local_data);
  g_ptr_array_free (self->outputs, /* free_seg = */ TRUE); /* also frees all output variables */
  g_free (self);

#if DEBUG
  g_debug ("----- EXIT free (%s)", MODEL_NAME);
#endif
}



/**
 * Returns a new infection monitor.
 */
adsm_module_t *
new (sqlite3 * params, UNT_unit_list_t * units, projPJ projection,
     ZON_zone_list_t * zones)
{
  adsm_module_t *self;
  local_data_t *local_data;
  EVT_event_type_t events_listened_for[] = {
    EVT_BeforeAnySimulations,
    EVT_BeforeEachSimulation,
    EVT_NewDay,
    EVT_Infection,
    EVT_Detection,
    0
  };
  guint nprodtypes;
  UNT_production_type_t prodtype;

#if DEBUG
  g_debug ("----- ENTER new (%s)", MODEL_NAME);
#endif

  self = g_new (adsm_module_t, 1);
  local_data = g_new (local_data_t, 1);

  self->name = MODEL_NAME;
  self->events_listened_for = adsm_setup_events_listened_for (events_listened_for);
  self->outputs = g_ptr_array_new();
  self->model_data = local_data;
  self->run = run;
  self->is_listening_for = adsm_model_is_listening_for;
  self->has_pending_actions = adsm_model_answer_no;
  self->has_pending_infections = adsm_model_answer_no;
  self->to_string = to_string;
  self->printf = adsm_model_printf;
  self->fprintf = adsm_model_fprintf;
  self->free = local_free;

  local_data->daily_outputs = g_ptr_array_new();
  local_data->cumul_outputs = g_ptr_array_new();
  local_data->production_types = units->production_type_names;
  nprodtypes = local_data->production_types->len;
  {
    RPT_bulk_create_t outputs[] = {
      { &local_data->num_units_infected, "infnU", RPT_integer,
        RPT_NoSubcategory, NULL, 0,
        RPT_NoSubcategory, NULL, 0,
        self->outputs, local_data->daily_outputs },

      { &local_data->num_units_infected_by_cause, "infnU%s", RPT_integer,
        RPT_CharArray, ADSM_contact_type_abbrev, ADSM_NCONTACT_TYPES,
        RPT_NoSubcategory, NULL, 0,
        self->outputs, local_data->daily_outputs },

      { &local_data->num_units_infected_by_prodtype, "infnU%s", RPT_integer,
        RPT_GPtrArray, local_data->production_types, nprodtypes,
        RPT_NoSubcategory, NULL, 0,
        self->outputs, local_data->daily_outputs },

      { &local_data->num_units_infected_by_cause_and_prodtype, "infnU%s%s", RPT_integer,
        RPT_CharArray, ADSM_contact_type_abbrev, ADSM_NCONTACT_TYPES,
        RPT_GPtrArray, local_data->production_types, nprodtypes,
        self->outputs, local_data->daily_outputs },

      { &local_data->cumul_num_units_infected, "infcU", RPT_integer,
        RPT_NoSubcategory, NULL, 0,
        RPT_NoSubcategory, NULL, 0,
        self->outputs, local_data->cumul_outputs },

      { &local_data->cumul_num_units_infected_by_cause, "infcU%s", RPT_integer,
        RPT_CharArray, ADSM_contact_type_abbrev, ADSM_NCONTACT_TYPES,
        RPT_NoSubcategory, NULL, 0,
        self->outputs, local_data->cumul_outputs },

      { &local_data->cumul_num_units_infected_by_prodtype, "infcU%s", RPT_integer,
        RPT_GPtrArray, local_data->production_types, nprodtypes,
        RPT_NoSubcategory, NULL, 0,
        self->outputs, local_data->cumul_outputs },

      { &local_data->cumul_num_units_infected_by_cause_and_prodtype, "infcU%s%s", RPT_integer,
        RPT_CharArray, ADSM_contact_type_abbrev, ADSM_NCONTACT_TYPES,
        RPT_GPtrArray, local_data->production_types, nprodtypes,
        self->outputs, local_data->cumul_outputs },

      { &local_data->num_animals_infected, "infnA", RPT_real,
        RPT_NoSubcategory, NULL, 0,
        RPT_NoSubcategory, NULL, 0,
        self->outputs, local_data->daily_outputs },

      { &local_data->num_animals_infected_by_cause, "infnA%s", RPT_real,
        RPT_CharArray, ADSM_contact_type_abbrev, ADSM_NCONTACT_TYPES,
        RPT_NoSubcategory, NULL, 0,
        self->outputs, local_data->daily_outputs },

      { &local_data->num_animals_infected_by_prodtype, "infnA%s", RPT_real,
        RPT_GPtrArray, local_data->production_types, nprodtypes,
        RPT_NoSubcategory, NULL, 0,
        self->outputs, local_data->daily_outputs },

      { &local_data->num_animals_infected_by_cause_and_prodtype, "infnA%s%s", RPT_real,
        RPT_CharArray, ADSM_contact_type_abbrev, ADSM_NCONTACT_TYPES,
        RPT_GPtrArray, local_data->production_types, nprodtypes,
        self->outputs, local_data->daily_outputs },

      { &local_data->cumul_num_animals_infected, "infcA", RPT_real,
        RPT_NoSubcategory, NULL, 0,
        RPT_NoSubcategory, NULL, 0,
        self->outputs, local_data->cumul_outputs },

      { &local_data->cumul_num_animals_infected_by_cause, "infcA%s", RPT_real,
        RPT_CharArray, ADSM_contact_type_abbrev, ADSM_NCONTACT_TYPES,
        RPT_NoSubcategory, NULL, 0,
        self->outputs, local_data->cumul_outputs },

      { &local_data->cumul_num_animals_infected_by_prodtype, "infcA%s", RPT_real,
        RPT_GPtrArray, local_data->production_types, nprodtypes,
        RPT_NoSubcategory, NULL, 0,
        self->outputs, local_data->cumul_outputs },

      { &local_data->cumul_num_animals_infected_by_cause_and_prodtype, "infcA%s%s", RPT_real,
        RPT_CharArray, ADSM_contact_type_abbrev, ADSM_NCONTACT_TYPES,
        RPT_GPtrArray, local_data->production_types, nprodtypes,
        self->outputs, local_data->cumul_outputs },

      { &local_data->first_det_u_inf, "firstDetUInf", RPT_integer,
        RPT_NoSubcategory, NULL, 0,
        RPT_NoSubcategory, NULL, 0,
        self->outputs, NULL },

      { &local_data->first_det_a_inf, "firstDetAInf", RPT_real,
        RPT_NoSubcategory, NULL, 0,
        RPT_NoSubcategory, NULL, 0,
        self->outputs, NULL },

      { &local_data->ratio, "ratio", RPT_real,
        RPT_NoSubcategory, NULL, 0,
        RPT_NoSubcategory, NULL, 0,
        self->outputs, NULL },

      { NULL }
    };  
    RPT_bulk_create (outputs);
  }

  /* Dispose of a few output variables we aren't interested in, to keep the
   * output neater. */
  g_ptr_array_remove_fast (self->outputs, local_data->num_units_infected_by_cause[ADSM_UnspecifiedInfectionType] );
  g_ptr_array_remove_fast (self->outputs, local_data->cumul_num_units_infected_by_cause[ADSM_UnspecifiedInfectionType] );
  g_ptr_array_remove_fast (self->outputs, local_data->num_animals_infected_by_cause[ADSM_UnspecifiedInfectionType] );
  g_ptr_array_remove_fast (self->outputs, local_data->cumul_num_animals_infected_by_cause[ADSM_UnspecifiedInfectionType] );
  for (prodtype = 0; prodtype < nprodtypes; prodtype++)
    {
      g_ptr_array_remove_fast (self->outputs, local_data->num_units_infected_by_cause_and_prodtype[ADSM_UnspecifiedInfectionType][prodtype] );
      g_ptr_array_remove_fast (self->outputs, local_data->cumul_num_units_infected_by_cause_and_prodtype[ADSM_UnspecifiedInfectionType][prodtype] );
      g_ptr_array_remove_fast (self->outputs, local_data->num_animals_infected_by_cause_and_prodtype[ADSM_UnspecifiedInfectionType][prodtype] );
      g_ptr_array_remove_fast (self->outputs, local_data->cumul_num_animals_infected_by_cause_and_prodtype[ADSM_UnspecifiedInfectionType][prodtype] );
    }

  /* A list to store the number of new infections on each day for the recent
   * past. */
  local_data->nrecent_days = 7;
  local_data->nrecent_infections = g_new0 (unsigned int, local_data->nrecent_days * 2);
  local_data->recent_day_index = 0;

#if DEBUG
  g_debug ("----- EXIT new (%s)", MODEL_NAME);
#endif

  return self;
}

/* end of file infection_monitor.c */
