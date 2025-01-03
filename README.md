# Panlexia

## Introduction

Panlexia is a **universal dictionary** for an unlimited number of languages
and including minority languages and constructed languages.
It links words from different languages together by using common concept definitions.

In the founding phase it collects together word lists from various free and open sources
(see the Acknowledgements chapter below).
Everybody is free to contribute in growing the dictionary
by adding new words, new concepts and even entire word lists in new languages to Panlexia.

## Organization

In practice, Panlexia is a collection of concept definition lists and word lists,
whose entries are linked together with concept identifiers or `id`s.
Each id identifies a unique concept, which is defined in a concept definition file.
The repository also includes programs that can be used to combine the data together into bilingual dictionaries.

Only some languages have a concept definition file.
The concept definitions in English are stored in the file [eng-definition.tsv](concepts/E/eng-definition.tsv).
All words in the word list files are based on the concepts.
So each word is a **label for a common concept** and not a translation from a word in another language.
This way the system avoids change and corruption of information that would happen
if the words were translated from language to language in a chain.

                    ┌──────────────────────────────────┐
                    │ File: eng-definition.tsv         │
                    ├──────────────────────────────────┤
                    │ id               Definition      │
                    │ ---------------  ------------    │
                    │ PWN:father.n.01  A male parent   │
                    │ PWN:mother.n.01  A female parent │
                    └──────────────────────────────────┘
                             ▲               ▲
                             │               │
                             │               │
    ┌───────────────────────────────┐  ┌──────────────────────────────┐
    │ File: eng.tsv                 │  │ File: fra.tsv                │
    ├───────────────────────────────┤  ├──────────────────────────────┤
    │ id              style  word   │  │ id              style  word  │
    │ --------------- ------ ------ │  │ --------------- ------ ----  │
    │ PWN:father.n.01        father │  │ PWN:father.n.01        père  │
    │ PWN:father.n.01  inf.  dad    │  │ PWN:father.n.01  inf.  papa  │
    │ PWN:mother.n.01        mother │  │ PWN:mother.n.01        mère  │
    │ PWN:mother.n.01  inf.  mum    │  │ PWN:mother.n.01  inf.  maman │
    └───────────────────────────────┘  └──────────────────────────────┘

## Word lists

Each language has its own word list file.
The file names consist of a three-letter language code from the ISO 639-3 standard and `.tsv` suffix.
For example, the name of the word list file for English is [eng.tsv](dict/E/eng.tsv),
and the one for French is [fra.tsv](dict/F/fra.tsv).

Each word list file contains a list of concept identifiers with associated words or "translations"
and optionally additional information, like how the word is pronounced

Each word list file consists in minimum of two columns separated by a tab: `id` and `word`.
The `id` column includes concept identifiers, and the `word` column includes words, whose meaning match the definition of the concept.
Below is a possible example of a word list file in French.
(For the real file, see <[dict/F/fra.tsv](dict/F/fra.tsv).)

    id                      word
    PLX:yes.ptcl            oui
    PWN:domestic_ass.n.01   âne
    PWN:drink.v.01          boire

## Concept ids

The [concept identifier](doc/id.md) is a unique code that consists of the following parts:

- the source of the concept, either `PWN` (Princeton Wordnet) or `PLX` (Panlexia)
- a colon (`:`)
- the term in English
- a period (`.`)
- a word class identifier, such as `n` for *noun*, `a` for *adjective* and `v` for *verb*
- (optional) another period (`.`)
- (optional) a unique number for identifiers that are otherwise identical

## Generating dictionaries from word lists

The concept identifiers link words in different languages together.
For example, the above word list in French could be combined with the below word list in English,
because they include same concepts.
(For the real file, see <[dict/E/eng.tsv](dict/E/eng.tsv).)

    id                      word
    PLX:yes.ptcl            yes
    PWN:domestic_ass.n.01   ass
    PWN:domestic_ass.n.01   donkey
    PWN:drink.v.01          drink

The combination can be done with [a Python program](src/generate_bilingual_dict.py) with the following command:  
`python3 src/generate_bilingual_dict.py eng fra`
It would produce the following result:

> # Français - English
>
> ## A
>
> **âne** *n* ① ass ② donkey
>
> ## B
>
> **boire** *v* drink
>
> ## O
>
> **oui** *ptcl* yes

In a Unix-like system you can generate dictionaries from one language (type `eng` for English) to all other languages with this shell script command:  
`sh generate_bilingual_dictionaries.sh eng`  
The generated dictionary files (in Markdown format) can be found inside the `generated` directory.

## License

The contents are free to be read, shared, printed, adapted and so on by Creative Commons license: Attribution 4.0 International (CC BY 4.0),
with the condition that you give appropriate credit and indicate if changes were made.
See examples of proper attribution below.

> Hypertext attribution:  
> "[Panlexia[(https://github.com/barumau/panlexia)" by Risto Kupsala et al. is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
>
> Text attribution:  
> "Panlexia" (https://github.com/barumau/panlexia) by Risto Kupsala et al. is licensed under Creative Commons Attribution 4.0 (https://creativecommons.org/licenses/by/4.0/)

Details of the license are in [LICENSE.md](LICENSE.md).

## Acknowledgments

The Panlexia project re-uses material from the following sources:

- [Concepticon](https://concepticon.clld.org/), which is  edited by
  List, Johann Mattis & Tjuka, Annika & van Zantwijk, Mathilda & Blum, Frederic & Ugarte, Carlos Barrientos & Rzymski, Christoph & Greenhill, Simon & Forkel, Robert
  and is licensed under a
  [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
- [NorthEuraLex](http://northeuralex.org/), which is edited by Johannes Dellert & Gerhard Jäger and which is licensed under the
  [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).
- Universal Language Dictionary (ULD) by Rick Harrison et al.
- [The World Loanword Database (WOLD)](https://wold.clld.org), which is edited by Martin Haspelmath & Uri Tadmor and which is licensed under the
  [Creative Commons Attribution 3.0 Germany License](http://creativecommons.org/licenses/by/3.0/de/)
- [Open Multilingual Wordnet](https://omwn.org/) by Francis Bond et al. which is licensed under the
  [MIT License](https://github.com/globalwordnet/OMW/blob/develop/LICENSE)

## Contact

Panlexia is maintained by **Risto Kupsala** from Oulu, Finland.
You may contact him by sending email to <risto@pandunia.info>.

## Let's work together!

Panlexia is a collaborative project.
You can help in many ways!

-   Improve the documentation.
    - Edit text so that it's easier to understand.
      The documentation is aimed for common people with a basic education.
      If you don't understand something, the problem is probably in the text, not in you!
    - Correct mistakes when you spot them.
-   Translate the documentation to new languages.
-   Add more words in the language of your choice!
-   Add new concepts.
-   Add a word list for a new language.

The documentation is in plain-text in Markdown formatting.
Learn about Markdown [here](https://guides.github.com/features/mastering-markdown/).

You may contribute via GitHub.
Create an account for yourself and follow instructions about [cloning a repository](https://guides.github.com/activities/forking/) and [basic use](https://guides.github.com/activities/hello-world/).
If you contribute changes yourself, you will be added to our list of contributors automatically.

Our contributors are listed [here](https://github.com/barumau/panlexia/graphs/contributors)

If you have any questions, please contact us at our
[PhpBB discussion forum](https://pandunia.info/forum/viewforum.php?f=9&sid=73cace4ded824e36c4a05246a67273c6).
