"""Write language-specific dictionaries with Panlexia concept ids from WOLD data.

- Transform `Parameter_ID` to Panlexia concept id.
- Transform `Language_ID` to the 3-letter language code.
- If there is content in the `original_script` field,
    copy it to the `word` field and copy from the `Form` field to the `transcription` field.
  Else copy the `Form` field to the `word` field.
- Get etymological information:
    - If the "Borrowed" field is "1. clearly borrowed" or "2. probably borrowed"
        - Match `ID` with "Target_Form_ID" in borrowings.csv
        - Get the 3-letter language code by the source "Language_ID"
          and the source form from the "Comment" field.
        - Write "<src>:<form>" to the "etymology" field.

ID,Target_Form_ID,Source_Form_ID,Comment,Source,relation,certain,Language_ID
7164,19687,,lokhadātu,,earlier,true,251
7165,19687,,shìjiè,,immediate,true,89

CC-BY 2024 Panlexia (https://github.com/barumau/panlexia)
"""
import helpers

WOLD_forms = 'data/WOLD/forms.csv'
WOLD_languages = 'data/WOLD/languages.csv'
WOLD_etymology = 'data/WOLD/borrowings.csv'

def sort_and_write_to_dictionary_file(lang_name, data):
    """Sort the id map by Panlexia id and write TSV file with a header row."""
    sorted_map = sorted(data)

    filename = "dict/" + lang_name[0].upper() + "/" + lang_name.lower() + ".tsv"
    outfile = helpers.tsv_writer(filename, 'w')
    outfile.dict.writerow(["id", "word"])

    for row in sorted_map:
        outfile.dict.writerow([row[0], row[1]])

def write_dictionary_for_one_language(lang_id, lang_code, WOLD_to_Panlexia):
    """Writes dictionary for one language ordered by Panlexia id."""
    print("Getting words for", lang_code)
    dictionary = []
    forms = helpers.csv_reader(WOLD_forms, ',')
    for row in forms.dict:
        if row["Language_ID"] == lang_id:
            id = WOLD_to_Panlexia[row["Parameter_ID"]]
            word = row["Form"]
            if id != "" and word != "":
                dictionary.append([id, word])
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

def create_dictionaries_from_WOLD(WOLD_to_Panlexia):
    langs = get_41_languages()
    for lang in langs:
        write_dictionary_for_one_language(lang[0], lang[1], WOLD_to_Panlexia)

# Execution begins:
WOLD_to_Panlexia = helpers.get_other_id_to_Panlexia_id_map("WOLD_id")
create_dictionaries_from_WOLD(WOLD_to_Panlexia)