"""Extract definitions for Panlexia concept ids.

Definitions are extracted from Open Multilingual Wordnet 1.4 (OMW) and Concepticon.

Output: <lang code>-definition.tsv files:
    Data table file with two columns: id | Definition.
    The id field has the Panlexia concept id.
    The definitions are written the given language.

CC-BY 2024 Panlexia (https://github.com/barumau/panlexia)
"""
import helpers
import nltk
from nltk.corpus import wordnet as wn

def get_concept_definition_file_path(lang):
    """Returns path to concept definition file."""
    path = 'concepts/' + lang[0].upper() + '/' + lang + '-definition.tsv'
    return path

def create_english_definition_file_from_master():
    """Writes ready (non-empty) ids and their definitions to a file."""

    definition_writer = helpers.tsv_writer('concepts/E/eng-definition.tsv', 'w')
    definition_writer.dict.writerow(["id", "Definition"])

    combined = helpers.tsv_reader('data/worksheet.tsv')
    for row in combined.dict:
        if row["id"] != "":
            definition_writer.dict.writerow([row["id"], row["Definition"]])

def create_definitions_for(language_code):
    definition_filename = get_concept_definition_file_path(language_code)
    definition_writer = helpers.tsv_writer(definition_filename, 'w')
    definition_writer.dict.writerow(["id", "Definition"])

    id_map = helpers.tsv_reader('data/id_map.tsv')
    for row in id_map.dict:
        id = row["id"]
        if id.split(':')[0] == 'PWN':
            synset_id = id.split(':')[1]
            synset = wn.synset(synset_id)
            print(synset.lemma_names(language_code))
            definition = synset.definition(lang=language_code)
            if definition is not None:
                definition_writer.dict.writerow([id, definition[0]])

def create_other_definitions_from_OMW():
    """Creates concept definition file from OMW data for the languages, whose codes are listed below."""
    #Download Open Multilingual Wordnet data only in the first run.
    #nltk.download('omw-1.4')
    create_definitions_for('ita')
    create_definitions_for('ind')
    create_definitions_for('jpn')
    create_definitions_for('ell')

# Execution begins
create_english_definition_file_from_master()
create_other_definitions_from_OMW()