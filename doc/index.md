# Panlexia

Panlexia is a universal dictionary.
It is a system for translating concepts (meanings) between different languages.

At the heart of Panlexia is a set of well defined concepts.
Each [concept definition](definition.md) is associated to a unique identifier, the [concept id](id.md).
This id is in turn associated to words that cover the meaning of the concept.
Interlinked concept definitions and words constitute a database, which can be used for many purposes.

The primary purpose of Panlexia is to serve as the source material for word lists and dictionaries between different languages.
It is possibe to generate a dictionary between any pair of languages,
which have words that are associated to the same concepts.

The [contents](contents.md) of Panlexia is made up of TSV (tab-separated value) files.
Each row in each file has a unique concept id and a word, a definition or other data.
The identifier links definitions and words in various languages together.
The identifier also links each word in one language to its equivalents in other languages.
This way the database can serve as a source for translation dictionaries.
