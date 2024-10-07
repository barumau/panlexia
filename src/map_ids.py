"""Map Panlexia concept ids to WOLD and NorthEuraLex ids.

Output:
- id-WOLD.tsv : maps Panlexia id to WOLD id.
- id-NELex.tsv : maps Panlexia id to NorthEuraLex id.

CC-BY 2024 Panlexia (https://github.com/barumau/panlexia)
"""
import re
import helpers

# Data files for id creation and id mapping
Concepticon = 'data/Concepticon/concepticon.tsv'
Concepticon_IDS = 'data/Concepticon/List-2020-1365.tsv'
Concepticon_WOLD = 'data/Concepticon/Haspelmath-2009-1460.tsv'
Panlexia_to_Concepticon = 'data/id-concepticon-definition.tsv'
WOLD = '../data/WOLD/parameters.csv'
NELex = 'data/NorthEuraLex/northeuralex-0.9-concept-data.tsv'

def get_panlexia_id(concepticon_id):
    panlexia = helpers.tsv_reader(Panlexia_to_Concepticon)
    for row in panlexia.dict:
        if row["Concepticon_id"] == concepticon_id:
            return row["id"]
    return "Undefined:?.?"

def sort_and_write_to_file(id_map, filename, header):
    sorted_map = sorted(id_map)
    id_writer = helpers.tsv_writer(filename, 'w')
    id_writer.dict.writerow(["id", header])
    for pair in sorted_map:
        id_writer.dict.writerow([pair[0], pair[1]])

def map_WOLD_ids_via_Concepticon_to_Panlexia():
    concepticon = helpers.tsv_reader(Concepticon_WOLD)
    id_map = []

    for row in concepticon.dict:
        id = get_panlexia_id(row["CONCEPTICON_ID"])
        id_map.append((id, row["WOLD_ID"]))

    sort_and_write_to_file(id_map, 'data/id-WOLD.tsv', "WOLD_id")

def map_NELex_ids_via_Concepticon_to_Panlexia():
    concepticon = helpers.tsv_reader(NELex)
    id_map = []

    for row in concepticon.dict:
        id = get_panlexia_id(row["concepticon_id"])
        id_map.append((id, row["id_nelex"]))

    sort_and_write_to_file(id_map, 'data/id-NELex.tsv', "NELex_id")

# Execute functions
map_WOLD_ids_via_Concepticon_to_Panlexia()
map_NELex_ids_via_Concepticon_to_Panlexia()