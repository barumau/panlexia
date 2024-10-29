"""Write language-specific dictionaries with Panlexia concept ids from NorthEuraLex data.

CC-BY 2024 Panlexia (https://github.com/barumau/panlexia)
"""
import csv
import os
import sys
import helpers
from string import ascii_uppercase

master_file = 'data/master.tsv'
NorthEuraLex = 'data/NorthEuraLex/northeuralex-0.9-forms.tsv'
NELex_concepts = 'data/NorthEuraLex/northeuralex-0.9-concept-data.tsv'
# The column headers in NELex_concepts file are:
#Language_ID	Glottocode	Concept_ID	Word_Form	rawIPA	IPA	ASJP	List	Dolgo	Next_Step
#    0              1           2           3          4       5          6       7         8
Language_ID = 0
Glottocode = 1
Concept_ID = 2
Word_Form = 3
IPA = 4

def create_directory(directory_name):
    """Creates a given directory."""
    try:
        os.mkdir(directory_name)
        print(f"Directory '{directory_name}' created successfully.")
    except FileExistsError:
        print(f"Directory '{directory_name}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{directory_name}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

def create_directories():
    """Creates alphabetical directories inside dict/."""
    for initial_letter in ascii_uppercase:
        directory_name = "dict/" + initial_letter
        create_directory(directory_name)

def get_id_by_NELex_id(NELex_id):
    """Returns the corresponding Panlexia concept id to a NELex id."""
    master = helpers.tsv_reader(master_file)
    for row in master.dict:
        if NELex_id == row["NELex_id"]:
            return row["id"]
    return ""

def create_NELex_id_to_Panlexia_id_map():
    """Creates a map of NELex to Panlexia ids in the standard NELex order."""
    NELex = helpers.tsv_reader(NELex_concepts)
    NELex_to_Panlexia = []
    for row in NELex.dict:
        id = get_id_by_NELex_id(row["id_nelex"])
        NELex_to_Panlexia.append([row["id_nelex"], id])
    return NELex_to_Panlexia

def sort_and_write_to_dictionary_file(lang_code, data):
    """Sort the id map by Panlexia id and write TSV file with a header row."""
    sorted_map = sorted(data)

    filename = "dict/" + lang_code[0].upper() + "/" + lang_code + ".tsv"
    outfile = helpers.tsv_writer(filename, 'w')
    outfile.dict.writerow(["id", "style", "word", "pronunciation"])

    for row in sorted_map:
        outfile.dict.writerow([row[0], "", row[1], row[2]])


def write_dictionary_for_one_language(datalist, i, n, NELex_to_Panlexia):
    """Writes dictionary for one language ordered by Panlexia id."""
    lang_code = datalist[i][Language_ID]
    original_index = i
    count = 0
    id_index = 0
    id_sum = len(NELex_to_Panlexia)

    dictionary = []

    # Iterate over all rows that have the same Language_ID.
    while i < n and lang_code == datalist[i][Language_ID]:
        # Iterate over NELex ids in the standard NELex order.
        while id_index < id_sum:
            NELex_id = datalist[i][Concept_ID]
            if NELex_to_Panlexia[id_index][0] == NELex_id:
                # Write only those words that have a Panlexia id.
                if NELex_to_Panlexia[id_index][1] != "":
                    count = count + 1
                    dictionary.append([NELex_to_Panlexia[id_index][1], datalist[i][Word_Form], datalist[i][IPA]])
                break
            id_index = id_index + 1
        i = i + 1

    sort_and_write_to_dictionary_file(lang_code, dictionary)
    print(lang_code, "has", count, "words with Panlexia id out of total", i - original_index)
    return i

def create_dictionaries_from_NELex(NELex_to_Panlexia):
    with open(NorthEuraLex, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        datalist = list(reader)
        data_size = len(list(datalist))
        print(f"{data_size} lines")
        if data_size < 2:
            print("Not enough data")
            sys.exit()
        i = 1
        while i < data_size:
            i = write_dictionary_for_one_language(datalist, i, data_size, NELex_to_Panlexia)

# Execution begins:
#create_directories() # Done only once
NELex_to_Panlexia = create_NELex_id_to_Panlexia_id_map()
create_dictionaries_from_NELex(NELex_to_Panlexia)