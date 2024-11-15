"""Writes bilingual dictionaries from a source language to a target language.

This program takes two arguments:
    1. Language code for the source language
    2. Language code for the target language

Example command for running this program:
    python3 src/write_bilingual_dict.py eng fra
It will create a bilingual English to French dictionary by the name eng-fra.md
in the Markdown format into the generated/ directory.

CC-BY 2024 Panlexia (https://github.com/barumau/panlexia)
"""
import helpers
import sys

def make_bilingual_dictionary_table(source_language_dict, target_language_dict):
    """Iterate through both dictionaries and combine rows with the same id."""

    # Open monolingual source language dictionary.
    source_reader = helpers.tsv_reader(source_language_dict)
    source_dict = source_reader.dict
    target_reader = helpers.tsv_reader(target_language_dict)
    target_dict = target_reader.dict

    # Collect transcription or pronunciation if available.
    has_transcription = False
    has_pronunciation = False
    if "transcription" in target_dict.fieldnames:
        has_transcription = True
    elif "pronunciation" in target_dict.fieldnames:
        has_pronunciation = True

    # Start both dictionaries from the first row.
    source_row = next(source_dict, None)
    target_row = next(target_dict, None)

    bilingual_dictionary = []

    while True:
        if source_row == None or target_row == None:
            # Break the loop when one or the other dictionary has been read to the end.
            break
        if source_row["id"] == target_row["id"]:
            word_class = source_row["id"].split('.')[1].lower()
            if has_transcription:
                bilingual_dictionary.append([source_row["word"], word_class, target_row["word"], target_row["transcription"]])
            elif has_pronunciation:
                bilingual_dictionary.append([source_row["word"], word_class, target_row["word"], target_row["pronunciation"]])
            else:
                bilingual_dictionary.append([source_row["word"], word_class, target_row["word"]])
            # TODO: Handle synonyms better.
            # Advance only target row in case of synonyms.
            target_row = next(target_dict, None)
        elif source_row["id"] < target_row["id"]:
            # The source dictionary is behind the target dictionary.
            source_row = next(source_dict, None)
        else:
            # The source dictionary is ahead of the target dictionary.
            target_row = next(target_dict, None)

    return bilingual_dictionary

def circled_number(num):
    if num == 1:
        return " ① "
    elif num == 2:
        return " ② "
    elif num == 3:
        return " ③ "
    elif num == 4:
        return " ④ "
    elif num == 5:
        return " ⑤ "
    elif num == 6:
        return " ⑥ "
    else:
        return " (" + num.__str__() + ") "

def is_synonym(row_A, row_B):
        """Return True if term (0) and word-class (1) are the same."""
        if row_A[0] == row_B[0] and row_A[1] == row_B[1]:
            return True
        else:
            return False

def build_translation(row):
    """Builds translation term with its optional pronunciation."""
    translation = row[2]
    # Include transcription or pronunciation if the field for it is available and not empty.
    if len(row) == 4 and row[3] != "":
        # The format is: target_word /pronunciation/
        translation = translation + " /" + row[3] + "/"
    return translation

def format_and_write(source_lang, target_lang, dict):
    """Sorts the dictionary alphabetically and writes it to file in Markdown format."""
    # Sort the words in case-insensitive way.
    sorted_dict = sorted(dict, key=lambda s: s[0].casefold())

    filename = "generated/" + source_lang + "-" + target_lang + ".md"
    file = helpers.simple_file_writer(filename)

    previous_initial = ""
    i = 0
    while i < len(sorted_dict):
        row = sorted_dict[i]
        initial = row[0][0].upper()
        if previous_initial != initial:
            # Write alphabetic section header, like "## A"
            file.write("\n## " + initial + "\n\n")
            previous_initial = initial

        translation = build_translation(row)
        j = 1
        while i + j < len(sorted_dict):
            next_row = sorted_dict[i + j]
            if is_synonym(row, next_row):
                j = j + 1
                translation = translation + circled_number(j) + build_translation(next_row)
            else:
                break

        if j > 1:
            # Add number also before the first translation.
            translation = circled_number(1) + translation

        # Make bilingual entry in simple Markdown format.
        # The format is: **source_word** *PoS* target_word /pronunciation/
        entry = '**' + row[0] + '**' + " *" + row[1] + '* ' + translation
        file.write(entry + "  \n")
        i = i + j
        # Uncomment the following line if you want to print the entries to the screen.
        #print(entry)

    file.write("\n\"[Panlexia](https://github.com/barumau/panlexia)\" by Risto Kupsala et al. is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)")
    print(f"Created {filename} with {len(sorted_dict)} entry terms.")

def get_dictionary_filename(lang_code):
    filename = "dict/" + lang_code[0].upper() + "/" + lang_code + ".tsv"
    return filename

source_lang = sys.argv[1]
target_lang = sys.argv[2]

if source_lang == target_lang:
    print("The source and target languages are the same:", source_lang)
    sys.exit

source_language_dict = get_dictionary_filename(source_lang)
target_language_dict = get_dictionary_filename(target_lang)

print(f"Making bilingual {source_lang}-{target_lang} dictionary...")

bilingual_dictionary = make_bilingual_dictionary_table(source_language_dict, target_language_dict)
format_and_write(source_lang, target_lang, bilingual_dictionary)