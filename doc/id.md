# The concept id

## Introduction

The concept ids are a key ingredient in Panlexia.
They are built so that they give a hint of the meaning of the concept in English
and some grammatical information.
There are two kinds of concept ids currently.

1.  `PWN:term.PoS.01`  
    These concept ids are technically "concept names" from Princeton Wordnet and Open Multilingual Wordnet.
    Princeton Wordnet (PWN) is a comprehensive semantic network of the English language,
    and it has been adapted to many other languages.

    The prefix `PWN` is followed by the colon `:` and the "concept name" from Wordnet.
    The "concept name" is made up of a term, a part of speech (PoS) abbreviation and the number of the concept.
    
    The ids are numbered because there can be many meanings for the same word.
    For example:  
    `PWN:anger.n.01` is a noun that means 'a strong emotion of hostility'.  
    `PWN:anger.v.01` is a transtive verb that means 'to make someone angry'.  
    `PWN:anger.v.02` is an intransitive verb that means 'to get angry'.

2.  `PLX:term.PoS`  
    Concepts that start with the prefix `PLX` are created for Panlexia.
    These are always concepts that don't exist in Princeton Wordnet.

    Princeton Wordnet, as a semantic network, is full of **content words**,
    which are the words that contain information about the world outside the language.
    It omits **grammar words**, which contain information about the language system itself.
    Grammar words connect content words together into meaningful sentences
    but add add little meaning beyond defining the relationship between other words.
    However, Panlexia, as a universal dictionary, has to cover also grammar words
    and even grammatical morphemes, which are units smaller than words.

    Grammar words include several parts of speech,
    like pronouns, prepositions, conjunctions and grammatical particles.
    Sometimes these are identified by grammatical codes.
    For example:  
    `PLX:3SG.pro` is a 3rd person singular pronoun that means 'he or she or it'.  
    `PLX:3SG F.pro` is a 3rd person singular female pronoun that means 'she'.  
    `PLX:3SG M.pro` is a 3rd person singular male pronoun that means 'he'.  
    `PLX:3PL.pro` is a 3rd person plural pronoun that means 'they'.

The concept ids are made up of the following parts:

- the source of the idthesaurusa meaning field: The field of meaning where the concept belongs or the topic that the concept is about.
- a colon (`:`)
- a term: A word or phrase that identifies the concept in the field of meaning.
- a period (`.`)
- a word-class marker: One or several uppercase letters that identify the word class of the concept.

For example, the concept id `Family:father.N` consists of
the field `Family`
the term `father`
and the word-class marker `N`, which stands for noun i.e. a person or a thing.
This mini definition on one hand associates the term *father* to its meaning inside the field of *family*
and separates it from other fields like *religion*, where *father* would refer to a 'male priest'.

## Parts of speech

- `a`: adjective i.e. a property or a quality
- `adv`: adverb or adverbial
- `clf`: classifier
- `cnj`: conjunction
- `int`: interjection
- `num`: numeral i.e. a quantity
- `n`: noun i.e. a thing or a person
- `pp`: preposition or postposition
- `pro`: pronoun
- `ptcl`: particle
- `r`: (only in PWN concpets) adverb or adverbial
- `s`: (only in PWN concpets) adjective
- `v`: verb i.e. an action or a process
