/** @file module_util.h
 * Interface for module_util.c.
 *
 * @author Neil Harvey <nharve01@uoguelph.ca><br>
 *   School of Computer Science, University of Guelph<br>
 *   Guelph, ON N1G 2W1<br>
 *   CANADA
 * @date October 2004
 *
 * Copyright &copy; University of Guelph, 2004-2006
 * 
 * This program is free software; you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the Free
 * Software Foundation; either version 2 of the License, or (at your option)
 * any later version.
 */

#ifndef MODULE_UTIL_H
#define MODULE_UTIL_H


#include "module.h"



/* Prototypes. */
gboolean *spreadmodel_read_prodtype_attribute (const scew_element *, char *, GPtrArray *);
gboolean *spreadmodel_read_zone_attribute (const scew_element *, ZON_zone_list_t *);
void spreadmodel_extend_rotating_array (GPtrArray * array, unsigned int length, unsigned int index);
void g_queue_free_as_GDestroyNotify (gpointer data);
char *spreadmodel_insert_node_number_into_filename (const char *filename);

#endif /* !MODULE_UTIL_H */