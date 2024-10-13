"""Create initial Panlexia concept ids and map them to initial sources.

Initial concept ids for Panlexia are created based on Concepticon and ULD data.

Output:
- main.tsv : Tas separated values file for mapping initial Panlexia ids
  to Concepticon definition and other ids.

Note! The initial_ids are not final! They will be checked and improved manually.

CC-BY 2024 Panlexia (https://github.com/barumau/panlexia)
"""
import helpers

# Data files for id creation and id mapping
Concepticon = 'data/Concepticon/concepticon.tsv'
Concepticon_WOLD = 'data/Concepticon/Haspelmath-2009-1460.tsv'
NorthEuraLex = 'data/Concepticon/Dellert-2017-1016.tsv'

simple_semantic_field_from = {
    "The physical world" : "Nature",
    "Kinship" : "Family",
    "Animals" : "Animal",
    "The body" : "Body",
    "Food and drink" : "Food",
    "Clothing and grooming" : "Clothing/Grooming",
    "The house" : "House",
    "Agriculture and vegetation" : "Agriculture/Plant",
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
    #print(id)
    return id

def get_WOLD_id_by_Concepticon_id(concepticon_id):
    """Finds and returns WOLD id by Concepticon id or empty if not found."""
    wold = helpers.tsv_reader(Concepticon_WOLD)

    for row in wold.dict:
        if row["CONCEPTICON_ID"] == concepticon_id:
            return row["WOLD_ID"]

    return ""

def get_NELex_id_by_Concepticon_id(concepticon_id):
    """Finds and returns NELex id by Concepticon id or empty if not found."""
    NELex = helpers.tsv_reader(NorthEuraLex)

    for row in NELex.dict:
        if row["CONCEPTICON_ID"] == concepticon_id:
            return row["NELEX_ID"]

    return ""

def create_initial_concept_id_definition_map(id_map):
    """ Creates initial Panlexia id and maps it to definition and other ids."""
    concepticon = helpers.csv_reader(Concepticon, '\t')

    for row in concepticon.dict:
        id = build_Panlexia_id(row["SEMANTICFIELD"], row["GLOSS"], row["ONTOLOGICAL_CATEGORY"])
        WOLD_id = get_WOLD_id_by_Concepticon_id(row["ID"])
        NELex_id = get_NELex_id_by_Concepticon_id(row["ID"])
        # Saves the following data:
        # Initial_id | Definition | Concepticon_id | WOLD_id | NELex_id
        id_map.append([id, row["DEFINITION"], row["ID"], WOLD_id, NELex_id])

def sort_and_write_to_file(id_map, filename):
    """Sort the id map by Panlexia id and write TSV file with a header row."""
    sorted_map = sorted(id_map)
    id_writer = helpers.tsv_writer(filename, 'w')
    id_writer.dict.writerow(["id", "initial_id", "Definition", "Concepticon_id", "WOLD_id", "NELex_id"])
    for row in sorted_map:
        id_writer.dict.writerow(["", row[0], row[1], row[2], row[3], row[4]])

# Execution begins
id_map = []
create_initial_concept_id_definition_map(id_map)
sort_and_write_to_file(id_map, "data/main.tsv")
