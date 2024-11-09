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
import math

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

def make_link(main_lang, code):
        link = main_lang + "-" + code + ".md"
        link_text = main_lang + "-" + code
        complete_link = "[" + link_text + "](" + link + ")"
        return complete_link

def make_cells(main_lang, codes):
    cells = []
    previous_initial = ""
    for code in codes:
        initial = code[0].upper()
        if initial != previous_initial:
            #if previous_initial != "":
            #    cells.append([""])
            text = "**" + initial + "**"
            cells.append([text])
            #cells.append([""])
            previous_initial = initial
        link = make_link(main_lang, code)
        cells.append([link])
    return cells

def print_in_columns(cells, num_of_columns):
    index_file = helpers.simple_file_writer("generated/index.md")
    index_file.write("---\nhide:\n  - navigation\n  - footer\n  - toc\n---\n")
    index_file.write("# PANLEXIA\n\n|")

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

    index_file.write("\n\"[Panlexia](https://github.com/barumau/panlexia)\" by Risto Kupsala et al. is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)\n")


# Execution begins here.
main_lang = sys.argv[1]
list_filename = sys.argv[2]

codes = sorted(get_language_list(list_filename))

cells = make_cells(main_lang, codes)

print_in_columns(cells, 3)
