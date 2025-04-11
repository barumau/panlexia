"""Write language-specific dictionaries with Panlexia concept ids from data from other projects.

- NorthEuraLex (NELex)
- Concepticon
- World Loanword Database (WOLD)
- Universal Language Dictionary (ULD)

CC-BY 2025 Panlexia (https://github.com/barumau/panlexia)
"""
import helpers
import languages
import csv
import re
from nltk.corpus import wordnet as wn

id_map_file = 'data/id_map.tsv'
NorthEuraLex = 'data/NorthEuraLex/northeuralex-0.9-forms.tsv'
NELex_concepts = 'data/NorthEuraLex/northeuralex-0.9-concept-data.tsv'
WOLD_forms = 'data/WOLD/forms.csv'
WOLD_forms_2 = 'data/WOLD/forms_fra_spa_deu_rus.tsv'
WOLD_languages = 'data/WOLD/languages.csv'
WOLD_etymology = 'data/WOLD/borrowings.csv'
ULD_file = 'data/ULD/ULD.tsv'
Pandunia_master = 'pandunia_source.tsv'

# The column headers in NELex_concepts file are:
#Language_ID	Glottocode	Concept_ID	Word_Form	rawIPA	IPA	ASJP	List	Dolgo	Next_Step
#    0              1           2           3          4       5          6       7         8
Language_ID = 0
Glottocode = 1
Concept_ID = 2
Word_Form = 3
IPA = 4

def sort_and_write_to_dictionary_file(lang_name, data):
    """Sort the id map by Panlexia id and write TSV file with a header row."""
    sorted_map = sorted(data)

    filename = helpers.get_dictionary_filename(lang_name)
    outfile = helpers.tsv_writer(filename, 'w')

    column_num = len(data[0])
    if column_num == 5:
        outfile.dict.writerow(["id", "style", "word", "pronunciation", "etymology"])
    elif column_num == 4:
        outfile.dict.writerow(["id", "style", "word", "pronunciation"])
    else:
        outfile.dict.writerow(["id", "style", "word"])

    for row in sorted_map:
        if len(row) == 2:
            # Write id, style (blank) and word.
            outfile.dict.writerow([row[0], "", row[1], ""])
        if len(row) == 3:
            # Write id, style and word.
            outfile.dict.writerow([row[0], row[1], row[2], ""])
        elif len(row) == 4:
            # Write id, style, word, transcription and etymology.
            outfile.dict.writerow([row[0], row[1], row[2], row[3]])
        elif len(row) == 5:
            outfile.dict.writerow([row[0], row[1], row[2], row[3], row[4]])

def get_original_word_list(lang_code):
    original_file = helpers.get_dictionary_filename(lang_code)

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

def is_word_entry_new(dictionary, id, entry):
    for row in dictionary:
        if row[0] == id and row[2] == entry:
            return False
    return True

def write_dictionary_for_one_language(lang_code, id_to_Panlexia):
    """Writes dictionary for one language ordered by Panlexia id."""
    code3 = languages.language_code_from_2_to_3_letters[lang_code]
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
                    dictionary.append([id, "", word.lower()])
    print(lang_code, code3)
    sort_and_write_to_dictionary_file(code3, dictionary)

def create_dictionaries_from_Concepticon(id_to_Panlexia):
    langs = ["af", "ar", "az", "ca", "cy", "da", "de", "el", "en", "es", "et", "fa", "fi", "fr", "ga", "ha", "he", "hu", "is", "it", "ja", "ka", "la", "lb", "lt", "mr", "mt", "nl", "no", "pl", "pt", "ru", "sk", "sr", "sv", "tr", "uk", "vi", "wo", "xh", "zh"]
    for lang in langs:
        write_dictionary_for_one_language(lang, id_to_Panlexia)

def write_dictionary_for_one_language_in_ULD(lang_code, ULD_to_Panlexia):
    """Writes dictionary for one language ordered by Panlexia id."""
    dictionary = get_original_word_list(lang_code)
    uld = helpers.tsv_reader(ULD_file)
    for row in uld.dict:
        id = ""
        if row["number"] in ULD_to_Panlexia:
            id = ULD_to_Panlexia[row["number"]]
        entry = row[lang_code]
        if id != "" and entry != "":
            exists = does_concept_exist_already(dictionary, id)
            if exists == False:
                words = entry.split(',')
                for word in words:
                    dictionary.append([id, "", word.strip()])
    sort_and_write_to_dictionary_file(lang_code, dictionary)

def create_dictionaries_from_ULD(ULD_to_Panlexia):
    langs = ["epo", "Novial", "Lidepla", "Sambahsa"]
    for lang in langs:
        write_dictionary_for_one_language_in_ULD(lang, ULD_to_Panlexia)

def write_dictionary_for_one_language_in_PD(lang_code):
    """Writes dictionary for one language ordered by Panlexia id."""
    dictionary = get_original_word_list(lang_code)
    pd = helpers.tsv_reader(Pandunia_master)
    i = 0
    for row in pd.dict:
        id = row["id"]
        entry = row[lang_code]
        if id != "" and entry != "":
            words = entry.split(',')
            for word in words:
                word = word.strip()
                if is_word_entry_new(dictionary, id, word):
                    dictionary.append([id, "", word])
                    i = i + 1
    sort_and_write_to_dictionary_file(lang_code, dictionary)
    print("Wrote", i, "entries for", lang_code, "from old Pandunia master file.")

def create_dictionaries_from_PD_master():
    langs = ["eng", "deu", "fra", "spa", "por", "rus",
        "fas", "hin", "ben", "tam", "ind", "arb", "tur", "swh", "hau", "ful",
        "cmn", "yue", "jpn", "kor", "vie", "epo", "fin", "pol"]
    for lang in langs:
        write_dictionary_for_one_language_in_PD(lang)


def create_NELex_id_to_Panlexia_id_map():
    """Creates a map of NELex to Panlexia ids in the standard NELex order."""
    NELex = helpers.tsv_reader(NELex_concepts)
    NELex_to_Panlexia = []
    for row in NELex.dict:
        id = get_id_by_NELex_id(row["id_nelex"])
        NELex_to_Panlexia.append([row["id_nelex"], id])
    return NELex_to_Panlexia

def get_id_by_NELex_id(NELex_id):
    """Returns the corresponding Panlexia concept id to a NELex id."""
    id_map = helpers.tsv_reader(id_map_file)
    for row in id_map.dict:
        if NELex_id == row["NELex_id"]:
            return row["id"]
    return ""

def write_dictionary_for_one_language_in_NELex(datalist, i, n, NELex_to_Panlexia):
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
                    dictionary.append([NELex_to_Panlexia[id_index][1], "", datalist[i][Word_Form], datalist[i][IPA]])
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
            i = write_dictionary_for_one_language_in_NELex(datalist, i, data_size, NELex_to_Panlexia)

def get_language_code(id):
    """Get ISO-639-P3 languge code by language ID."""
    wold = helpers.csv_reader(WOLD_languages, ',')
    for row in wold.dict:
        if id == row["ID"]:
            return row["ISO639P3code"]
    return id

def get_etymology(id):
    """Get the source language and form of a borrowed word by form ID."""
    etym = ""
    wold = helpers.csv_reader(WOLD_etymology, ',')
    for row in wold.dict:
        if row["Target_Form_ID"] == id:
            code = get_language_code(row["Language_ID"])
            # Etymology data format is "<src>:<form>" where `src` is a 3-letter language code.
            etym = code + ":" + row["Comment"]
            break
    return etym

def write_dictionary_for_one_language_in_WOLD(lang_id, lang_code, WOLD_to_Panlexia, dict):
    """Writes dictionary for one language ordered by Panlexia id."""
    print("Getting words for", lang_id, lang_code)

    dictionary = get_original_word_list(lang_code)

    for row in dict:
        if row["Language_ID"] == lang_id:
            id = ""
            if row["Parameter_ID"] in WOLD_to_Panlexia:
                id = WOLD_to_Panlexia[row["Parameter_ID"]]
            if id != "":

                exists = does_concept_exist_already(dictionary, id)
                if exists == False:
                    # Get etymology for words that are clearly or probably borrowed.
                    etymology = ""
                    if "Borrowed" in dict.fieldnames:
                        if row["Borrowed"] == "1. clearly borrowed" or row["Borrowed"] == "2. probably borrowed":
                            etymology = get_etymology(row["ID"])

                    # Use the original script firstly.
                    word = row["original_script"]
                    if word != "":
                        transcription = row["Form"]
                        dictionary.append([id, "", word, transcription, etymology])
                    else:
                        word = row["Form"]
                        dictionary.append([id, "", word, "", etymology])

    print("Extracted", len(dictionary), "words for", lang_code)

    sort_and_write_to_dictionary_file(lang_code, dictionary)

def write_minimal_dictionary_for_one_language(lang_code, WOLD_to_Panlexia, dict):
    """Writes dictionary for one language ordered by Panlexia id."""
    print("Getting words for", lang_code)

    dictionary = get_original_word_list(lang_code)
    for row in dict:
        if row["Language_ID"] == lang_code:
            id = ""
            if row["Parameter_ID"] in WOLD_to_Panlexia:
                id = WOLD_to_Panlexia[row["Parameter_ID"]]
            word = row["Form"]
            if id != "" and word != "":
                exists = does_concept_exist_already(dictionary, id)
                if exists == False:
                    dictionary.append([id, "", word])

    print("Extracted", len(dictionary), "words for", lang_code)
    sort_and_write_to_dictionary_file(lang_code, dictionary)

def get_41_languages():
    """Gets table of numerical ids and 3-letter language codes for the 41 languages in WOLD."""
    languages = []
    wold = helpers.csv_reader(WOLD_languages, ',')
    i = 0
    for row in wold.dict:
        languages.append([row["ID"], row["ISO639P3code"]])
        i = i + 1
        if i == 41:
            break
    return languages

def create_41_dictionaries_from_WOLD(WOLD_to_Panlexia):
    """Writes dictionaries for the 41 languages in WOLD."""
    langs = get_41_languages()
    for lang in langs:
        forms = helpers.csv_reader(WOLD_forms, ',')
        write_dictionary_for_one_language_in_WOLD(lang[0], lang[1], WOLD_to_Panlexia, forms.dict)

def create_4_dictionaries_from_WOLD(WOLD_to_Panlexia):
    """Writes dictionaries for fra, spa, deu and rus."""
    langs = ["fra", "spa", "deu", "rus"]
    for lang in langs:
        forms = helpers.tsv_reader(WOLD_forms_2)
        write_minimal_dictionary_for_one_language(lang, WOLD_to_Panlexia, forms.dict)

def get_valid_entry(lemma):
    # Discard chemical element acronyms (like H and He), and numbers.
    if re.match(r"^([A-Z]|[A-Z][a-z]|[0-9])$", lemma):
        return None
    if "atomic_number" in lemma:
        return None
    # Delete species names, like 'Canis familiaris'.
    if re.match(r"^[A-Z][a-z]*_[a-z]*", lemma):
        return None
    return lemma.replace('_', ' ')

def write_dictionary_for_one_language_in_Wordnet(lang_code):
    """Writes dictionary for one language ordered by Panlexia id."""
    dictionary = get_original_word_list(lang_code)
    new_entries = []
    id_map = helpers.tsv_reader(id_map_file)
    for row in id_map.dict:
        id = row['id']
        PWN_id = row['PWN_id']
        if PWN_id != "":
            offset = PWN_id.split('-')[0]
            pos = PWN_id.split('-')[1]
            synset = wn.synset_from_pos_and_offset(pos, int(offset))

            for lemma in synset.lemma_names(lang_code):
                word = get_valid_entry(lemma)
                if word is not None:
                    if is_word_entry_new(dictionary, id, word):
                        new_entries.append([id, "", word])
                        print(id, word)

    sort_and_write_to_dictionary_file(lang_code, dictionary + new_entries)

def create_dictionaries_from_Wordnet():
    """Writes dictionaries for languages in NLTK/Wordnet."""
    langs = ['ell', 'eng', 'fin', 'ind', 'ita', 'jpn', 'arb', 'cmn', 'fra', 'pol', 'spa', 'por', 'ron', 'swe', 'tha', 'nld']
    for lang in langs:
        write_dictionary_for_one_language_in_Wordnet(lang)

# Execution begins:
if False:
    NELex_to_Panlexia = create_NELex_id_to_Panlexia_id_map()
    create_dictionaries_from_NELex(NELex_to_Panlexia)

    #WOLD_to_Panlexia = helpers.get_other_id_to_Panlexia_id_map("WOLD_id")
    create_4_dictionaries_from_WOLD(WOLD_to_Panlexia)
    create_41_dictionaries_from_WOLD(WOLD_to_Panlexia)

    Concepticon_to_Panlexia = helpers.get_other_id_to_Panlexia_id_map("Concepticon_id")
    create_dictionaries_from_Concepticon(Concepticon_to_Panlexia)

    ULD_to_Panlexia = helpers.get_other_id_to_Panlexia_id_map("ULD_id")
    create_dictionaries_from_ULD(ULD_to_Panlexia)

create_dictionaries_from_Wordnet()

#Used only by Barumau.
#create_dictionaries_from_PD_master()
