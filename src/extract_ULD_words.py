"""Write language-specific dictionaries with Panlexia concept ids from ULD data.

CC-BY 2024 Panlexia (https://github.com/barumau/panlexia)
"""
import helpers

ULD_file = 'data/ULD/ULD.tsv'

def sort_and_write_to_dictionary_file(lang_name, data):
    """Sort the id map by Panlexia id and write TSV file with a header row."""
    sorted_map = sorted(data)

    filename = "dict/" + lang_name[0].upper() + "/" + lang_name.lower() + ".tsv"
    outfile = helpers.tsv_writer(filename, 'w')
    outfile.dict.writerow(["id", "word"])

    for row in sorted_map:
        outfile.dict.writerow([row[0], row[1]])

def write_dictionary_for_one_language(lang_code, ULD_to_Panlexia):
    """Writes dictionary for one language ordered by Panlexia id."""
    dictionary = []
    uld = helpers.tsv_reader(ULD_file)
    for row in uld.dict:
        id = ULD_to_Panlexia[row["number"]]
        word = row[lang_code]
        if id != "" and word != "":
            dictionary.append([id, word])
    sort_and_write_to_dictionary_file(lang_code, dictionary)

def create_dictionaries_from_ULD(ULD_to_Panlexia):
    langs = ["Esperanto", "Novial", "Lidepla", "Sambahsa"]
    for lang in langs:
        write_dictionary_for_one_language(lang, ULD_to_Panlexia)

# Execution begins:
ULD_to_Panlexia = helpers.get_other_id_to_Panlexia_id_map("ULD_id")
create_dictionaries_from_ULD(ULD_to_Panlexia)
