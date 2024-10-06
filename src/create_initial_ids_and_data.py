"""Create initial Panlexia concept ids and map them to initial sources.

Initial concept ids for Panlexia are created based on Concepticon data.

Output:
- id-concepticon-definition.tsv : Intermediate file for mapping Panlexia ids
  to Concepticon ids and definitions

Note! The ids are not final! They will be checked and improved manually.

CC-BY 2024 Panlexia (https://github.com/barumau/panlexia)
"""
import csv
import re

# Data files for id creation and id mapping
Concepticon = 'data/Concepticon/concepticon.tsv'

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

simple_semantic_field_from = {
    "The physical world" : "Nature",
    "Kinship" : "Family",
    "Animals" : "Animalia",
    "The body" : "Body",
    "Food and drink" : "Gastronomy",
    "Clothing and grooming" : "Clothing/Grooming",
    "The house" : "House",
    "Agriculture and vegetation" : "Agriculture/Plantae",
    "Basic actions and technology" : "Action/Technology",
    "Motion" : "Motion",
    "Possession" : "Possession",
    "Spatial relations" : "Space",
    "Quantity" : "Quantity",
    "Time" : "Time",
    "Sense perception" : "Perception",
    "Emotions and values" : "Emotion",
    "Cognition" : "Cognition",
    "Speech and language" : "Language",
    "Social and political relations" : "Society",
    "Warfare and hunting" : "Combat/Hunting",
    "Law" : "Law",
    "Religion and belief" : "Belief",
    "Modern world" : "Modernity",
    "Miscellaneous function words" : "Grammar"
}

word_class_from = {
    "Action/Process" : "V",
    "Person/Thing" : "N",
    "Property" : "A",
    "Number" : "NUM",
    "Classifier" : "CLF",
    "Other" : "?"
}

def build_Panlexia_id(complex_semantic_field, gloss, ontological_category):
    """Builds the preliminary Panlexia id based on semantic field, gloss and word class"""
    semantic_field = simple_semantic_field_from[complex_semantic_field]
    word_class = word_class_from[ontological_category]
    id = semantic_field + ":" + gloss.lower() + "." + word_class
    print(id)
    return id

def create_initial_concept_id_definition_map():
    concepticon = csv_reader(Concepticon, '\t')
    id_writer = tsv_writer('data/id-concepticon-definition.tsv', 'w')

    for row in concepticon.dict:
        id = build_Panlexia_id(row["SEMANTICFIELD"], row["GLOSS"], row["ONTOLOGICAL_CATEGORY"])
        id_writer.dict.writerow([id, row["ID"], row["DEFINITION"]])

# Execution begins
create_initial_concept_id_definition_map()