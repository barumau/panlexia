"""Write language-specific dictionaries with Panlexia concept ids from WOLD data.

- Transform `Parameter_ID` to Panlexia concept id.
- Transform `Language_ID` to the 3-letter language code.
- If there is content in the `original_script` field,
    copy it to the `word` field and copy from the `Form` field to the `transcription` field.
  Else copy the `Form` field to the `word` field.
- TODO: Get etymological information:
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
WOLD_forms_2 = 'data/WOLD/forms_fra_spa_deu_rus.tsv'
WOLD_languages = 'data/WOLD/languages.csv'
WOLD_etymology = 'data/WOLD/borrowings.csv'

def sort_and_write_to_dictionary_file(lang_name, data, column_num):
    """Sort the id map by Panlexia id and write TSV file with a header row."""
    sorted_map = sorted(data)

    filename = "dict/" + lang_name[0].upper() + "/" + lang_name.lower() + ".tsv"
    outfile = helpers.tsv_writer(filename, 'w')
    if column_num == 2:
        outfile.dict.writerow(["id", "word"])
    else:
        outfile.dict.writerow(["id", "word", "transcription"])
    
    for row in sorted_map:
        if column_num == 2:
            # Write id and word.
            outfile.dict.writerow([row[0], row[1]])
        else:
            if (len(row)) == 3:
                # Write id, word and transcription.
                outfile.dict.writerow([row[0], row[1], row[2]])
            else:
                # If row is missing data in the original_script field in WOLD,
                # write id, blank and transcription.
                outfile.dict.writerow([row[0], "", row[1]])

def write_dictionary_for_one_language(lang_id, lang_code, WOLD_to_Panlexia, dict, column_num):
    """Writes dictionary for one language ordered by Panlexia id."""
    print("Getting words for", lang_id, lang_code)

    has_transcription = False
    dictionary = []
    for row in dict:
        if row["Language_ID"] == lang_id:
            id = WOLD_to_Panlexia[row["Parameter_ID"]]
            word = ""
            if column_num == 3:
                word = row["original_script"]

            if word != "":
                has_transcription = True
                if id != "":
                    transcription = row["Form"]
                    dictionary.append([id, word, transcription])
            else:
                word = row["Form"]
                if id != "" and word != "":
                    dictionary.append([id, word])

    if has_transcription == False:
        column_num = 2
    sort_and_write_to_dictionary_file(lang_code, dictionary, column_num)

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
        write_dictionary_for_one_language(lang[0], lang[1], WOLD_to_Panlexia, forms.dict, 3)

def create_4_dictionaries_from_WOLD(WOLD_to_Panlexia):
    """Writes dictionaries for fra, spa, deu and rus."""
    langs = [["fra", "fra"], ["spa", "spa"], ["deu", "deu"], ["rus", "rus"]]
    for lang in langs:
        forms = helpers.tsv_reader(WOLD_forms_2)
        write_dictionary_for_one_language(lang[0], lang[1], WOLD_to_Panlexia, forms.dict, 2)

# Execution begins:
WOLD_to_Panlexia = helpers.get_other_id_to_Panlexia_id_map("WOLD_id")
create_4_dictionaries_from_WOLD(WOLD_to_Panlexia)
create_41_dictionaries_from_WOLD(WOLD_to_Panlexia)
