"""Write language-specific dictionaries with Panlexia concept ids from Concepticon data.

CC-BY 2025 Panlexia (https://github.com/barumau/panlexia)
"""
import helpers
import csv

# Maps language ids from ISO 639-1 to ISO 639-3.
lang_code_map = {
    "af" : "afr",
    "ar" : "arb",
    "az" : "azj",
    "ca" : "cat",
    "cy" : "cym",
    "da" : "dan",
    "de" : "deu",
    "el" : "ell",
    "en" : "eng",
    "es" : "spa",
    "et" : "est",
    "fa" : "fas",
    "fi" : "fin",
    "fr" : "fra",
    "ga" : "gle",
    "ha" : "hau",
    "he" : "heb",
    "hu" : "hun",
    "is" : "isl",
    "it" : "ita",
    "ja" : "jpn",
    "ka" : "kat",
    "la" : "lat",
    "lb" : "ltz",
    "lt" : "lit",
    "mr" : "mar",
    "mt" : "mlt",
    "nl" : "nld",
    "no" : "nor",
    "pl" : "pol",
    "pt" : "por",
    "ru" : "rus",
    "sk" : "slk",
    "sr" : "srp",
    "sv" : "swe",
    "tr" : "tur",
    "uk" : "ukr",
    "vi" : "vie",
    "wo" : "wol",
    "xh" : "xho",
    "zh" : "cmn"
}

def get_dictionary_filename(lang_code):
    filename = "dict/" + lang_code[0].upper() + "/" + lang_code.lower() + ".tsv"
    return filename

def sort_and_write_to_dictionary_file(lang_name, data):
    """Sort the id map by Panlexia id and write TSV file with a header row."""
    sorted_map = sorted(data)

    filename = get_dictionary_filename(lang_name)
    outfile = helpers.tsv_writer(filename, 'w')
    outfile.dict.writerow(["id", "style", "word", "pronunciation"])

    for row in sorted_map:
        if len(row) == 2:
            outfile.dict.writerow([row[0], "", row[1], ""])
        if len(row) == 3:
            outfile.dict.writerow([row[0], row[1], row[2], ""])
        elif len(row) == 4:
            outfile.dict.writerow([row[0], row[1], row[2], row[3]])
        elif len(row) == 5:
            outfile.dict.writerow([row[0], row[1], row[2], row[3], row[4]])

def get_original_word_list(lang_code):
    original_file = get_dictionary_filename(lang_code)

    with open(original_file) as f:
        reader = csv.reader(f, delimiter='\t')
        word_list = list(reader)

    word_list = word_list[1:]
    return word_list

def does_concept_exist_already(dictionary, id):
    for row in dictionary:
        if row[0] == id:
            return True
    return False

def write_dictionary_for_one_language(lang_code, id_to_Panlexia):
    """Writes dictionary for one language ordered by Panlexia id."""
    code3 = lang_code_map[lang_code]
    dictionary = get_original_word_list(code3)
    source_file = 'data/Concepticon/mappings/map-' + lang_code + '.tsv'
    concepticon = helpers.tsv_reader(source_file)
    for row in concepticon.dict:
        id = ""
        if row["ID"] in id_to_Panlexia:
            id = id_to_Panlexia[row["ID"]]
        entry = row["GLOSS"]
        if id != "" and entry != "":
            exists = does_concept_exist_already(dictionary, id)
            if exists == False:
                word = entry.split('///')[1]
                if word != "NA":
                    dictionary.append([id, word.lower()])
    print(lang_code, code3)
    sort_and_write_to_dictionary_file(code3, dictionary)

def create_dictionaries_from_Concepticon(id_to_Panlexia):
    langs = ["af", "ar", "az", "ca", "cy", "da", "de", "el", "en", "es", "et", "fa", "fi", "fr", "ga", "ha", "he", "hu", "is", "it", "ja", "ka", "la", "lb", "lt", "mr", "mt", "nl", "no", "pl", "pt", "ru", "sk", "sr", "sv", "tr", "uk", "vi", "wo", "xh", "zh"]
    for lang in langs:
        write_dictionary_for_one_language(lang, id_to_Panlexia)

# Execution begins:
Concepticon_to_Panlexia = helpers.get_other_id_to_Panlexia_id_map("Concepticon_id")
create_dictionaries_from_Concepticon(Concepticon_to_Panlexia)
