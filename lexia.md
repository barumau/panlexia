The lexia.csv in not valid by RFC 4180.

The following are the differences:

1. The first two lines are header lines and the values in the second are only series of dashes (-).
2. The values are seperated by pipes (|).

Here are descriptions of headers:

1. "lingue" - languages where the word is used
2. "morfeme" - morphemic structure of the word
3. "lexe" - word, phrase or affix
4. "klase" - grammatical category of the word
5. "tipe" - field of knowledge where the word belongs
6. "" - conventional symbols of referents (i.e. translations to scientific nomenclature).
7. "lexasle" - etymology of a word (syntax described below)
8. "eng" - translations to English
9. "deu" - translations to German
10. "fra" - translations to French
11. "spa" - translations to Spanish
12. "por" - translations to Portugese
13. "rus" - translations to Russian
14. "fas" - translations to Farsi/Persian
15. "hin" - translations to Hindi
16. "ben" - translations to Bengali
17. "tam" - translations to Tamil
18. "may" - translations to Malay (Malaysian and Indonesian)
19. "ara" - translations to Arabic
20. "tur" - translations to Turkish
21. "swa" - translations to Swahili
22. "hau" - translations to Hausa
23. "ful" - translations to Fula ~ Fulfulde ~ Pulaar
24. "zho" - translations to Mandarin Chinese
25. "yue" - translations to Cantonese Chinese
26. "jpn" - translations to Japanese
27. "kor" - translations to Korean
28. "vie" - translations to Vietnamese
29. "epo" - translations to Esperanto
30. "fin" - translations to Finnish
31. "pol" - translations to Polish

Each translation value can consist of more than one word or phrase. Additional translations are then surrounded by bracets and separated by comma and space (, ) sequence.

Syntax of "lexasle":

1. Each value contains zero or more language blocks.
2. If there are more than one language block, they are seperated by comma and space (, ) sequence.
3. Each language block starts with ISO 639-3 code and a colon (ex. "eng:").
4. Each language block contains one or more source words.
5. If there are more than one source words in a language block, they are seperated by comma and space (, ) sequence.

How to translate?

Open the file in your csv editor of choice and fill the gaps in a column that you are interested in based on values in other columns.
It is advised to used a spreadsheet editor, hide unuseful columns, and use filter function.
