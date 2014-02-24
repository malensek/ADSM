/** @file vaccination_list_monitor.c
 * Tracks the number of units waiting to be vaccinated.
 *
 * @author Neil Harvey <nharve01@uoguelph.ca><br>
 *   School of Computer Science, University of Guelph<br>
 *   Guelph, ON N1G 2W1<br>
 *   CANADA
 * @version 0.1
 * @date April 2004
 *
 * Copyright &copy; University of Guelph, 2004-2009
 * 
 * This program is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the Free
 * Software Foundation; either version 2 of the License, or (at your option)
 * any later version.
 */

#if HAVE_CONFIG_H
#  include <config.h>
#endif

/* To avoid name clashes when multiple modules have the same interface. */
#define new vaccination_list_monitor_new
#define run vaccination_list_monitor_run
#define reset vaccination_list_monitor_reset
#define events_listened_for vaccination_list_monitor_events_listened_for
#define local_free vaccination_list_monitor_free
#define handle_before_any_simulations_event vaccination_list_monitor_handle_before_any_simulations_event
#define handle_new_day_event vaccination_list_monitor_handle_new_day_event
#define handle_commitment_to_vaccinate_event vaccination_list_monitor_handle_commitment_to_vaccinate_event
#define handle_vaccination_event vaccination_list_monitor_handle_vaccination_event
#define handle_vaccination_canceled_event vaccination_list_monitor_handle_vaccination_canceled_event

#include "module.h"

#if STDC_HEADERS
#  include <string.h>
#endif

#include "vaccination_list_monitor.h"

/** This must match an element name in the DTD. */
#define MODEL_NAME "vaccination-list-monitor"



#define NEVENTS_LISTENED_FOR 5
EVT_event_type_t events_listened_for[] =
  { EVT_BeforeAnySimulations, EVT_NewDay, EVT_CommitmentToVaccinate,
    EVT_VaccinationCanceled, EVT_Vaccination };



/** Specialized information for this model. */
typedef struct
{
  GPtrArray *production_types;
  unsigned int nunits;          /* Number of units. */
  GHashTable *status; /**< The status of each unit with respect to vaccination.
    If the unit is not awaiting vaccination, it will not be present in the
    table.  If it is awaiting vaccination, its associated value will be an
    integer (cast to a gpointer using GINT_TO_POINTER) indicating how many
    times the unit is in queue. */
  unsigned int peak_nunits;
  double peak_nanimals;
  unsigned int peak_wait;
  double sum; /**< The numerator for calculating the average wait time. */
  unsigned int count; /**< The denominator for calculating the average wait time. */
  RPT_reporting_t *nunits_awaiting_vaccination;
  RPT_reporting_t *nunits_awaiting_vaccination_by_prodtype;
  unsigned int unique_units_awaiting_vaccination;
  RPT_reporting_t *nanimals_awaiting_vaccination;
  RPT_reporting_t *nanimals_awaiting_vaccination_by_prodtype;
  double unique_animals_awaiting_vaccination;
  RPT_reporting_t *peak_nunits_awaiting_vaccination;
  RPT_reporting_t *peak_nunits_awaiting_vaccination_day;
  RPT_reporting_t *peak_nanimals_awaiting_vaccination;
  RPT_reporting_t *peak_nanimals_awaiting_vaccination_day;
  RPT_reporting_t *peak_wait_time;
  RPT_reporting_t *average_wait_time;
  RPT_reporting_t *unit_days_in_queue;
  RPT_reporting_t *animal_days_in_queue;
}
local_data_t;



/**
 * Before any simulations, this module announces the output variables it is
 * recording.
 *
 * @param self this module.
 * @param queue for any new events this function creates.
 */
void
handle_before_any_simulations_event (struct spreadmodel_model_t_ *self,
                                     EVT_event_queue_t *queue)
{
  unsigned int n, i;
  RPT_reporting_t *output;
  GPtrArray *outputs = NULL;

  n = self->outputs->len;
  for (i = 0; i < n; i++)
    {
      output = (RPT_reporting_t *) g_ptr_array_index (self->outputs, i);
      if (output->frequency != RPT_never)
        {
          if (outputs == NULL)
            outputs = g_ptr_array_new();
          g_ptr_array_add (outputs, output);
        }
    }

  if (outputs != NULL)
    EVT_event_enqueue (queue, EVT_new_declaration_of_outputs_event (outputs));
  /* We don't free the pointer array, that will be done when the event is freed
   * after all interested modules have processed it. */

  return;
}



/**
 * Responds to a new day event by updating unit-days in queue and animal-days
 * in queue.
 *
 * @param self the model.
 */
void
handle_new_day_event (struct spreadmodel_model_t_ *self)
{
  local_data_t *local_data;

#if DEBUG
  g_debug ("----- ENTER handle_new_day_event (%s)", MODEL_NAME);
#endif

  local_data = (local_data_t *) (self->model_data);

  RPT_reporting_add_integer (local_data->unit_days_in_queue,
                             local_data->unique_units_awaiting_vaccination,
                             NULL);
  RPT_reporting_add_real (local_data->animal_days_in_queue,
                          local_data->unique_animals_awaiting_vaccination,
                          NULL);

#if DEBUG
  g_debug ("----- EXIT handle_new_day_event (%s)", MODEL_NAME);
#endif

  return;
}



/**
 * Responds to a commitment to vaccinate event by recording the unit's status
 * as "waiting".
 *
 * @param self the model.
 * @param event a commitment to vaccinate event.
 */
void
handle_commitment_to_vaccinate_event (struct spreadmodel_model_t_ *self,
                                      EVT_commitment_to_vaccinate_event_t * event)
{
  local_data_t *local_data;
  UNT_unit_t *unit;
  gpointer p;
  int count;
  unsigned int nunits;
  double nanimals;

#if DEBUG
  g_debug ("----- ENTER handle_commitment_to_vaccinate_event (%s)", MODEL_NAME);
#endif

  local_data = (local_data_t *) (self->model_data);
  unit = event->unit;

  /* For each unit, we maintain a count of how many times the unit is in
   * queue. */
  p = g_hash_table_lookup (local_data->status, unit);
  if (p == NULL)
    {
      g_hash_table_insert (local_data->status, unit, GINT_TO_POINTER(1));
      local_data->unique_units_awaiting_vaccination += 1;
      local_data->unique_animals_awaiting_vaccination += (double)(unit->size);
    }
  else
    {
      count = GPOINTER_TO_INT(p);
      g_hash_table_insert (local_data->status, unit, GINT_TO_POINTER(count+1));
    }

  if (NULL != spreadmodel_queue_unit_for_vaccination)
    {
      spreadmodel_queue_unit_for_vaccination (unit->index);
    }

  /* Increment the counts of vaccinations still to do. */
  RPT_reporting_add_integer (local_data->nunits_awaiting_vaccination, 1, NULL);
  if (local_data->nunits_awaiting_vaccination_by_prodtype->frequency != RPT_never)
    RPT_reporting_add_integer1 (local_data->nunits_awaiting_vaccination_by_prodtype, 1,
                                unit->production_type_name);
  nunits = RPT_reporting_get_integer (local_data->nunits_awaiting_vaccination, NULL);
  if (nunits > local_data->peak_nunits)
    {
      local_data->peak_nunits = nunits;
      RPT_reporting_set_integer (local_data->peak_nunits_awaiting_vaccination, nunits, NULL);
      RPT_reporting_set_integer (local_data->peak_nunits_awaiting_vaccination_day, event->day, NULL);
    }

  RPT_reporting_add_real (local_data->nanimals_awaiting_vaccination, (double)(unit->size), NULL);
  if (local_data->nanimals_awaiting_vaccination_by_prodtype->frequency != RPT_never)
    RPT_reporting_add_real1 (local_data->nanimals_awaiting_vaccination_by_prodtype,
                             (double)(unit->size), unit->production_type_name);
  nanimals = RPT_reporting_get_real (local_data->nanimals_awaiting_vaccination, NULL);
  if (nanimals > local_data->peak_nanimals)
    {
      local_data->peak_nanimals = nanimals;
      RPT_reporting_set_real (local_data->peak_nanimals_awaiting_vaccination, nanimals,
                                 NULL);
      RPT_reporting_set_integer (local_data->peak_nanimals_awaiting_vaccination_day, event->day,
                                 NULL);
    }

#if DEBUG
  g_debug ("----- EXIT handle_commitment_to_vaccinate_event (%s)", MODEL_NAME);
#endif
}



/**
 * Responds to a vaccination event by removing the unit's "waiting" status and
 * updating the peak and average wait times.
 *
 * @param self the model.
 * @param event a vaccination event.
 */
void
handle_vaccination_event (struct spreadmodel_model_t_ *self, EVT_vaccination_event_t * event)
{
  local_data_t *local_data;
  UNT_unit_t *unit;
  gpointer p;
  int count;
  unsigned int wait;

#if DEBUG
  g_debug ("----- ENTER handle_vaccination_event (%s)", MODEL_NAME);
#endif

  local_data = (local_data_t *) (self->model_data);
  unit = event->unit;

  /* Special case: if a unit's starting state is Vaccine Immune, it won't be on
   * a waiting list and it won't affect the various counts maintained by this
   * monitor. */
  p = g_hash_table_lookup (local_data->status, unit);
  if (p != NULL)
    {
      /* The day when the unit went onto the waiting list is recorded in the
       * vaccination event. */
      wait = event->day - event->day_commitment_made;

      /* Update the peak wait time. */
      local_data->peak_wait = MAX (local_data->peak_wait, wait);
      RPT_reporting_set_integer (local_data->peak_wait_time, local_data->peak_wait, NULL);

      /* Update the average wait time. */
      local_data->sum += wait;
      local_data->count += 1;
      RPT_reporting_set_real (local_data->average_wait_time,
                              local_data->sum / local_data->count, NULL);

      /* Mark the unit as no longer on a waiting list. */
      count = GPOINTER_TO_INT(p);
      if (count == 1)
        {
          g_hash_table_remove (local_data->status, unit);
          local_data->unique_units_awaiting_vaccination -= 1;
          local_data->unique_animals_awaiting_vaccination -= (double)(unit->size);
        }
      else
        g_hash_table_insert (local_data->status, unit, GINT_TO_POINTER(count-1));

      /* Decrement the counts of vaccinations still to do. */
      RPT_reporting_sub_integer (local_data->nunits_awaiting_vaccination, 1, NULL);
      if (local_data->nunits_awaiting_vaccination_by_prodtype->frequency != RPT_never)
        RPT_reporting_sub_integer1 (local_data->nunits_awaiting_vaccination_by_prodtype, 1,
                                    unit->production_type_name);

      RPT_reporting_sub_real (local_data->nanimals_awaiting_vaccination, (double)(unit->size), NULL);
      if (local_data->nanimals_awaiting_vaccination_by_prodtype->frequency != RPT_never)
        RPT_reporting_sub_real1 (local_data->nanimals_awaiting_vaccination_by_prodtype,
                                 (double)(unit->size), unit->production_type_name);
    }

#if DEBUG
  g_debug ("----- EXIT handle_vaccination_event (%s)", MODEL_NAME);
#endif
}



/**
 * Responds to a vaccination canceled event by removing the unit's "waiting"
 * status, if it is waiting for vaccination.
 *
 * @param self the model.
 * @param event a destruction event.
 */
void
handle_vaccination_canceled_event (struct spreadmodel_model_t_ *self,
                                   EVT_vaccination_canceled_event_t * event)
{
  local_data_t *local_data;
  UNT_unit_t *unit;
  gpointer p;
  int count;
  UNT_control_t update;
#if DEBUG
  g_debug ("----- ENTER handle_vaccination_canceled_event (%s)", MODEL_NAME);
#endif

  local_data = (local_data_t *) (self->model_data);
  unit = event->unit;

  /* Inform the GUI of the cancellation. */
  update.unit_index = unit->index;
  update.day_commitment_made = event->day_commitment_made;
  update.reason = 0; /* This is unused for "vaccination canceled" events */
  
#ifdef USE_SC_GUILIB
  sc_cancel_unit_vaccination( event->day, unit, update );
#else  
  if (NULL != spreadmodel_cancel_unit_vaccination)
    {
      spreadmodel_cancel_unit_vaccination (update);
    }
#endif  

  /* Mark the unit as no longer on a waiting list. */
  p = g_hash_table_lookup (local_data->status, unit);
  g_assert (p != NULL);
  count = GPOINTER_TO_INT(p);
  if (count == 1)
    {
      g_hash_table_remove (local_data->status, unit);
      local_data->unique_units_awaiting_vaccination -= 1;
      local_data->unique_animals_awaiting_vaccination -= (double)(unit->size);
    }
  else
    g_hash_table_insert (local_data->status, unit, GINT_TO_POINTER(count-1));

  /* Decrement the counts of vaccinations still to do. */
  RPT_reporting_sub_integer (local_data->nunits_awaiting_vaccination, 1, NULL);
  if (local_data->nunits_awaiting_vaccination_by_prodtype->frequency != RPT_never)
    RPT_reporting_sub_integer1 (local_data->nunits_awaiting_vaccination_by_prodtype, 1,
                                unit->production_type_name);

  RPT_reporting_sub_real (local_data->nanimals_awaiting_vaccination, (double)(unit->size), NULL);
  if (local_data->nanimals_awaiting_vaccination_by_prodtype->frequency != RPT_never)
    RPT_reporting_sub_real1 (local_data->nanimals_awaiting_vaccination_by_prodtype,
                             (double)(unit->size), unit->production_type_name);

#if DEBUG
  g_debug ("----- EXIT handle_vaccination_canceled_event (%s)", MODEL_NAME);
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
run (struct spreadmodel_model_t_ *self, UNT_unit_list_t * units, ZON_zone_list_t * zones,
     EVT_event_t * event, RAN_gen_t * rng, EVT_event_queue_t * queue)
{
#if DEBUG
  g_debug ("----- ENTER run (%s)", MODEL_NAME);
#endif

  switch (event->type)
    {
    case EVT_BeforeAnySimulations:
      handle_before_any_simulations_event (self, queue);
      break;
    case EVT_NewDay:
      handle_new_day_event (self);
      break;
    case EVT_CommitmentToVaccinate:
      handle_commitment_to_vaccinate_event (self, &(event->u.commitment_to_vaccinate));
      break;
    case EVT_VaccinationCanceled:
      handle_vaccination_canceled_event (self, &(event->u.vaccination_canceled));
      break;
    case EVT_Vaccination:
      handle_vaccination_event (self, &(event->u.vaccination));
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
 * Resets this model after a simulation run.
 *
 * @param self the model.
 */
void
reset (struct spreadmodel_model_t_ *self)
{
  local_data_t *local_data;

#if DEBUG
  g_debug ("----- ENTER reset (%s)", MODEL_NAME);
#endif

  local_data = (local_data_t *) (self->model_data);

  g_hash_table_remove_all (local_data->status);

  RPT_reporting_zero (local_data->nunits_awaiting_vaccination);
  RPT_reporting_zero (local_data->nunits_awaiting_vaccination_by_prodtype);
  local_data->unique_units_awaiting_vaccination = 0;
  RPT_reporting_zero (local_data->nanimals_awaiting_vaccination);
  RPT_reporting_zero (local_data->nunits_awaiting_vaccination_by_prodtype);
  local_data->unique_animals_awaiting_vaccination = 0;
  RPT_reporting_zero (local_data->peak_nunits_awaiting_vaccination);
  RPT_reporting_set_null (local_data->peak_nunits_awaiting_vaccination_day, NULL);
  RPT_reporting_zero (local_data->peak_nanimals_awaiting_vaccination);
  RPT_reporting_set_null (local_data->peak_nanimals_awaiting_vaccination_day, NULL);
  RPT_reporting_set_null (local_data->peak_wait_time, NULL);
  RPT_reporting_set_null (local_data->average_wait_time, NULL);
  RPT_reporting_zero (local_data->unit_days_in_queue);
  RPT_reporting_zero (local_data->animal_days_in_queue);

  local_data->peak_nunits = local_data->peak_nanimals = 0;
  local_data->peak_wait = 0;
  local_data->sum = local_data->count = 0;

#if DEBUG
  g_debug ("----- EXIT reset (%s)", MODEL_NAME);
#endif
}



/**
 * Frees this model.
 *
 * @param self the model.
 */
void
local_free (struct spreadmodel_model_t_ *self)
{
  local_data_t *local_data;

#if DEBUG
  g_debug ("----- ENTER free (%s)", MODEL_NAME);
#endif

  /* Free the dynamically-allocated parts. */
  local_data = (local_data_t *) (self->model_data);
  g_hash_table_destroy (local_data->status);

  RPT_free_reporting (local_data->nunits_awaiting_vaccination);
  RPT_free_reporting (local_data->nunits_awaiting_vaccination_by_prodtype);
  RPT_free_reporting (local_data->nanimals_awaiting_vaccination);
  RPT_free_reporting (local_data->nanimals_awaiting_vaccination_by_prodtype);
  RPT_free_reporting (local_data->peak_nunits_awaiting_vaccination);
  RPT_free_reporting (local_data->peak_nunits_awaiting_vaccination_day);
  RPT_free_reporting (local_data->peak_nanimals_awaiting_vaccination);
  RPT_free_reporting (local_data->peak_nanimals_awaiting_vaccination_day);
  RPT_free_reporting (local_data->peak_wait_time);
  RPT_free_reporting (local_data->average_wait_time);
  RPT_free_reporting (local_data->unit_days_in_queue);
  RPT_free_reporting (local_data->animal_days_in_queue);

  g_free (local_data);
  g_ptr_array_free (self->outputs, TRUE);
  g_free (self);

#if DEBUG
  g_debug ("----- EXIT free (%s)", MODEL_NAME);
#endif
}



/**
 * Returns a new vaccination list monitor.
 */
spreadmodel_model_t *
new (scew_element * params, UNT_unit_list_t * units, projPJ projection,
     ZON_zone_list_t * zones)
{
  spreadmodel_model_t *self;
  local_data_t *local_data;
  scew_element *e;
  scew_list *ee, *iter;
  const XML_Char *variable_name;
  RPT_frequency_t freq;
  gboolean success;
  gboolean broken_down;
  unsigned int i;      /* loop counter */

#if DEBUG
  g_debug ("----- ENTER new (%s)", MODEL_NAME);
#endif

  self = g_new (spreadmodel_model_t, 1);
  local_data = g_new (local_data_t, 1);

  self->name = MODEL_NAME;
  self->events_listened_for = events_listened_for;
  self->nevents_listened_for = NEVENTS_LISTENED_FOR;
  self->outputs = g_ptr_array_sized_new (10);
  self->model_data = local_data;
  self->set_params = NULL;
  self->run = run;
  self->reset = reset;
  self->is_singleton = spreadmodel_model_answer_yes;
  self->is_listening_for = spreadmodel_model_is_listening_for;
  self->has_pending_actions = spreadmodel_model_answer_no;
  self->has_pending_infections = spreadmodel_model_answer_no;
  self->to_string = spreadmodel_model_to_string_default;
  self->printf = spreadmodel_model_printf;
  self->fprintf = spreadmodel_model_fprintf;
  self->free = local_free;

  /* Make sure the right XML subtree was sent. */
  g_assert (strcmp (scew_element_name (params), MODEL_NAME) == 0);

  local_data->nunits_awaiting_vaccination =
    RPT_new_reporting ("vacwUAll", RPT_integer, RPT_never);
  local_data->nunits_awaiting_vaccination_by_prodtype =
    RPT_new_reporting ("vacwU", RPT_group, RPT_never);
  local_data->nanimals_awaiting_vaccination =
    RPT_new_reporting ("vacwAAll", RPT_real, RPT_never);
  local_data->nanimals_awaiting_vaccination_by_prodtype =
    RPT_new_reporting ("vacwA", RPT_group, RPT_never);
  local_data->peak_nunits_awaiting_vaccination =
    RPT_new_reporting ("vacwUMax", RPT_integer, RPT_never);
  local_data->peak_nunits_awaiting_vaccination_day =
    RPT_new_reporting ("vacwUMaxDay", RPT_integer, RPT_never);
  local_data->peak_nanimals_awaiting_vaccination =
    RPT_new_reporting ("vacwAMax", RPT_real, RPT_never);
  local_data->peak_nanimals_awaiting_vaccination_day =
    RPT_new_reporting ("vacwAMaxDay", RPT_integer, RPT_never);
  local_data->peak_wait_time =
    RPT_new_reporting ("vacwUTimeMax", RPT_integer, RPT_never);
  local_data->average_wait_time =
    RPT_new_reporting ("vacwUTimeAvg", RPT_real, RPT_never);
  local_data->unit_days_in_queue =
    RPT_new_reporting ("vacwUDaysInQueue", RPT_integer, RPT_never);
  local_data->animal_days_in_queue =
    RPT_new_reporting ("vacwADaysInQueue", RPT_real, RPT_never);
  g_ptr_array_add (self->outputs, local_data->nunits_awaiting_vaccination);
  g_ptr_array_add (self->outputs, local_data->nunits_awaiting_vaccination_by_prodtype);
  g_ptr_array_add (self->outputs, local_data->nanimals_awaiting_vaccination);
  g_ptr_array_add (self->outputs, local_data->nanimals_awaiting_vaccination_by_prodtype);
  g_ptr_array_add (self->outputs, local_data->peak_nunits_awaiting_vaccination);
  g_ptr_array_add (self->outputs, local_data->peak_nunits_awaiting_vaccination_day);
  g_ptr_array_add (self->outputs, local_data->peak_nanimals_awaiting_vaccination);
  g_ptr_array_add (self->outputs, local_data->peak_nanimals_awaiting_vaccination_day);
  g_ptr_array_add (self->outputs, local_data->peak_wait_time);
  g_ptr_array_add (self->outputs, local_data->average_wait_time);
  g_ptr_array_add (self->outputs, local_data->unit_days_in_queue);
  g_ptr_array_add (self->outputs, local_data->animal_days_in_queue);

  /* Set the reporting frequency for the output variables. */
  ee = scew_element_list_by_name (params, "output");
#if DEBUG
  g_debug ("%u output variables", scew_list_size(ee));
#endif
  for (iter = ee; iter != NULL; iter = scew_list_next(iter))
    {
      e = (scew_element *) scew_list_data (iter);
      variable_name = scew_element_contents (scew_element_by_name (e, "variable-name"));
      freq = RPT_string_to_frequency (scew_element_contents
                                      (scew_element_by_name (e, "frequency")));
      broken_down = PAR_get_boolean (scew_element_by_name (e, "broken-down"), &success);
      if (!success)
      	broken_down = FALSE;
      broken_down = broken_down || (g_strstr_len (variable_name, -1, "-by-") != NULL); 
      /* Starting at version 3.2 we accept either the old, verbose output
       * variable names or the new shorter ones. */
      if (strcmp (variable_name, "vacwU") == 0
          || strncmp (variable_name, "num-units-awaiting-vaccination", 30) == 0)
        {
          RPT_reporting_set_frequency (local_data->nunits_awaiting_vaccination, freq);
          if (broken_down)
            RPT_reporting_set_frequency (local_data->nunits_awaiting_vaccination_by_prodtype, freq);
        }
      else if (strcmp (variable_name, "vacwA") == 0
               || strncmp (variable_name, "num-animals-awaiting-vaccination", 32) == 0)
        {
          RPT_reporting_set_frequency (local_data->nanimals_awaiting_vaccination, freq);
          if (broken_down)
            RPT_reporting_set_frequency (local_data->nanimals_awaiting_vaccination_by_prodtype, freq);
        }
      else if (strcmp (variable_name, "vacwUMax") == 0
               || strcmp (variable_name, "peak-num-units-awaiting-vaccination") == 0)
        RPT_reporting_set_frequency (local_data->peak_nunits_awaiting_vaccination, freq);
      else if (strcmp (variable_name, "vacwUMaxDay") == 0)
        RPT_reporting_set_frequency (local_data->peak_nunits_awaiting_vaccination_day, freq);
      else if (strcmp (variable_name, "vacwAMax") == 0
               || strcmp (variable_name, "peak-num-animals-awaiting-vaccination") == 0)
        RPT_reporting_set_frequency (local_data->peak_nanimals_awaiting_vaccination, freq);
      else if (strcmp (variable_name, "vacwAMaxDay") == 0)
        RPT_reporting_set_frequency (local_data->peak_nanimals_awaiting_vaccination_day, freq);
      else if (strcmp (variable_name, "vacwUTimeMax") == 0
               || strcmp (variable_name, "peak-wait-time") == 0
               || strcmp (variable_name, "peak-vaccination-wait-time") == 0)
        RPT_reporting_set_frequency (local_data->peak_wait_time, freq);
      else if (strcmp (variable_name, "vacwUTimeAvg") == 0
               || strcmp (variable_name, "average-wait-time") == 0
               || strcmp (variable_name, "average-vaccination-wait-time") == 0)
        RPT_reporting_set_frequency (local_data->average_wait_time, freq);
      else if (strcmp (variable_name, "vacwUDaysInQueue") == 0)
        RPT_reporting_set_frequency (local_data->unit_days_in_queue, freq);
      else if (strcmp (variable_name, "vacwADaysInQueue") == 0)
        RPT_reporting_set_frequency (local_data->animal_days_in_queue, freq);
      else
        g_warning ("no output variable named \"%s\", ignoring", variable_name);        
    }
  scew_list_free (ee);

  local_data->nunits = UNT_unit_list_length (units);
  local_data->production_types = units->production_type_names;
  for (i = 0; i < local_data->production_types->len; i++)
    {
      RPT_reporting_set_integer1 (local_data->nunits_awaiting_vaccination_by_prodtype, 0,
                                  (char *) g_ptr_array_index (local_data->production_types, i));
      RPT_reporting_set_real1 (local_data->nanimals_awaiting_vaccination_by_prodtype, 0,
                               (char *) g_ptr_array_index (local_data->production_types, i));
    }

  /* Initialize the unit status table. */
  local_data->status = g_hash_table_new (g_direct_hash, g_direct_equal);
  
#if DEBUG
  g_debug ("----- EXIT new (%s)", MODEL_NAME);
#endif

  return self;
}

/* end of file vaccination_list_monitor.c */