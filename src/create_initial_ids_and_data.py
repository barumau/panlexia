"""Create initial Panlexia concept ids from data from WOLD and NorthEuraLex.

Initial concept ids are created based on 3 kinds of data:
1. WOLD and NorthEuraLex
2. Only WOLD
3. Only NorthEuraLex

Creates also a table that maps Panlexia ids to those of WOLD and NorthEuraLex.

Note! The ids are not final! They will be checked and improved manually.

CC-BY 2024 Panlexia (https://github.com/barumau/panlexia)
"""
import csv
import re

class csv_reader:
    """Helper for opening and closing a CSV or TSV file for reading."""
    def __init__(self, file_name, delimiter):
        self.file = open(file_name, 'r')
        self.dict = csv.DictReader(self.file, delimiter=delimiter)

    def __del__(self):
        self.file.close()

class tsv_writer:
    """Helper for opening and closing a TSV file for writing."""
    def __init__(self, file_name, open_mode):
        self.file = open(file_name, open_mode)
        self.dict = csv.writer(self.file, delimiter='\t')

    def __del__(self):
        self.file.close()

def strip_gloss(gloss):
    """Strip initial 'to ' and 'the ' from a WOLD-style gloss."""
    return re.sub('(^to |^the )', '', gloss)

def is_same_gloss(wold_gloss, ne_gloss):
    """Compare glosses and return true if they match."""
    if strip_gloss(wold_gloss) == ne_gloss:
        return True
    return False

def convert_semantic_field_number_to_label(wold_id):
    number_to_label_map = {
        "1" : "Natura",
        "2" : "Familia",
        "3" : "Animalia",
        "4" : "Anatomia",
        "5" : "Gastronomia",
        "6" : "Vestitura",
        "7" : "Domestica",
        "8" : "Agricultura",
        "9" : "Action",
        "10" : "Motion",
        "11" : "Possession",
        "12" : "Spatium",
        "13" : "Quantita",
        "14" : "Tempus",
        "15" : "Perception",
        "16" : "Emotion",
        "17" : "Cognition",
        "18" : "Lingua",
        "19" : "Societa",
        "20" : "Militia",
        "21" : "Jus",
        "22" : "Religion",
        "23" : "Modernita",
        "24" : "Function",
        "25" : "Alia"
    }
    # Trim an id, like '1-215', by deleting '-' and everything after it,
    # so that only the number for the semantic field remains.
    semantic_field = re.sub('-.*$', '', wold_id)
    # Convert to the the label of the semantic field and return it.
    return number_to_label_map[semantic_field]

def build_Panlexia_id(wold_id, wold_gloss, ne_id):
    """Builds the preliminary Panlexia id based on WOLD id and gloss and NorthEuraLex word class"""
    field = convert_semantic_field_number_to_label(wold_id)
    new_id = field + ":" + strip_gloss(wold_gloss) + "." + re.sub('^.*::', '', ne_id)
    return new_id

def create_concept_ids_from_WOLD(euralex_ids):
    """Creates initial concept ids for Panlexia from data in WOLD and NorthEuraLex and only WOLD."""
    wold_count = 0
    wold_ne_count = 0
    wold_reader = csv_reader('../data/WOLD/parameters.csv', ',')
    id_writer = tsv_writer('../data/id_map.tsv', 'w')

    for wold in wold_reader.dict:
        has_match = False
        euralex_reader = csv_reader('../data/NorthEuraLex/northeuralex-0.9-concept-data.tsv', '\t')
        for euralex in euralex_reader.dict:
            if is_same_gloss(wold["Name"], euralex["gloss_en"]):
                # Create concept id from both WOLD and NorthEuraLex data.
                id = build_Panlexia_id(wold["ID"], wold["Name"], euralex["id_nelex"])
                id_writer.dict.writerow([id, wold["ID"], euralex["id_nelex"], wold["Description"]])
                euralex_ids.append(euralex["id_nelex"])
                wold_ne_count = wold_ne_count + 1
                has_match = True
                #print(f'Is match:\t{id}\t{wold["ID"]}\t{wold["Name"]}\t{euralex["id_nelex"]}\t{euralex["gloss_en"]}')

        if has_match == False:
            # Create concept id from only WOLD data.
            word_class = "?"
            if wold["Name"].find("the ") != -1:
                word_class = "N"
            elif wold["Name"].find("to ") != -1:
                word_class = "V"
            id = build_Panlexia_id(wold["ID"], wold["Name"], word_class)
            id_writer.dict.writerow([id, wold["ID"], "", wold["Description"]])
            wold_count = wold_count + 1
            #print(f'No match:\t{id}\t{wold["ID"]}\t{wold["Name"]}')

    print("Number of ids based on WOLD & NorthEuraLex:", wold_ne_count)
    print("Number of ids based on WOLD only:", wold_count)

def create_concept_ids_from_NorthEuraLex(euralex_ids):
    """Creates concept ids for those entries from NorthEuraLex that are not covered by WOLD."""
    id_writer = tsv_writer('../data/id_map.tsv', 'a')
    euralex_reader = csv_reader('../data/NorthEuraLex/northeuralex-0.9-concept-data.tsv', '\t')
    count = 0
    for euralex in euralex_reader.dict:
        if euralex["id_nelex"] not in euralex_ids:
            id = build_Panlexia_id("25", euralex["gloss_en"], euralex["id_nelex"])
            id_writer.dict.writerow([id, "", euralex["id_nelex"], euralex["annotation_en"]])
            count = count + 1
    print("Number of ids based on NorthEuraLex only:", count)

# Execution begins
euralex_ids = []
create_concept_ids_from_WOLD(euralex_ids)
create_concept_ids_from_NorthEuraLex(euralex_ids)
