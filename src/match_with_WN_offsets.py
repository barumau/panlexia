"""Program for getting WordNet ids and definitions.

Steps to install the Natural Language Toolkit (NLTK) first:
    1. pip install nltk
    2. Start the Python interpreter:
        python3
    3. Download Wordnet in the Python interpreter:
       import nltk
       nltk.download('wordnet')

See https://www.nltk.org/howto/wordnet.html

CC-BY 2024 Panlexia (https://github.com/barumau/panlexia)
"""

import helpers
from nltk.corpus import wordnet
from nltk.corpus import wordnet as wn

def test_synset_finding():
    """For testing purposes only."""
    print(wn.synsets('dog'))
    print(wn.synsets('dog', pos=wn.VERB))
    print(wn.synset_from_pos_and_offset('n',4543158))
    print(wn.synset_from_pos_and_offset('n',4543158).definition())
    print(wn.synsets('wagon', pos='n')[0].definition())
    print(wn.synsets('well', pos='a')[0].definition())
    print(wn.synsets('wagon', pos='n')[0].offset())

map_to_wn_pos = {
    'A' : 'a',
    'ADV' : 'r',
    'N' : 'n',
    'V' : 'v'
    # No Panlexia PoS for 's' i.e. adjective satellite (ADJ_SAT), which
    # "represents a concept that is similar in meaning to the concept represented by the head synset".
}

def get_WN_pos(id):
    panlexia_pos = helpers.get_PoS(id)
    if panlexia_pos in map_to_wn_pos:
        return map_to_wn_pos[panlexia_pos]
    return ''

def get_truncated_term(id):
    """Returns truncated term from id. F.ex. returns 'hit' from 'Action:hit (a target).V'."""
    term = helpers.get_term(id)
    return term.split(' ')[0]

def match_with_WN_offsets() :
    """Try to find a match for each Panlexia concepts in Wordnet and print them."""
    master_file = 'data/master.tsv'
    master = helpers.tsv_reader(master_file)
    for row in master.dict:
        if row["id"] != '':
            pos = get_WN_pos(row["id"])
            term = get_truncated_term(row["id"])
            # Find a synonym set with the term and the part of speech.
            synsets = wn.synsets(term, pos=pos)
            if len(synsets) > 0:
                # Use the first synonym, because it is usually the most frequent one and hence probably right.
                synset = synsets[0]
                # Print the data for manual processing.
                print(row["id"], "\t", synset.offset(), "\t", synset.pos(), "\t", synset.name(), "\t", synset.definition())
            else:
                print("")

match_with_WN_offsets()
