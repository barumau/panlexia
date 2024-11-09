"""Writes index file with links to generated bilingual dictionaries.

This program takes two arguments:
    1. Code or name of the main source language.
    2. Name of the file with a list of the target languages.

Example command for running this program:
    src/make_dict_index.py eng dict_list.txt
It will create an index of dictionaries from/to English (eng).

CC-BY 2024 Panlexia (https://github.com/barumau/panlexia)
"""
import helpers
import sys

def get_language_list(list_filename):
    list_file = helpers.simple_file_reader(list_filename)
    codes = []

    while True:
        lang = list_file.readline().strip()
        if lang == "":
            break
        codes.append(lang)

    print(codes)
    return codes

main_lang = sys.argv[1]
list_filename = sys.argv[2]

codes = get_language_list(list_filename)
index_file = helpers.simple_file_writer("generated/index.md")
index_file.write("# PANLEXIA\n\n")
for code in codes:
    link = main_lang + "-" + code + ".md"
    link_text = main_lang + "-" + code
    index_file.write("[" + link_text + "](" + link + ")\n")

index_file.write("\n\"[Panlexia](https://github.com/barumau/panlexia)\" by Risto Kupsala et al. is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)\n")