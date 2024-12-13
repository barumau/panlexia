"""Create initial Panlexia concept ids and map them to initial sources.

Initial concept ids for Panlexia are created based on Concepticon and ULD data.

Output:
- master.tsv : Tab-separated values file for mapping initial Panlexia ids
  to Concepticon or ULD definition and other ids.

Note! This script is run only once in the beginning of this project.
The initial_ids that it creates are not final. They will be validated and adjusted manually.


CC-BY 2024 Panlexia (https://github.com/barumau/panlexia)
"""
import helpers

# Data files for id creation and id mapping
Concepticon = 'data/Concepticon/concepticon.tsv'
Concepticon_WOLD = 'data/Concepticon/Haspelmath-2009-1460.tsv'
NorthEuraLex = 'data/Concepticon/Dellert-2017-1016.tsv'
ULD_file = 'data/ULD/ULD.tsv'
Borin = 'data/Concepticon/Borin-2015-1532.tsv'
master_file = 'data/master.tsv'

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

def build_Panlexia_id(semantic_field, gloss, word_class):
    """Builds the preliminary Panlexia id based on semantic field, gloss and word class"""
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
        word_class = word_class_from[row["ONTOLOGICAL_CATEGORY"]]
        semantic_field = simple_semantic_field_from[row["SEMANTICFIELD"]]
        id = build_Panlexia_id(semantic_field, row["GLOSS"], word_class)
        WOLD_id = get_WOLD_id_by_Concepticon_id(row["ID"])
        NELex_id = get_NELex_id_by_Concepticon_id(row["ID"])
        # Saves the following data:
        # Initial_id | Definition | Concepticon_id | WOLD_id | NELex_id | ULD_id
        id_map.append([id, row["DEFINITION"], row["ID"], WOLD_id, NELex_id, ""])

def get_gloss(description):
    """Retuns substring before first occurence of ',' '(' or '['."""
    return description.replace(" (", ",").replace(" [", ",").split(',')[0]

uld_word_class = {
    "aj" : "A",
    "aj/av" : "A",
    "aj/pn" : "PRN",
    "aj/pfx" : "A",
    "aux v" : "V",
    "av" : "ADV",
    "cj" : "CNJ",
    "num" : "NUM",
    "pn" : "PRN",
    "pr" : "ADP",
    "pr/cj" : "ADP",
    "v" : "V",
    "vi" : "V",
    "vt" : "V"
}

def get_word_class(description):
    """Returns word class based on ULD word class."""
    # Get substring between square brackets, like [v], [aux v], [aj] or [pr].
    if "[" in description:
        # initializing substrings
        sub1 = "["
        sub2 = "]"
        
        # getting index of substrings
        idx1 = description.index(sub1)
        idx2 = description.index(sub2)
        
        res = ''
        # getting elements in between
        for idx in range(idx1 + len(sub1), idx2):
            res = res + description[idx]

        if res in uld_word_class:
            return uld_word_class[res]
        else:
            print(res)

    return "N"

def get_definition(description):
    """Retuns substring before '['."""
    return description.split('[')[0]

def create_initial_concept_ids_from_ULD(id_map):
    """ Creates initial Panlexia id and maps it to ULD definition and id."""
    uld = helpers.csv_reader(ULD_file, '\t')
    for row in uld.dict:
        if row["number"] != "":
            gloss = get_gloss(row["English"])
            word_class = get_word_class(row["English"])
            definition = get_definition(row["English"])
            id = build_Panlexia_id(row["category"], gloss, word_class)
            # Saves the following data:
            # Initial_id | Definition | Concepticon_id | WOLD_id | NELex_id | ULD_id
            id_map.append([id, definition, "", "", "", row["number"]])

def sort_and_write_to_file(id_map, filename):
    """Sort the id map by Panlexia id and write TSV file with a header row."""
    sorted_map = sorted(id_map)
    id_writer = helpers.tsv_writer(filename, 'w')
    id_writer.dict.writerow(["id", "initial_id", "Definition", "Concepticon_id", "WOLD_id", "NELex_id", "ULD_id"])
    for row in sorted_map:
        id_writer.dict.writerow(["", row[0], row[1], row[2], row[3], row[4], row[5]])

def get_PWN_id_by_Concepticon_id(concepticon_id):
    """Finds and returns Princeton WordNet offset and PoS by Concepticon id or empty if not found."""
    concepticon = helpers.tsv_reader(Borin)

    for row in concepticon.dict:
        if row["CONCEPTICON_ID"] == concepticon_id:
            offset = row["PWN_SYNSET"].replace('n', '').replace('a', '').replace('v', '').replace('r', '')
            offset_and_pos = offset + "\t" + row["PWN_POS"]
            return offset_and_pos

    return ""

def map_Concepticon_ids_to_PWN_synset_ids():
    """Prints mapping of Concepticon ids to WordNet offset and PoS."""
    master = helpers.tsv_reader(master_file)
    i = 0
    for row in master.dict:
        concepticon_id = row["Concepticon_id"]
        if concepticon_id != "":
            pwn_id = get_WN_id_by_Concepticon_id(concepticon_id)
            print(f"{concepticon_id}\t{pwn_id}")
            if pwn_id != "":
                i = i + 1
        else:
            print("\t\t\t")
    print("Mapped ", i, " ids to PWN.")

# Execution begins
id_map = []
create_initial_concept_id_definition_map(id_map)
create_initial_concept_ids_from_ULD(id_map)
sort_and_write_to_file(id_map, master_file)
