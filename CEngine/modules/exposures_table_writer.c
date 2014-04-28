/** @file exposures_table_writer.c
 * Writes out a table of exposures and infections in comma-separated value
 * (csv) format.
 *
 * @author Neil Harvey <nharve01@uoguelph.ca><br>
 *   School of Computer Science, University of Guelph<br>
 *   Guelph, ON N1G 2W1<br>
 *   CANADA
 * 
 * This program is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the Free
 * Software Foundation; either version 2 of the License, or (at your option)
 * any later version.
 *
 * @todo check errno after opening the file for writing.
 */

#if HAVE_CONFIG_H
#  include <config.h>
#endif

/* To avoid name clashes when multiple modules have the same interface. */
#define new exposures_table_writer_new
#define run exposures_table_writer_run
#define reset exposures_table_writer_reset
#define events_listened_for exposures_table_writer_events_listened_for
#define to_string exposures_table_writer_to_string
#define local_free exposures_table_writer_free
#define handle_output_dir_event exposures_table_writer_handle_output_dir_event
#define handle_before_any_simulations_event exposures_table_writer_handle_before_any_simulations_event
#define handle_before_each_simulation_event exposures_table_writer_handle_before_each_simulation_event
#define handle_exposure_event exposures_table_writer_handle_exposure_event
#define handle_infection_event exposures_table_writer_handle_infection_event

#include "module.h"
#include "module_util.h"

#if STDC_HEADERS
#  include <string.h>
#endif

#if HAVE_MATH_H
#  include <math.h>
#endif

#if HAVE_STRINGS_H
#  include <strings.h>
#endif

#if HAVE_UNISTD_H
#  include <unistd.h>
#endif

#include "exposures_table_writer.h"

/** This must match an element name in the DTD. */
#define MODEL_NAME "exposures-table-writer"



#define NEVENTS_LISTENED_FOR 5
EVT_event_type_t events_listened_for[] = {
  EVT_OutputDirectory,
  EVT_BeforeAnySimulations,
  EVT_BeforeEachSimulation,
  EVT_Exposure,
  EVT_Infection
};



/* Specialized information for this module. */
typedef struct
{
  char *filename; /* with the .csv extension */
  GIOChannel *channel; /* The open file. */
  gboolean channel_is_stdout;
  int run_number;
  GString *buf;
}
local_data_t;



/**
 * Responds to an "output directory" event by prepending the directory to the
 * its output filename.
 *
 * @param self this module.
 * @param event an output directory event.
 */
void
handle_output_dir_event (struct spreadmodel_model_t_ * self,
                         EVT_output_dir_event_t *event)
{
  local_data_t *local_data;
  char *tmp;

#if DEBUG
  g_debug ("----- ENTER handle_output_dir_event (%s)", MODEL_NAME);
#endif

  local_data = (local_data_t *) (self->model_data);
  if (local_data->channel_is_stdout == FALSE)
    {
      tmp = local_data->filename;
      local_data->filename = g_build_filename (event->output_dir, tmp, NULL);
      g_free (tmp);
      #if DEBUG
        g_debug ("filename is now %s", local_data->filename);
      #endif
    }

#if DEBUG
  g_debug ("----- EXIT handle_output_dir_event (%s)", MODEL_NAME);
#endif
  return;
}



/**
 * Before any simulations, this module sets the run number to zero, opens its
 * output file and writes the table header.
 *
 * @param self this module.
 */
void
handle_before_any_simulations_event (struct spreadmodel_model_t_ * self)
{
  local_data_t *local_data;
  GError *error = NULL;

#if DEBUG
  g_debug ("----- ENTER handle_before_any_simulations_event (%s)", MODEL_NAME);
#endif

  local_data = (local_data_t *) (self->model_data);
  if (local_data->channel_is_stdout)
    {
      #ifdef G_OS_UNIX
        local_data->channel = g_io_channel_unix_new (STDOUT_FILENO);
      #endif
      #ifdef G_OS_WIN32
        local_data->channel = g_io_channel_win32_new_fd (STDOUT_FILENO);
      #endif
    }
  else
    {
      local_data->channel = g_io_channel_new_file (local_data->filename, "w", &error);
      if (local_data->channel == NULL)
        {
          g_error ("%s: %s error when attempting to open file \"%s\"",
                   MODEL_NAME, error->message, local_data->filename);
        }
    }
  g_io_channel_write_chars (local_data->channel,
                            "Run,Day,Type,Reason,Source ID,Production type,Lat,Lon,Zone,Recipient ID,Production type,Lat,Lon,Zone\n",
                            -1 /* assume null-terminated string */,
                            NULL, &error);
  g_io_channel_flush (local_data->channel, &error);

  /* This count will be incremented for each new simulation. */
  local_data->run_number = 0;

#if DEBUG
  g_debug ("----- EXIT handle_before_any_simulations_event (%s)", MODEL_NAME);
#endif
}



/**
 * Before each simulation, this module increments its "run number".
 *
 * @param self this module.
 */
void
handle_before_each_simulation_event (struct spreadmodel_model_t_ * self)
{
  local_data_t *local_data;

#if DEBUG
  g_debug ("----- ENTER handle_before_each_simulation_event (%s)", MODEL_NAME);
#endif

  local_data = (local_data_t *) (self->model_data);
  local_data->run_number++;

#if DEBUG
  g_debug ("----- EXIT handle_before_each_simulation_event (%s)", MODEL_NAME);
#endif
}



/**
 * Responds to an exposure event by writing a table row.
 *
 * @param self this module.
 * @param event an exposure event.
 * @param zones the list of zones.
 */
void
handle_exposure_event (struct spreadmodel_model_t_ *self,
                       EVT_exposure_event_t * event,
                       ZON_zone_list_t *zones)
{
  local_data_t *local_data;
  ZON_zone_fragment_t *exposing_unit_zone, *exposed_unit_zone, *background_zone;
  GError *error = NULL;

#if DEBUG
  g_debug ("----- ENTER handle_exposure_event (%s)", MODEL_NAME);
#endif

  local_data = (local_data_t *) (self->model_data);

  /* Show all traceable exposures, but show untraceable exposures only if they
   * are adequate. */

  if (event->traceable || event->adequate)
    {
      background_zone = ZON_zone_list_get_background (zones);
      exposed_unit_zone = zones->membership[event->exposed_unit->index];

      /* The data fields are: run, day, type, reason, source ID, source production
       * type, source latitude, source longitude, source zone, recipient ID,
       * recipient production type, recipient latitude, recipient longitude,
       * recipient zone. */
      if (event->exposing_unit == NULL)
        g_string_printf (local_data->buf,
                         "%i,%i,Exposure,%s,,,,,,%s,%s,%g,%g,%s\n",
                         local_data->run_number,
                         event->day,
                         SPREADMODEL_contact_type_abbrev[event->contact_type],
                         event->exposed_unit->official_id,
                         event->exposed_unit->production_type_name,
                         event->exposed_unit->latitude,
                         event->exposed_unit->longitude,
                         ZON_same_zone (exposed_unit_zone, background_zone) ? "" : exposed_unit_zone->parent->name);
      else
        {
          exposing_unit_zone = zones->membership[event->exposing_unit->index];
          g_string_printf (local_data->buf,
                           "%i,%i,Exposure,%s,%s,%s,%g,%g,%s,%s,%s,%g,%g,%s\n",
                           local_data->run_number,
                           event->day,
                           SPREADMODEL_contact_type_abbrev[event->contact_type],
                           event->exposing_unit->official_id,
                           event->exposing_unit->production_type_name,
                           event->exposing_unit->latitude,
                           event->exposing_unit->longitude,
                           ZON_same_zone (exposing_unit_zone, background_zone) ? "" : exposing_unit_zone->parent->name,
                           event->exposed_unit->official_id,
                           event->exposed_unit->production_type_name,
                           event->exposed_unit->latitude,
                           event->exposed_unit->longitude,
                           ZON_same_zone (exposed_unit_zone, background_zone) ? "" : exposed_unit_zone->parent->name);
        }
      g_io_channel_write_chars (local_data->channel, local_data->buf->str, 
                                -1 /* assume null-terminated string */,
                                NULL, &error);
    }

#if DEBUG
  g_debug ("----- EXIT handle_exposure_event (%s)", MODEL_NAME);
#endif
  return;
}



/**
 * Responds to an infection event by writing a table row.
 *
 * @param self this module.
 * @param event an infection event.
 * @param zones the list of zones.
 */
void
handle_infection_event (struct spreadmodel_model_t_ *self,
                        EVT_infection_event_t * event,
                        ZON_zone_list_t *zones)
{
  local_data_t *local_data;
  const char *reason;
  ZON_zone_fragment_t *zone, *background_zone;
  GError *error = NULL;

#if DEBUG
  g_debug ("----- ENTER handle_infection_event (%s)", MODEL_NAME);
#endif

  local_data = (local_data_t *) (self->model_data);

  if (event->contact_type == SPREADMODEL_InitiallyInfected)
    reason = SPREADMODEL_contact_type_abbrev[SPREADMODEL_InitiallyInfected];
  else
    reason = "";

  zone = zones->membership[event->infected_unit->index];
  background_zone = ZON_zone_list_get_background (zones);

  /* The data fields are: run, day, type, reason, source ID, source production
   * type, source latitude, source longitude, source zone, recipient ID,
   * recipient production type, recipient latitude, recipient longitude,
   * recipient zone. */
  g_string_printf (local_data->buf,
                   "%i,%i,Infection,%s,,,,,,%s,%s,%g,%g,%s\n",
                   local_data->run_number,
                   event->day,
                   reason,
                   event->infected_unit->official_id,
                   event->infected_unit->production_type_name,
                   event->infected_unit->latitude,
                   event->infected_unit->longitude,
                   ZON_same_zone (zone, background_zone) ? "" : zone->parent->name);
  g_io_channel_write_chars (local_data->channel, local_data->buf->str, 
                            -1 /* assume null-terminated string */,
                            NULL, &error);

#if DEBUG
  g_debug ("----- EXIT handle_infection_event (%s)", MODEL_NAME);
#endif
  return;
}



/**
 * Runs this module.
 *
 * @param self this module.
 * @param units a list of units.
 * @param zones a list of zones.
 * @param event the event that caused this module to run.
 * @param rng a random number generator.
 * @param queue for any new events this module creates.
 */
void
run (struct spreadmodel_model_t_ *self, UNT_unit_list_t * units,
     ZON_zone_list_t * zones, EVT_event_t * event, RAN_gen_t * rng, EVT_event_queue_t * queue)
{
#if DEBUG
  g_debug ("----- ENTER run (%s)", MODEL_NAME);
#endif

  switch (event->type)
    {
    case EVT_OutputDirectory:
      handle_output_dir_event (self, &(event->u.output_dir));
      break;
    case EVT_BeforeAnySimulations:
      handle_before_any_simulations_event (self);
      break;
    case EVT_BeforeEachSimulation:
      handle_before_each_simulation_event (self);
      break;
    case EVT_Exposure:
      handle_exposure_event (self, &(event->u.exposure), zones);
      break;
    case EVT_Infection:
      handle_infection_event (self, &(event->u.infection), zones);
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
 * Resets this module after a simulation run.
 *
 * @param self this module.
 */
void
reset (struct spreadmodel_model_t_ *self)
{
#if DEBUG
  g_debug ("----- ENTER reset (%s)", MODEL_NAME);
#endif

  /* Nothing to do. */

#if DEBUG
  g_debug ("----- EXIT reset (%s)", MODEL_NAME);
#endif
  return;
}



/**
 * Returns a text representation of this module.
 *
 * @param self this module.
 * @return a string.
 */
char *
to_string (struct spreadmodel_model_t_ *self)
{
  local_data_t *local_data;
  GString *s;
  char *chararray;

  local_data = (local_data_t *) (self->model_data);
  s = g_string_new (NULL);
  g_string_sprintf (s, "<%s filename=\"%s\">", MODEL_NAME, local_data->filename);

  /* don't return the wrapper object */
  chararray = s->str;
  g_string_free (s, FALSE);
  return chararray;
}



/**
 * Frees this module.
 *
 * @param self this module.
 */
void
local_free (struct spreadmodel_model_t_ *self)
{
  local_data_t *local_data;
  GError *error = NULL;

#if DEBUG
  g_debug ("----- ENTER free (%s)", MODEL_NAME);
#endif

  local_data = (local_data_t *) (self->model_data);

  /* Flush and close the file. */
  if (local_data->channel_is_stdout)
    g_io_channel_flush (local_data->channel, &error);
  else
    g_io_channel_shutdown (local_data->channel, /* flush = */ TRUE, &error);

  /* Free the dynamically-allocated parts. */
  g_string_free (local_data->buf, TRUE);
  g_free (local_data->filename);
  g_free (local_data);
  g_ptr_array_free (self->outputs, TRUE);
  g_free (self);

#if DEBUG
  g_debug ("----- EXIT free (%s)", MODEL_NAME);
#endif
}



/**
 * Returns a new exposures table writer.
 */
spreadmodel_model_t *
new (sqlite3 * params, UNT_unit_list_t * units, projPJ projection,
     ZON_zone_list_t * zones)
{
  spreadmodel_model_t *self;
  local_data_t *local_data;

#if DEBUG
  g_debug ("----- ENTER new (%s)", MODEL_NAME);
#endif

  self = g_new (spreadmodel_model_t, 1);
  local_data = g_new (local_data_t, 1);

  self->name = MODEL_NAME;
  self->events_listened_for = events_listened_for;
  self->nevents_listened_for = NEVENTS_LISTENED_FOR;
  self->outputs = g_ptr_array_sized_new (0);
  self->model_data = local_data;
  self->run = run;
  self->reset = reset;
  self->is_listening_for = spreadmodel_model_is_listening_for;
  self->has_pending_actions = spreadmodel_model_answer_no;
  self->has_pending_infections = spreadmodel_model_answer_no;
  self->to_string = to_string;
  self->printf = spreadmodel_model_printf;
  self->fprintf = spreadmodel_model_fprintf;
  self->free = local_free;

  /* Get the filename for the table.  If the filename is omitted, blank, '-',
   * or 'stdout' (case insensitive), then the table is written to standard
   * output. */
  if (TRUE)
    {
      local_data->filename = g_strdup ("stdout"); /* just so we have something
        to display, and to free later */
      local_data->channel_is_stdout = TRUE;    
    }
  else
    {
      local_data->filename = NULL; /* get PAR_get_text (e); */
      if (local_data->filename == NULL
          || g_ascii_strcasecmp (local_data->filename, "") == 0
          || g_ascii_strcasecmp (local_data->filename, "-") == 0
          || g_ascii_strcasecmp (local_data->filename, "stdout") == 0)
        {
          local_data->channel_is_stdout = TRUE;
        }
      else
        {
          char *tmp;
          if (!g_str_has_suffix(local_data->filename, ".csv"))
            {
              tmp = local_data->filename;
              local_data->filename = g_strdup_printf("%s.csv", tmp);
              g_free(tmp);
            }
          tmp = local_data->filename;
          local_data->filename = spreadmodel_insert_node_number_into_filename (local_data->filename);
          g_free(tmp);
          local_data->channel_is_stdout = FALSE;
        }
    }

  local_data->buf = g_string_new (NULL);

#if DEBUG
  g_debug ("----- EXIT new (%s)", MODEL_NAME);
#endif

  return self;
}

/* end of file exposures_table_writer.c */
