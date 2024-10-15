# Contents of Panlexia

## Language-specific word lists

Language-specific word list files consist in minimum of the following three columns.

1. `id`: The Panlexia concept identifier that links definitions and words and in different languages together.
   Fields in this column shall never be empty.
2. `num`: The number of the translation as a simple numeral, like `1`, `2`, `3`, `4`, etc.
   An empty value means the same as `1`.
3. `word`: The word or phrase in the current language that expresses the meaning of the concept.
   Fields in this column shall never be empty.

Below is an excerpt of a minimal word list file for the Esperanto language in table format.

| id                 | num | word               |
|--------------------|-----|--------------------|
| Family:father.N    | 1   | patro              |
| Family:father.N    | 2   | paĉjo              |
| Family:mother.N    | 1   | patrino            |
| Family:mother.N    | 2   | panjo              |
| People:man.N       |     | viro               |
| People:woman.N     |     | virino             |

Word list files may include also some or all of the following additional columns.

- `transcription`: Transcription of the contents of the `word` field in the standard Romanization system,
   such as Pinyin for Mandarin Chinese.
- `pronunciation`: Pronunciation of the contents of the `word` field in the International Phonetic Alphabet (IPA).
- `grammar`: Grammatical information about the word.
   For example, nouns may be marked `F` (feminine), `M` (masculine) or `N` (neuter) in languages that have grammatical gender.
- `style`: The sociolinguistic style of the word when it's other than neutral.
   This field may contain markers like `D` (dialectal), `V` (vulgar) and `T` (technical).
- `etymology`: The origin of the word in case it is a (recent) loanword.
   This field may consist of a 3-letter ISO language code, a colon (`:`), the word in the original language and its pronunciation inside parentheses.

Any fields in the additional columns may be empty.
For example, most fields in the `style` column would probably be empty
because most words belong to the neutral style in every language.
