"""Adds concept definitions and missing concepts to a dictionary file.

This program takes one argument, which is the language code.
Example command for running this program:
    python3 src/add_definitions_to_dictionary.py fra

The program will
1. open the dictionary file by the language code (f.ex. dict/F/fra.tsv)
2. insert concept definitions to the last column in the dictionary file.
3. insert ids and definitions for concepts that haven't been translated yet
4. write the modified file with the same name (f.ex. dict/F/fra.tsv).

The header row of the dictionary will change, for example, as below:
    Before: id	style	word
    After:  id	style	word	definition

CC-BY 2025 Panlexia (https://github.com/barumau/panlexia)
"""
import csv
import helpers
import sys


def get_header_row(filename):
    """Get the header row of a dictionary as a list."""
    reader = helpers.tsv_reader(filename)
    return reader.dict.fieldnames

def get_dictionary_to_list(original_file):
    """Read dictionary to a list without the header row."""
    with open(original_file) as f:
        reader = csv.reader(f, delimiter='\t')
        word_list = list(reader)

    # Remove the header row, sort the list and return it.
    return sorted(word_list[1:])

def sort_and_write_to_dictionary_file(lang_name, header_row, data):
    """Sort the id map by Panlexia id and write a TSV file with a header row."""
    sorted_map = sorted(data)

    filename = helpers.get_dictionary_filename(lang_name)
    outfile = helpers.tsv_writer(filename, 'w')

    header_row.append("definition")
    outfile.dict.writerow(header_row)

    for row in sorted_map:
        outfile.dict.writerow(row)

def write_dictionary_with_definitions(lang_code, header_row, word_list, definition_list):
    """Writes dictionary for one language ordered by Panlexia id."""
    word_index = 0
    definition_index = 0
    num_of_words = len(word_list)
    num_of_definitions = len(definition_list)
    num_of_columns = len(word_list[0])
    dictionary = []
    last_match = ""

    # Iterate over the word list.
    while word_index < num_of_words:
        # Iterate over the definition list.
        #print(word_list[i])
        while definition_index < num_of_definitions:
            #print(i, id_index, word_list[i][0], definition_list[id_index][0])
            if definition_list[definition_index][0] == word_list[word_index][0]:
                last_match = definition_list[definition_index][0]

                row = word_list[word_index]
                row.append(definition_list[definition_index][1])
                dictionary.append(row)
                break
            else:
                if definition_list[definition_index][0] != last_match:
                    if num_of_columns == 3:
                        dictionary.append([definition_list[definition_index][0], "", "",
                                           definition_list[definition_index][1]])
                    elif num_of_columns == 4:
                        dictionary.append([definition_list[definition_index][0], "", "", "",
                                           definition_list[definition_index][1]])
                    elif num_of_columns == 5:
                        dictionary.append([definition_list[definition_index][0], "", "", "", "",
                                           definition_list[definition_index][1]])
                definition_index = definition_index + 1
        word_index = word_index + 1

    #print(dictionary)
    sort_and_write_to_dictionary_file(lang_code, header_row, dictionary)


lang_code = sys.argv[1]
original_filename = helpers.get_dictionary_filename(lang_code)
header_row = get_header_row(original_filename)
original_dict = get_dictionary_to_list(original_filename)

definition_filename = 'concepts/E/eng-definition.tsv'
definition_dict = get_dictionary_to_list(definition_filename)

write_dictionary_with_definitions(lang_code, header_row, original_dict, definition_dict)
