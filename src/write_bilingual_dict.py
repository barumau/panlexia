"""Writes bilingual dictionaries for one source language to many target languages.

CC-BY 2024 Panlexia (https://github.com/barumau/panlexia)
"""
import helpers

source_language_dict = 'dict/P/pandunia.tsv'
target_language_dict = 'dict/F/fra.tsv'

def make_bilingual_entry(source_row, target_row):
    word_class = source_row["id"].split('.')[1].lower()
    # Makes bilingual entry in simple Markdown format.
    # The format is: **source_word** *PoS* target_word
    entry = '**' + source_row["word"] + '**' + " *" + word_class + '* ' + target_row["word"]
    return entry

def write_dictionary_for_one_pair():
    """Iterate through the source language and find matching ids in the target language."""

    # Open monolingual source language dictionary.
    source_reader = helpers.tsv_reader(source_language_dict)
    source_dict = source_reader.dict
    target_reader = helpers.tsv_reader(target_language_dict)
    target_dict = target_reader.dict
    # Start both dictionaries from the first row.
    source_row = next(source_dict, None)
    target_row = next(target_dict, None)
    while True:
        if source_row == None or target_row == None:
            # Break the loop when one or the other dictionary has been read to the end.
            break
        if source_row["id"] == target_row["id"]:
            # TODO: Print to file.
            entry = make_bilingual_entry(source_row, target_row)
            print(entry)
            # TODO: Handle synonyms better.
            # Advance only target row in case of synonyms.
            target_row = next(target_dict, None)
        elif source_row["id"] < target_row["id"]:
            # The source dictionary is behind the target dictionary.
            source_row = next(source_dict, None)
        else:
            # The source dictionary is ahead of the target dictionary.
            target_row = next(target_dict, None)

write_dictionary_for_one_pair()