"""Create initial Panlexia concept ids and map them to initial sources.

1. Initial concept ids are created based on Concepticon data.
2. They are mapped to NorthEuraLex ids by Concepticon ids.
3. They are mapped to WOLD ids by IDS keys.

Output:

- eng_definition.tsv : Defines concepts in English.
- id_Concepticon.tsv : maps Panlexia id to Concepticon id.
- id_WOLD.tsv : maps Panlexia id to WOLD id.
- id_NELex.tsv : maps Panlexia id to NorthEuraLex id.

Note! The ids are not final! They will be checked and improved manually.

CC-BY 2024 Panlexia (https://github.com/barumau/panlexia)
"""
import csv
import re

# Data files for id creation and id mapping
Concepticon = '../data/Concepticon/concepticon.tsv'

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
    "The body" : "Body",
    "Emotions and values" : "Emotion",
    "The physical world" : "Nature",
    "The house" : "House",
    "Animals" : "Animalia",
    "Spatial relations" : "Space",
    "Religion and belief" : "Religion",
    "Speech and language" : "Language",
    "Time" : "Time",
    "Motion" : "Motion",
    "Law" : "Law",
    "Warfare and hunting" : "Warfare and hunting",
    "Agriculture and vegetation" : "Agriculture and vegetation",
    "Sense perception" : "Perception",
    "Cognition" : "Cognition",
    "Basic actions and technology" : "Basic actions and technology",
    "Food and drink" : "Food",
    "Social and political relations" : "Society",
    "Modern world" : "Modernity",
    "Clothing and grooming" : "Clothing and grooming",
    "Kinship" : "Kinship",
    "Miscellaneous function words" : "Grammar",
    "Possession" : "Possession",
    "Quantity" : "Quantity"
}

word_class_from = {
    "Action/Process" : "V",
    "Person/Thing" : "N",
    "Property" : "A",
    "Number" : "NUM",
    "Classifier" : "CLAS",
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
    id_writer = tsv_writer('../data/eng_definition.tsv', 'w')

    for row in concepticon.dict:
        id = build_Panlexia_id(row["SEMANTICFIELD"], row["GLOSS"], row["ONTOLOGICAL_CATEGORY"])
        id_writer.dict.writerow([id, row["ID"], row["DEFINITION"]])

# Execution begins
create_initial_concept_id_definition_map()