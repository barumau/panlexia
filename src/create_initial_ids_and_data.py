"""Find match for gloss ids in WOLD and NorthEuraLex and build Panlexia id.
"""
import csv
import re

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
        "1" : "Milieu",
        "2" : "Familia",
        "3" : "Animalia",
        "4" : "Anatomia",
        "5" : "Food",
        "6" : "Clothing",
        "7" : "House",
        "8" : "Agricultura",
        "9" : "Action",
        "10" : "Motion",
        "11" : "Possession",
        "12" : "Spatial",
        "13" : "Quantity",
        "14" : "Tempus",
        "15" : "Perception",
        "16" : "Emotion",
        "17" : "Cognition",
        "18" : "Lingua",
        "19" : "Social",
        "20" : "Warfare",
        "21" : "Canon",
        "22" : "Religion",
        "23" : "Modernita",
        "24" : "Function"
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

def create_initial_dictionaries():
    """Creates initial dictionaries for Panlexia from data from WOLD and NorthEuraLex."""
    count = 0
    with open('../data/WOLD/parameters.csv', mode='r') as wold_file:
        wold_reader = csv.DictReader(wold_file, delimiter=',')

        for wold in wold_reader:
            with open('../data/NorthEuraLex/northeuralex-0.9-concept-data.tsv', mode='r') as euralex_file:
                euralex_reader = csv.DictReader(euralex_file, delimiter='\t')
                for euralex in euralex_reader:
                    if is_same_gloss(wold["Name"], euralex["gloss_en"]):
                        id = build_Panlexia_id(wold["ID"], wold["Name"], euralex["id_nelex"])
                        print(f'{wold["ID"]}\t{euralex["id_nelex"]}\t{wold["Name"]}\t{euralex["gloss_en"]}\t{id}')
                        count = count + 1

    print("Number of new ids:", count)

# Execution begins
create_initial_dictionaries()