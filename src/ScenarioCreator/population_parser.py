import csv
import itertools
import os
import xml.etree.ElementTree as ET


def gettext(elem):
    return ",".join(elem.itertext())


def lowercase_header(iterator):
    """Source: http://stackoverflow.com/questions/16937457/python-dictreader-how-to-make-csv-column-names-lowercase"""
    return itertools.chain([next(iterator).lower()], iterator)


class PopulationParser(object):
    model_labels = ['user_notes', 'production_type', 'latitude', 'longitude', 'initial_state', 'initial_size']
    xml_fields   = ['id',             'production-type', 'latitude', 'longitude', 'status',        'size']
    text_fields = list(zip(model_labels, xml_fields))

    def __init__(self, filename):
        if not os.path.isfile(filename):
            raise OSError("'" + filename + "' is not a file.")

        if not os.path.getsize(filename):
            raise EOFError("File Read returned a blank string.")

        self.population = []
        self.filename = filename
        self.is_xml = '.xml' in filename
        if self.is_xml:
            tree = ET.ElementTree(file=filename)
            self.top_level = tree.getroot()
        else:  #csv
            self.__parse_csv(filename)

    def parse_to_dictionary(self):
        if self.is_xml:
            self.__parse_xml_population_fields(self.text_fields)
        else:
            pass  # csv parsing already done
        return self.population

    def __parse_csv_units(self, filename, mapping):
        with open(filename) as csvfile:
            reader = csv.DictReader(lowercase_header(csvfile))
            for unit in reader:
                entry = {store_key: unit[header] for header, store_key in mapping.items()}
                # preserve the information from any colulmns I didn't use
                entry['user_notes'] = ', '.join(["%s=%s" % (key, value) for key, value in unit.items() if key not in mapping])
                self.population.append(entry)

    def __parse_csv(self, filename):
        """Based on FLAPS example, and a NAADSM csv example"""
        try:
            try:
                mapping = {'productiontype': 'production_type',  # FLAPS Preferred Mapping
                           'longitude': 'longitude',
                           'latitude': 'latitude',
                           'population': 'initial_size', }
                self.__parse_csv_units(filename, mapping)
            except KeyError:
                mapping = {'commoditytype': 'production_type',  # FLAPS Fallback Mapping
                           'longitude': 'longitude',
                           'latitude': 'latitude',
                           'population': 'initial_size', }
                self.__parse_csv_units(filename, mapping)
        except KeyError:
            mapping = {'production-type': 'production_type',  # NAADSM CSV mapping
                       'longitude': 'longitude',
                       'latitude': 'latitude',
                       'size': 'initial_size',
                       'status': 'initial_state'}
            try:
                self.__parse_csv_units(filename, mapping)
            except KeyError:
                raise ET.ParseError("Unrecognized csv header format. Please use: " + ', '.join(list(mapping.keys())))


    def __parse_xml_population_fields(self, text_fields):
        for herd in self.top_level.iter('herd'):
            self.population.append( dict() ) #empty
            for t in text_fields:
                if isinstance(t, tuple):
                    self.__populate_xml_text_field(herd, *t)
                else:
                    self.__populate_xml_text_field(herd, t)

    def __populate_xml_text_field(self, herd, field_name, xml_name=''):
        if not xml_name:
            xml_name = field_name
        try:
            element = next(herd.iter(xml_name))
            text = gettext(element)
        except:
            raise IOError("Couldn't find '%s' label in xml" % xml_name)
        self.population[-1][field_name] = text