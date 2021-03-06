from django.db.models import Q

from ScenarioCreator.models import ProductionType, DiseaseProgressionAssignment, DiseaseSpreadAssignment, Disease, Unit, DirectSpread, DiseaseProgression, \
    ControlProtocol

__author__ = 'Josiah'


def whole_scenario_validation():
    warnings = []
    total_types = ProductionType.objects.all().count()
    empty_assignments = DiseaseSpreadAssignment.objects.filter(direct_contact_spread__isnull=True, indirect_contact_spread__isnull=True,
                                                               airborne_spread__isnull=True)
    for pt in ProductionType.objects.all():
        if not DiseaseProgressionAssignment.objects.filter(production_type=pt, progression__isnull=False).count():
            warnings.append(pt.name + " has no Disease Progression assigned and so is a non-participant in the simulation.")
        if empty_assignments.filter(source_production_type=pt).count() == total_types and \
                        empty_assignments.filter(destination_production_type=pt).count() == total_types:
            warnings.append(pt.name + " is not involved in any type of disease spread. This Type is a non-participant in the simulation.")

    if not Disease.objects.get().include_direct_contact_spread:
        warnings.append("Direct Spread is not enabled in this Simulation.")
    if not Unit.objects.filter(~Q(initial_state='S')).count():
        warnings.append("There are no infected units in the Population.  Please set at least one unit to 'Latent' in the Population screen.")
    if not Disease.objects.get().use_within_unit_prevalence:
        if DirectSpread.objects.filter(infection_probability__isnull=True).count():
            warnings.append("Direct Spread: Infection Probability is required if you are not using Disease Prevalence.  Please define in: ")
            for entry in DirectSpread.objects.filter(infection_probability__isnull=True):
                warnings.append(" - - - " + entry.name)
    else:
        if DiseaseProgression.objects.filter(disease_prevalence__isnull=True).count():
            warnings.append("Disease Progression: Disease Prevalence must be defined for each progression model.  Please define in: ")
            for entry in DiseaseProgression.objects.filter(disease_prevalence__isnull=True):
                warnings.append(" - - - " + entry.name)

    #Check that an invalid tab wasn't activated
    for protocol in ControlProtocol.objects.all():
        if not protocol.is_valid():
            warnings.append(protocol.name + " Protocol has a section enabled but not completely filled in.  Either disable the section or fill in the details of the invalid section.")

    return warnings
