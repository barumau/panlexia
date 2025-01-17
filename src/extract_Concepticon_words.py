"""Write language-specific dictionaries with Panlexia concept ids from ULD data.

CC-BY 2024 Panlexia (https://github.com/barumau/panlexia)
"""
import helpers

# Maps language ids from ISO 639-1 to ISO 639-3.
lang_code_map = {
    "af" : "afr",
    "ar" : "arb",
    "az" : "aze",
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

def sort_and_write_to_dictionary_file(lang_name, data):
    """Sort the id map by Panlexia id and write TSV file with a header row."""
    sorted_map = sorted(data)

    filename = "dict/" + lang_name[0].upper() + "/" + lang_name.lower() + ".tsv"
    outfile = helpers.tsv_writer(filename, 'w')
    outfile.dict.writerow(["id", "style", "word", "pronunciation"])

    for row in sorted_map:
        outfile.dict.writerow([row[0], "", row[1], ""])

def write_dictionary_for_one_language(lang_code, id_to_Panlexia):
    """Writes dictionary for one language ordered by Panlexia id."""
    dictionary = []
    source_file = 'data/Concepticon/mappings/map-' + lang_code + '.tsv'
    concepticon = helpers.tsv_reader(source_file)
    for row in concepticon.dict:
        id = ""
        if row["ID"] in id_to_Panlexia:
            id = id_to_Panlexia[row["ID"]]
        entry = row["GLOSS"]
        if id != "" and entry != "":
            word = entry.split('///')[1]
            if word != "NA":
                dictionary.append([id, word])
    code3 = lang_code_map[lang_code]
    print(lang_code, code3)
    sort_and_write_to_dictionary_file(code3, dictionary)

def create_dictionaries_from_Concepticon(id_to_Panlexia):
    #langs = ["af", "ar", "az", "ca", "cy", "da", "de", "el", "en", "es", "et", "fa", "fi", "fr", "ga", "ha", "he", "hu", "is", "it", "ja", "ka", "la", "lb", "lt", "mr", "mt", "nl", "no", "pl", "pt", "ru", "sk", "sr", "sv", "tr", "uk", "vi", "wo", "xh", "zh"]
    langs = ["af", "et", "lb", "mr", "mt", "sr", "wo", "xh"]
    for lang in langs:
        write_dictionary_for_one_language(lang, id_to_Panlexia)

# Execution begins:
Concepticon_to_Panlexia = helpers.get_other_id_to_Panlexia_id_map("Concepticon_id")
create_dictionaries_from_Concepticon(Concepticon_to_Panlexia)
