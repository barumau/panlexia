"""Copy final Panlexia concept ids and English definitions to a file.

Initial concept ids for Panlexia are created based on Concepticon and ULD data.

Input: master.tsv:
    Tab-separated values file for mapping initial Panlexia ids
    to Concepticon or ULD definition and other ids.

Output: eng-definition.tsv:
    Data table file with two columns: id and English definition.

CC-BY 2024 Panlexia (https://github.com/barumau/panlexia)
"""
import csv
import sys
import helpers
NorthEuraLex = 'data/NorthEuraLex/northeuralex-0.9-forms.tsv'
NELex_concepts = 'data/NorthEuraLex/northeuralex-0.9-concept-data.tsv'
master_file = 'data/master.tsv'

#NELex_to_Panlexia = 'data/NELex_id_to_Panlexia_id.tsv'

# The column headers are:
#Language_ID	Glottocode	Concept_ID	Word_Form	rawIPA	IPA	ASJP	List	Dolgo	Next_Step
#    0              1           2           3          4       5          6       7         8
Language_ID = 0
Glottocode = 1
Concept_ID = 2
Word_Form = 3
IPA = 4

def get_id_by_NELex_id(NELex_id):
    master = helpers.tsv_reader(master_file)
    for row in master.dict:
        if NELex_id == row["NELex_id"]:
            return row["id"]
    return ""

def create_NELex_id_to_Panlexia_id_map():
    NELex = helpers.tsv_reader(NELex_concepts)
    NELex_to_Panlexia = []
    for row in NELex.dict:
        id = get_id_by_NELex_id(row["id_nelex"])
        NELex_to_Panlexia.append([row["id_nelex"], id])
    return NELex_to_Panlexia

def write_dictionary_for_one_language(datalist, i, n, NELex_to_Panlexia):
    """Writes one dictionary in NELex order."""
    lang_code = datalist[i][Language_ID]
    filename = "dict/natlangs/" + lang_code + ".tsv"
    outfile = helpers.tsv_writer(filename, 'w')
    outfile.dict.writerow(["id", "num", "word", "pronunciation"])

    original_index = i
    count = 0
    j = 0
    id_sum = len(NELex_to_Panlexia)

    print(NELex_to_Panlexia[0][0], id_sum)
    last_id = ""
    num = 0

    while i < n and lang_code == datalist[i][Language_ID]:
        while j < id_sum:
            if NELex_to_Panlexia[j][0] == datalist[i][Concept_ID]:
                count = count + 1
                if NELex_to_Panlexia[j][1] != "":
                    outfile.dict.writerow([NELex_to_Panlexia[j][1], datalist[i][Word_Form], datalist[i][IPA]])
                break
            j = j + 1
        i = i + 1

    #TODO: Sort output file
    print(lang_code, " has ", count, " ready words out of ", i - original_index)
    return i

def create_dictionaries_from_NELex(NELex_to_Panlexia):
    with open(NorthEuraLex, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='\t')
        datalist = list(reader)
        row_sum = len(list(datalist))
        print(f"{row_sum} lines")
        if row_sum < 2:
            print("Not enough data")
            sys.exit()
        i = 1
        while i < row_sum:
            i = write_dictionary_for_one_language(datalist, i, row_sum, NELex_to_Panlexia)

# Execution begins:
NELex_to_Panlexia = create_NELex_id_to_Panlexia_id_map()
create_dictionaries_from_NELex(NELex_to_Panlexia)