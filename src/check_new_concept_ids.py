"""Create new Panlexia concept id based on Wordnet name from temporary id.

For example, the temporary id 'TMP:09786585.n' produces the proper Panlexia concept id 'PWN:amateur.n.01'.

CC-BY 2025 Panlexia (https://github.com/barumau/panlexia)
"""

import helpers
from nltk.corpus import wordnet as wn

def create_and_print_new_id(temporary_id, separator):
    '''Creates new Panlexia concept id from a temporary id.'''
    offset = int(temporary_id.split(separator)[0])
    pos = temporary_id.split(separator)[1]
    synset = wn.synset_from_pos_and_offset(pos, offset)
    if synset is not None:
        new_id = "PWN:" + synset.name()
        print(f"TMP:{temporary_id}, {new_id}, {synset.definition()}")
    else:
        print("No Wordnet synset found for TMP:", temporary_id)

def find_and_rename_temporary_ids():
    '''Finds temporary concept ids to be renamed as normalized Panlexia concept ids.'''
    id_map = helpers.tsv_reader('data/id_map.tsv')
    for row in id_map.dict:
        id = row["id"].strip()
        prefix = id.split(':')[0]
        if prefix == 'TMP':
            rest = id.split(':')[1]
            if '.' in rest:
                create_and_print_new_id(rest, '.')
            elif '-' in rest:
                create_and_print_new_id(rest, '-')
            else:
                print("Malformed temporary id:", id)

find_and_rename_temporary_ids()
