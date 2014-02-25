-----------------------------------------
-- outputs
-- not going to constrain outputs at all
-- schoenbaum
-- 2/24/14 - base script
-----------------------------------------

create table outdailybyproductiontype (
iteration		int,
_productiontypeid	int,
day			int,
transition_state_daily_unit_susceptible		int,
transition_state_daily_animal_susceptible	int,
transition_state_daily_unit_latent		int,
transition_state_daily_animal_latent		int,
transition_state_daily_unit_subclinical		int,
transition_state_daily_animal_subclinical	int,
transition_state_daily_unit_clinical		int,
transition_state_daily_animal_clinical		int,
transition_state_daily_unit_nat_immune		int,
transition_state_daily_animal_nat_immune	int,
transition_state_daily_unit_vac_immune		int,
transition_state_daily_animal_vac_immune	int,
transition_state_daily_unit_destroyed		int,
transition_state_daily_animal_destroyed		int,
transition_state_cum_unit_susceptible		int,
transition_state_cum_animal_susceptible		int,
transition_state_cum_unit_latent		int,
transition_state_cum_animal_latent		int,
transition_state_cum_unit_subclinical		int,
transition_state_cum_animal_subclinical		int,
transition_state_cum_unit_clinical		int,
transition_state_cum_animal_clinical		int,
transition_state_cum_unit_nat_immune		int,
transition_state_cum_animal_nat_immune		int,
transition_state_cum_unit_vac_immune		int,
transition_state_cum_animal_vac_immune		int,
transition_state_cum_unit_destroyed		int,
transition_state_cum_animal_destroyed		int,
infection_new_unit_air		int, -- infnu in xml spec  however is recombined with contact method for output field
infection_new_animal_air	int, -- infna in xml spec
infection_new_unit_dir		int,
infection_new_animal_dir	int,
infection_new_unit_ind		int,
infection_new_animal_ind	int,
infection_cum_unit_initial	int, -- infcu in xml spec
infection_cum_animal_initial	int,
infection_cum_unit_air		int, -- infcu in xml spec
infection_cum_animal_air	int,
infection_cum_unit_dir		int,
infection_cum_animal_dir	int,
infection_cum_unit_ind		int,
infection_cum_animal_ind	int,
exposed_cum_unit_dir		int,
exposed_cum_animal_dir		int,
exposed_cum_unit_ind		int,
exposed_cum_animal_ind		int,
trace_cum_unit_dir_fwd		int,
trace_cum_animal_dir_fwd	int,
trace_cum_unit_ind_fwd		int,
trace_cum_animal_ind_fwd	int,
trace_cum_unit_dir_p_fwd	int,
trace_cum_animal_dir_p_fwd	int,
trace_cum_unit_ind_p_fwd	int,
trace_cum_animal_ind_p_fwd	int,
trace_origin_cum_unit_dir_fwd	int,
trace_origin_cum_unit_ind_fwd	int,
trace_origin_cum_unit_dir_back	int,
trace_origin_cum_unit_ind_back	int,
trace_new_unit_dir_fwd		int,
trace_new_animal_dir_fwd	int,
trace_new_unit_ind_fwd		int,
trace_new_animal_ind_fwd	int,
trace_cum_unit_dir_back		int,
trace_cum_animal_dir_back	int,
trace_cum_unit_ind_back		int,
trace_cum_animal_ind_back	int,
trace_cum_unit_dir_p_back	int,
trace_cum_animal_dir_p_back	int,
trace_cum_unit_ind_p_back	int,
trace_cum_animal_ind_p_back	int,
trace_new_unit_dir_back		int,
trace_new_animal_dir_back	int,
trace_new_u_ind_back		int,
trace_new_animal_ind_back	int,
trace_origin_new_unit_dir_fwd	int,
trace_origin_new_unit_ind_fwd	int,
trace_origin_new_unit_dir_back	int,
trace_origin_new_unit_ind_back	int,
exam_cum_unit_dir_fwd		int,
exam_cum_animal_dir_fwd		int,
exam_cum_unit_ind_fwd		int,
exam_cum_animal_ind_fwd		int,
exam_cum_unit_dir_back		int,
exam_cum_animal_dir_back	int,
exam_cum_unit_ind_back		int,
exam_cum_animal_ind_back	int,
exam_new_unit_all		int,
exam_new_animal_all		int,
test_cum_unit_dir_fwd		int,
test_cum_animal_dir_fwd		int,
test_cum_unit_ind_fwd		int,
test_cum_animal_ind_fwd		int,
test_cum_unit_dir_back		int,
test_cum_animal_dir_back	int,
test_cum_unit_ind_back		int,
test_cum_animal_ind_back	int,
test_cum_unit_true_pos		int,
test_cum_animal_true_pos	int,
test_new_unit_true_pos		int,
test_new_animal_true_pos	int,
test_cum_unit_true_neg		int,
test_cum_animal_true_neg	int,
test_new_unit_true_neg		int,
test_new_animal_true_neg	int,
test_cum_unit_false_pos		int,
test_cum_animal_false_pos	int,
test_new_unit_false_pos		int,
test_new_animal_false_pos	int,
test_cum_unit_false_neg		int,
test_cum_animal_false_neg	int,
test_new_unit_false_neg		int,
test_new_animal_false_neg	int,
detect_new_unit_clin		int,
detect_new_animal_clin		int,
detect_cum_unit_clin		int,
detect_cum_animal_clin		int,
detect_new_unit_test		int,
detect_new_animal_test		int,
detect_cum_unit_test		int,
detect_cum_animal_test		int,
destroy_cum_unit_initial	int,
destroy_cum_animal_initial	int,
destroy_cum_unit_detect		int,
destroy_cum_animal_detect	int,
destroy_cum_unit_dir_fwd	int,
destroy_cum_animal_dir_fwd	int,
destroy_cum_unit_ind_fwd	int,
destroy_cum_animal_ind_fwd	int,
destroy_cum_unit_dir_back	int,
destroy_cum_animal_dir_back	int,
destroy_cum_unit_ind_back	int,
destroy_cum_animal_ind_back	int,
destroy_cum_unit_ring		int,
destroy_cum_animal_ring		int,
destroy_new_unit_all		int,
destroy_new_animal_all		int,
destroy_wait_unit_all		int,
destroy_wait_animal_all		int,
vac_cum_unit_initial		int,
vac_cum_animal_initial		int,
vac_cum_unit_ring		int,
vac_cum_animal_ring		int,
vac_new_unit_all		int,
vac_new_animal_all		int,
vac_wait_unit_all		int,
vac_wait_animal_all		int,
zone_new_foci			int,
zone_cum_foci			int
);

create table outdailybyzone (
iteration	int,
day		int,
zone_id		int,
zone_area	real,
zone_perimeter	real
);

create table outdailybyzoneandproductiontype  (
iteration		int,
day			int,
zone_id			int,
production_type_id	int,
unit_days_in_zone	int,
animal_days_in_zone	int,
units_in_zone		int,
animals_in_zone		int
);

create table outdailyevents (

iteration	int,
day		int,
event		int,
herd_id		int,
zone_id		int,  -- i think this should be zone description
event_code	text, -- i think this should be event description
new_state_code	text, -- i think this should be state description
test_result_code	text  
);

create table outdailyexposures (
iteration		int,
day			int,
exposure		int,
initiated_day		int,
exposed_herd_id		int,
exposed_zone_id		int,
exposing_herd_id	int,
exposing_zone_id	int,
spread_method_code	text,
is_adequate		int,
exposing_herd_status_code	text,
exposed_herd_status_code	text
);

create table outepidemiccurves (
iteration			int,
day				int,
production_type_id		int,
infected_units			int,
infected_animals		int,
detected_units			int,
detected_animals		int,
infectious_units		int,
apparent_infectious_units	int
);

create table outgeneral (
out_general_id		text, -- yuck is this that versionapplication thing
simulation_start_time	text,
simulation_end_time	text,  -- really, why don't we just calculate a run time, isn't that what shows up?
completed_iterations	int,
version			text
);

create table outiteration (
iteration		int,
disease_ended		int,
disease_end_day		int,
outbreak_ended		int,
outbreak_end_day	int,
zone_foci_created	int,
destroy_wait_unit_max	int,
destroy_wait_unit_max_day	int,
destroy_wait_animal_max		real,
destroy_wait_animal_max_day	int,
destroy_wait_unit_time_max	int,
destroy_wait_unit_time_avg	real,
vac_wait_unit_max		int,
vac_wait_unit_max_day	int,
vac_wait_animal_max	real,
vac_wait_animal_max_day	int,
vac_wait_unit_time_max	int,
vac_wait_unit_time_avg	real
);


create table outiterationbyherd (
iteration		int,
herd_id			int,
last_status_code	text,  -- why not put the descriptions in here instead since we are writing it?
last_status_day		int,
last_control_state_code	text,	-- why not put the descriptions in here since we are writing it?
last_control_state_day	int
);



create table outiterationbyproductiontype (

iteration		int,
production_type_id	int,
transition_state_cum_unit_susceptible	int,
transition_state_cum_animal_susceptible	int,
transition_state_cum_unit_latent	int,
transition_state_cum_animal_latent	int,
transition_state_cum_unit_subclinical	int,
transition_state_cum_animal_subclinical	int,
transition_state_cum_unit_clinical	int,
transition_state_cum_animal_clinical	int,
transition_state_cum_unit_nat_immune	int,
transition_state_cum_animal_nat_immune	int,
transition_state_cum_unit_vac_immune	int,
transition_state_cum_animal_vac_immune	int,
transition_state_cum_unit_destroyed	int,
transition_state_cum_animal_destroyed	int,
infection_cum_unit_initial		int,
infection_cum_animal_initial	int,
infection_cum_unit_air		int,
infection_cum_animal_air	int,
infection_cum_unit_dir		int,
infection_cum_animal_dir	int,
infection_cum_unit_ind		int,
infection_cum_animal_ind	int,
exposed_cum_unit_dir		int,
exposed_cum_animal_dir		int,
exposed_cum_unit_ind		int,
exposed_cum_animal_ind		int,
trace_cum_unit_dir_fwd		int,
trace_cum_animal_dir_fwd	int,
trace_cum_unit_ind_fwd		int,
trace_cum_animal_ind_fwd	int,
trace_cum_unit_dir_p_fwd	int,
trace_cum_animal_dir_pfwd	int,
trace_cum_unit_ind_p_fwd	int,
trace_cum_animal_ind_p_fwd	int,
trace_cum_unit_dir_back		int,
trace_cum_animal_dir_back	int,
trace_cum_unit_ind_back		int,
trace_cum_animal_ind_back	int,
trace_cum_unit_dir_p_back	int,
trace_cum_animal_dir_pback	int,
trace_cum_unit_ind_p_back	int,
trace_cum_animal_ind_p_back	int,
trace_origin_cum_unit_dir_fwd	int,
trace_origin_cum_unit_ind_fwd	int,
trace_origin_cum_unit_dir_back	int,
trace_origin_cum_unit_ind_back	int,
exam_cum_unit_dir_fwd		int,
exam_cum_animal_dir_fwd		int,
exam_cum_unit_ind_fwd		int,
exam_cum_animal_ind_fwd		int,
exam_cum_unit_dir_back		int,
exam_cum_animal_dir_back	int,
exam_cum_unit_ind_back		int,
exam_cum_animal_ind_back	int,
test_cum_unit_dir_fwd		int,
test_cum_animal_dir_fwd		int,
test_cum_unit_ind_fwd		int,
test_cum_animal_ind_fwd		int,
test_cum_unit_dir_back		int,
test_cum_animal_dir_back	int,
test_cum_unit_ind_back		int,
test_cum_animal_ind_back	int,
test_cum_unit_true_pos		int,
test_cum_animal_true_pos	int,
test_cum_unit_true_neg		int,
test_cum_animal_true_neg	int,
test_cum_unit_false_pos		int,
test_cum_animal_false_pos	int,
test_cum_unit_false_neg		int,
test_cum_animal_false_neg	int,
detect_cum_unit_clin		int,
detect_cum_animal_clin		int,
detect_cum_unit_test		int,
detect_cum_animal_test		int,
destroy_cum_unit_initial	int,
destroy_cum_animal_initial	int,
destroy_cum_unit_detect		int,
destroy_cum_animal_detect	int,
destroy_cum_unit_dir_fwd	int,
destroy_cum_animal_dir_fwd	int,
destroy_cum_unit_ind_fwd	int,
destroy_cum_animal_ind_fwd	int,
destroy_cum_unit_dir_back	int,
destroy_cum_animal_dir_back	int,
destroy_cum_unit_ind_back	int,
destroy_cum_animal_ind_back	int,
destroy_cum_unit_ring		int,
destroy_cum_animal_ring		int,
destroy_wait_unit_max		int,
destroy_wait_animal_max		real
destroy_wait_unit_max_day	int,
destroy_wait_animal_max_day	int,
destroy_wait_unit_time_max	int,
destroy_wait_unit_time_avg	real
destroy_wait_unit_days_in_queue	real
destroy_wait_animal_days_in_queue	real
vac_cum_unit_initial		int,
vac_cum_animal_initial		int,
vac_cum_unit_ring		int,
vac_cum_animal_ring		int, --
vac_wait_unit_max		int,
vac_wait_animal_max		real  -- 
vac_wait_unit_max_day		int,
vac_wait_animal_max_day		int,
vac_wait_unit_time_max		real
vac_wait_unit_time_avg		int,
zonc_foci			int,
first_detection			int,
first_det_unit_inf		int,
first_detect_animal_inf		int,
first_destruction		int,
first_vaccination		int,
last_detection			int
);

create table outiterationbyzone (
iteration		int,
zone_id			int,
max_zone_area		real,
max_zone_area_day	int,
final_zone_area		real,
max_zone_perimeter	real,
max_zone_perimeter_day	int,
final_zone_perimeter	real
);

create table outiterationbyzoneandproductiontype (
iteration		int,
zone_id			int,
production_type_id	int,
unit_days_in_zone	int,
animal_days_in_zone	int,
cost_surveillance	real
);

create table outiterationcosts (
iteration		int,
production_type_id	int,
destroy_appraisal	real,
destroy_cleaning	real,
destroy_euthanasia	real,
destroy_indemnification	real,
destroy_disposal	real,
vac_cum_setup		real,
vac_cum_vaccination	real
);






