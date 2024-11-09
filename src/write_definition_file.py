"""Copy final Panlexia concept ids and English definitions to a file.

Initial concept ids for Panlexia are created based on Concepticon and ULD data.

Input: master.tsv:
    Tab-separated values file for mapping initial Panlexia ids
    to Concepticon or ULD definition and other ids.

Output: eng-definition.tsv:
    Data table file with two columns: id and English definition.

CC-BY 2024 Panlexia (https://github.com/barumau/panlexia)
"""
import helpers

def create_english_definition_file_from_master():
    """Writes ready (non-empty) ids and their definitions to a file."""

    definition_writer = helpers.tsv_writer('concepts/E/eng-definition.tsv', 'w')
    definition_writer.dict.writerow(["id", "Definition"])

    combined = helpers.tsv_reader('data/master.tsv')
    for row in combined.dict:
        if row["id"] != "":
            definition_writer.dict.writerow([row["id"], row["Definition"]])

# Execution begins
create_english_definition_file_from_master()