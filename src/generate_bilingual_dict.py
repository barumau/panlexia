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

def format_and_write(source_lang, target_lang, dict):
    """Sorts the dictionary alphabetically and writes it to file in Markdown format."""
    sorted_dict = sorted(dict)

    filename = "generated/" + source_lang + "-" + target_lang + ".md"
    file = helpers.simple_file_writer(filename)

    previous_initial = ""

    for row in sorted_dict:
        initial = row[0][0].upper()
        if previous_initial != initial:
            # Write alphabetic section header, like "## A"
            file.write("\n## " + initial + "\n\n")
            previous_initial = initial

        # Make bilingual entry in simple Markdown format.
        # The format is: **source_word** *PoS* target_word
        #              source_word            PoS             target_word
        entry = '**' + row[0] + '**' + " *" + row[1] + '* ' + row[2]
        file.write(entry + "\n")
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