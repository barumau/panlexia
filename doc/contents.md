# Contents of Panlexia

## Directory structure

The overall directory structure of the Panlexia repository is shown below.
Only 1–3 files are listed per directory for brevity.

    panlexia/
    ├─ doc/
    │  ├─ index.md
    │  ├─ id.md
    │  └─ ...
    ├─ data/
    │  ├─ Concepticon/
    │  ├─ NorthEuraLex/
    │  ├─ ULD/
    │  ├─ WOLD/
    │  └─ master.tsv
    ├─ dict/
    │  ├─ definition
    │  │  └─ eng-definition.tsv
    │  ├─ A
    │  │  ├─ abk.tsv
    │  │  └─ ...
    │  ├─ ...
    │  └─ Z
    │     ├─ zul.tsv
    │     └─ ...
    ├─ src/
    │  ├─ create_initial_ids_and_definitions.py
    │  ├─ generate_pdf_dictionary.sh
    │  └─ ...
    ├─ LICENSE.md
    └─ README.md
 
- `data`: Files for creating first Panlexia dictionaries from external sources, like Concepticon, NorthEuraLex, WOLD and ULD.
- `doc`: Documentation about structure, contents and use of Panlexia.
- `dict`: Dictionary files for all languages.
    - The dictionaries are filed to subdirectories by their first letter.
    - Filename is either a 3-letter language code from the *ISO 639-3* standard
      or, in case the language code is missing, the full name of the languages in lowercase Basic Latin letters.
- `src`: Source code for programs for processing Panlexia data.

## Language-specific word lists

Language-specific word list files are located in the `dict` directory.
They consist in minimum of the following three columns.

1. `id`: The Panlexia concept identifier that links definitions and words and in different languages together.
   Fields in this column shall never be empty.
2. `word`: The word or phrase in the current language that expresses the meaning of the concept.
   Fields in this column shall never be empty.

Below is an excerpt of a minimal word list file for the English language.

    id                 word
    PWN:father.n.01    father
    PWN:father.n.01    dad
    PWN:mother.n.01    mother
    PWN:mother.n.01    mum
    PWN:man.n.01       man
    PWN:woman.n.01     woman

Word list files may include also some or all of the following additional columns.

- `style`: The sociolinguistic style of the word when it's other than neutral.
   This field may contain markers like `dial.` (dialectal), `fig.` (figurative), `inf.` (informal), and `spec.` (specialist or technical language).
- `transcription`: Transcription of the contents of the `word` field in the standard Romanization system,
   such as Pinyin for Mandarin Chinese.
- `pronunciation`: Pronunciation of the contents of the `word` field in the International Phonetic Alphabet (IPA).
- `grammar`: Grammatical information about the word.
   For example, nouns may be marked `F` (feminine), `M` (masculine) or `N` (neuter) in languages that have grammatical gender.
- `morphology`: The structure of the word analyzed into morphemes.
   An empty field means that the word consist of one unanalyzable part.
- `etymology`: The origin of the word in case it is a (recent) loanword.
   This field may consist of a 3-letter ISO language code, a colon (`:`), the word in the original language and its pronunciation inside parentheses.

Any fields in the additional columns may be empty.
For example, most fields in the `style` column would probably be empty
because most words belong to the neutral style in every language.
The English word list above would become more informative with the addition of the `style` information.

    id                 style       word
    PWN:father.n.01                father
    PWN:father.n.01    inf.        dad
    PWN:mother.n.01                mother
    PWN:mother.n.01    inf.        mum
    PWN:man.n.01                   man
    PWN:woman.n.01                 woman

### Style

Style labels indicate the context in which the word is normally used.

- *appr.* – Approving expressions show that you feel approval or admiration.
- *arch.* – Archaic or antiquated words that are no longer in ordinary use.
- *dial.* – Dialectal expressions are mainly used in particular regions.
- *disappr.* – Disapproving expressions show that you feel disapproval or contempt.
- *fig.* – Figurative language is used in a non-literal or metaphorical way.
- *form.* – Formal expressions are usually only used in serious or official language and would not be appropriate in normal everyday conversation.
- *hum.* - Humorous expressions are intended to be funny.
- *inf.* – Informal expressions are used between friends or in a relaxed or unofficial situation. They are not appropriate for formal situations.
- *lit.* – Literary language is used mainly in literature, like in poems and novels.
- *off.* – Offensive expressions refer to people in a way that is very insulting, especially in connection with their race, religion, sex or disabilities.
- *sl.* – Slang is language that is unique to people who share the same interests or belong to the same social group.
- *spec.* – Specialist language is used by people who specialize in particular subject areas.
- *taboo* – Taboo expressions are likely to be thought by many people to be shocking and not to be used.
