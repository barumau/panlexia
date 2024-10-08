"""Map Panlexia concept ids to WOLD and NorthEuraLex ids.

Output:
- id-WOLD.tsv : maps Panlexia id to WOLD id.
- id-NELex.tsv : maps Panlexia id to NorthEuraLex id.

CC-BY 2024 Panlexia (https://github.com/barumau/panlexia)
"""
import helpers

# The input files for id mapping:
Concepticon_WOLD = 'data/Concepticon/Haspelmath-2009-1460.tsv'
NELex = 'data/Concepticon/Dellert-2017-1016.tsv'
Panlexia_to_Concepticon = 'data/id-concepticon-definition.tsv'

def get_panlexia_id(concepticon_id):
    """Get Panlexia id by Concepticon id."""
    panlexia = helpers.tsv_reader(Panlexia_to_Concepticon)
    for row in panlexia.dict:
        if row["Concepticon_id"] == concepticon_id:
            return row["id"]
    return "Undefined:?.?"

def sort_and_write_to_file(id_map, filename, header):
    """Sort the id map by Panlexia id and write TSV file with a header row."""
    sorted_map = sorted(id_map)
    id_writer = helpers.tsv_writer(filename, 'w')
    id_writer.dict.writerow(["id", header])
    for pair in sorted_map:
        id_writer.dict.writerow([pair[0], pair[1]])

def map_WOLD_ids_via_Concepticon_to_Panlexia():
    """Create file that maps Panlexia ids to WOLD ids."""
    concepticon = helpers.tsv_reader(Concepticon_WOLD)
    id_map = []

    for row in concepticon.dict:
        id = get_panlexia_id(row["CONCEPTICON_ID"])
        id_map.append((id, row["WOLD_ID"]))

    sort_and_write_to_file(id_map, 'data/id-WOLD.tsv', "WOLD_id")

def map_NELex_ids_via_Concepticon_to_Panlexia():
    """Create file that maps Panlexia ids to NorthEuraLex ids."""
    concepticon = helpers.tsv_reader(NELex)
    id_map = []

    for row in concepticon.dict:
        id = get_panlexia_id(row["CONCEPTICON_ID"])
        id_map.append((id, row["NELEX_ID"]))

    sort_and_write_to_file(id_map, 'data/id-NELex.tsv', "NELex_id")

# Execute functions
#map_WOLD_ids_via_Concepticon_to_Panlexia()
map_NELex_ids_via_Concepticon_to_Panlexia()