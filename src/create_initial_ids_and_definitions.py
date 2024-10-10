"""Create initial Panlexia concept ids and map them to initial sources.

Initial concept ids for Panlexia are created based on Concepticon data.

Output:
- id-concepticon-definition.tsv : Intermediate file for mapping Panlexia ids
  to Concepticon ids and definitions

Note! The ids are not final! They will be checked and improved manually.

CC-BY 2024 Panlexia (https://github.com/barumau/panlexia)
"""
import helpers
import re

# Data files for id creation and id mapping
Concepticon = 'data/Concepticon/concepticon.tsv'

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
    concepticon = helpers.csv_reader(Concepticon, '\t')
    id_writer = helpers.tsv_writer('data/id-concepticon-definition.tsv', 'w')
    id_writer.dict.writerow(["id", "Concepticon_id", "Definition"])

    for row in concepticon.dict:
        id = build_Panlexia_id(row["SEMANTICFIELD"], row["GLOSS"], row["ONTOLOGICAL_CATEGORY"])
        id_writer.dict.writerow([id, row["ID"], row["DEFINITION"]])

def create_id_and_definition_files():
    """Writes id-concepticon.tsv and eng-definition.tsv files"""

    id_writer = helpers.tsv_writer('data/id-concepticon.tsv', 'w')
    id_writer.dict.writerow(["id", "Concepticon_id"])

    definition_writer = helpers.tsv_writer('dict/eng-definition.tsv', 'w')
    definition_writer.dict.writerow(["id", "Definition"])

    combined = helpers.tsv_reader('data/id-concepticon-definition.tsv')
    for row in combined.dict:
        if row["Id_status"] == "ready":
            id_writer.dict.writerow([row["id"], row["Concepticon_id"]])
            definition_writer.dict.writerow([row["id"], row["Definition"]])

def add_to_id_and_definition_files():
    """Appends new ids to id-concepticon.tsv and eng-definition.tsv files"""

    id_writer = helpers.tsv_writer('data/id-concepticon.tsv', 'a')
    definition_writer = helpers.tsv_writer('dict/eng-definition.tsv', 'a')

    combined = helpers.tsv_reader('data/id-concepticon-definition.tsv')
    for row in combined.dict:
        if row["Id_status"] == "ready":
            id_writer.dict.writerow([row["id"], row["Concepticon_id"]])
            definition_writer.dict.writerow([row["id"], row["Definition"]])


# Execution begins
#create_initial_concept_id_definition_map()
#create_id_and_definition_files()
add_to_id_and_definition_files()