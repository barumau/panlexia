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
import languages
import sys
import math

lang_index = 0
code_index = 1

main_lang_first = 1
main_lang_last = 2

def get_language_list(list_filename):
    list_file = helpers.simple_file_reader(list_filename)
    codes = []

    while True:
        lang = list_file.readline().strip()
        if lang == "":
            break
        language_name = languages.code_to_pandunia(lang) + " (" + languages.code_to_endonym(lang) + ")"
        codes.append([language_name, lang])

    print(codes)
    return codes

def make_link(main_lang, code, direction):
    if direction == main_lang_first:
        link = main_lang + "-" + code[code_index] + ".md"
    else:
        link = code[code_index] + "-" + main_lang + ".md"
    link_text = code[lang_index]
    complete_link = "[" + link_text + "](" + link + ")"
    return complete_link

def make_alphabetic_link_list(main_lang, codes, direction):
    cells = []
    previous_initial = ""
    for code in codes:
        initial = code[lang_index][0].upper()
        if initial != previous_initial:
            #if previous_initial != "":
            #    cells.append([""])
            text = "**" + initial + "**"
            cells.append([text])
            #cells.append([""])
            previous_initial = initial
        link = make_link(main_lang, code, direction)
        cells.append([link])
    return cells

def print_in_columns(cells, num_of_columns, index_file):
    # Write empty header row and separator row with n columns, because Markdown syntax requires them.
    # |     |     |     |
    # |-----|-----|-----|
    j = 0
    while j < num_of_columns:
        index_file.write("   |")
        j = j + 1
    index_file.write("\n|")
    j = 0
    while j < num_of_columns:
        index_file.write("-----|")
        j = j + 1
    index_file.write("\n")

    i = 0
    section_size = math.ceil(len(cells) / num_of_columns)

    # Write dictionary links to rows with n columns.
    while i < section_size:
        line = "|"
        j = 0
        while j < num_of_columns:
            index = (j * section_size) + i
            if index < len(cells):
                # The last column may have less lines than the others.
                line = line + cells[index][0]
            line = line + " |"
            j = j + 1
        i = i + 1
        index_file.write(line)
        index_file.write("\n")
        print(line)

# Execution begins here.
main_lang = sys.argv[1]
list_filename = sys.argv[2]

codes = sorted(get_language_list(list_filename))

dictionaries_from_main_lang = make_alphabetic_link_list(main_lang, codes, main_lang_first)
dictionaries_to_main_lang = make_alphabetic_link_list(main_lang, codes, main_lang_last)

index_file = helpers.simple_file_writer("generated/index.md")
index_file.write("---\nhide:\n  - navigation\n  - footer\n  - toc\n---\n")
index_file.write("# PANLEXIA\n\n")
index_file.write("## " + main_lang + " →\n\n|")

print_in_columns(dictionaries_from_main_lang, 4, index_file)

index_file.write("\n\n## → " + main_lang + "\n\n|")

print_in_columns(dictionaries_to_main_lang, 4, index_file)

# Write the license.
index_file.write("\n\"[Panlexia](https://github.com/barumau/panlexia)\" by Risto Kupsala et al. is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)\n")
