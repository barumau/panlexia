"""Extract definitions for Panlexia concept ids.

Definitions are extracted from Open Multilingual Wordnet 1.4 (OMW) and Concepticon.

Output: <lang code>-definition.tsv files:
    Data table file with two columns: id | Definition.
    The id field has the Panlexia concept id.
    The definitions are written the given language.

CC-BY 2024 Panlexia (https://github.com/barumau/panlexia)
"""
import helpers
import csv
import pandas as pd
import nltk
from nltk.corpus import wordnet as wn

def get_concept_definition_file_path(lang):
    """Returns path to concept definition file."""
    path = 'concepts/' + lang[0].upper() + '/' + lang + '-definition.tsv'
    return path

def get_existing_ids(definition_filename):
    dataframe = pd.read_csv(definition_filename, delimiter='\t')
    ids = dataframe['id'].to_list()
    return ids

def get_original_concept_list(definition_filename):
    with open(definition_filename) as f:
        reader = csv.reader(f, delimiter='\t')
        concept_list = list(reader)

    concept_list = concept_list[1:]
    return concept_list

def create_definitions_for(language_code):
    definition_filename = get_concept_definition_file_path(language_code)

    existing_ids = get_existing_ids(definition_filename)
    definitions = get_original_concept_list(definition_filename)

    id_map = helpers.tsv_reader('data/id_map.tsv')
    for row in id_map.dict:
        id = row["id"]
        if id not in existing_ids:
            if id.split(':')[0] == 'PWN':
                synset_id = id.split(':')[1]
                synset = wn.synset(synset_id)
                definition = synset.definition(lang=language_code)
                if definition is not None:
                    print(synset.lemma_names(language_code), definition)
                    definitions.append([id, definition])

    definition_writer = helpers.tsv_writer(definition_filename, 'w')
    definition_writer.dict.writerow(["id", "Definition"])
    for definition in definitions:
        definition_writer.dict.writerow(definition)

def create_definitions_from_OMW():
    """Creates concept definition file from OMW data for the languages, whose codes are listed below."""
    #Download Open Multilingual Wordnet data only in the first run.
    #nltk.download('omw-1.4')
    create_definitions_for('eng')
    create_definitions_for('ita')
    create_definitions_for('ind')
    create_definitions_for('jpn')
    create_definitions_for('ell')

# Execution begins
create_definitions_from_OMW()
