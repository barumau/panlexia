# How to contribute to Panlexia

## How to add new translations

1.  Find a suitable concept from a concept definition file, like [concepts/E/eng-definition.tsv](../concepts/E/eng-definition.tsv).
2.  Copy the concept id, like `PLX:anything.pro`.
3.  Open the language-specific monolingual dictionary file, like [dict/E/eng.tsv](../dict/E/eng.tsv) for English,
    in a text editor or a spreadsheet program, like LibreOffice Calc or Microsoft Excel.
4.  Insert a new row, paste the concept id to the `id` field, and write a word that matches the definition to to the `word` field.
    The row would look something like this:  
    `PLX:anything.pro   anything`
5.  If there is more than one translation for the concept, create a separate row for each of them.

## How to add new concepts

What to do if a concept doesn't exist yet in the concept definition file?

1.  Most concepts in Panlexia come from Princeton Wordnet.
    Try to find a suitable Wordnet definition from [Wordnet](https://compling.upol.cz/ntumc/cgi-bin/wn-gridx.cgi).
2.  If a suitable concept is found, find out the concept id as below
    or assign a temporary id using the Wordnet offset id, like `TMP:12345678.n`.
3.  If the concept is not found, create a new Panlexia concept id, like `PLX:new_concept.n`.
    (Typically this is the case with function words, interjections and non-English cultural concepts.)
4.  Add the id and its definition to [concepts/E/eng-definition.tsv)(../concepts/E/eng-definition.tsv).
5.  Add the id and possibly its Wordnet offset id to [data/id_map.tsv](../data/id_map.tsv).
    `PWN:car.n.01    02958343-n`

For example, the Wordnet offset id for the concept 'automobile' is
[02958343-n](https://compling.upol.cz/ntumc/cgi-bin/wn-gridx.cgi?gridmode=ntumcgrid&synset=02958343-n&lang=eng&lang2=eng).
You can get its "name" in Python by calling the functions below.

```
~$ python3
>>> from nltk.corpus import wordnet as wn
>>> wn.synset_from_pos_and_offset('n', 2958343).name()
'car.n.01'
```

The corresponding concept id in Panlexia is therefore `PWN:car.n.01`.
