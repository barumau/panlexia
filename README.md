# Panlexia

## Contents

Panlexia is a collection of interlinked word lists.
Each language has its own word list file.
The file names consist of a three-letter language code from the ISO 639-3 standard and `.tsv` suffix.
For example, the name of the word list file for English is `eng.tsv` and the one for Mandarin Chinese is `cmn.tsv`.

There can be also other language specific files for storing additional information,
for example phonetic transcription or grammatical information.
The name of a transcription file consists of the three-letter language code, a dash (`-`), the name of the transcription system, and `.tsv` suffix.
For example, the name of IPA pronunciation file for English is `eng-IPA.tsv`
and the name of Pinyin Romanized file for Mandarin Chinese is `cmn-pinyin.tsv`.

If for some reason there is two word lists for one language,
the second and greater ones are suffixed with an underscrore and a number.
For example, `eng_2.tsv` and `eng_2-IPA.tsv`.

Each word list file consists of lines that include an entry identifier, a tab (i.e. character tabulation) and a word or words in the given language.
The entry identifier is a unique code that consists of the following parts:

- the semantic field or theme in English
- a colon (`:`)
- the term in a standardized (scientific, technological or other) terminology or in plain English
- a period (`.`)
- a word class identifier, such as `N` for nouns, `ADJ` for adjectives and `V` for verbs

The word is the translation of the concept in the language in question.
The entry identifiers link translations in different languages together.

``` 
Animal:Felis catus.N cat
Animal:Canis lupus.N  wolf
Animal:Canis lupus familiaris.N dog
Body:head.N head
Body:face.N	face
Body:face.A facial
Food:Malus domestica.N  apple
Plant:Malus domestica.N apple tree
```

The repository includes also some Python and shell scripts for generating dictionaries.


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

Panlexia is maintained by **Risto Kupsala**.
You may contact him by sending email to risto@pandunia.info.

## Let's work together!

Panlexia is a collaborative project.
You can help in many ways!

- Improve the documentation.
   - Edit text so that it's easier to understand.
     The documentation is aimed for common people with a basic education.
 	 If you don't understand something, the problem is probably in the text, not in you!
   - Correct mistakes when you spot them.
- Translate the documentation to new languages.
- Add more words and translations!

The documentation is in plain-text in Markdown formatting.
Learn about Markdown [here](https://guides.github.com/features/mastering-markdown/).

You may contribute via GitHub.
Create an account for yourself and follow instructions about [cloning a repository](https://guides.github.com/activities/forking/) and [basic use](https://guides.github.com/activities/hello-world/).
If you contribute changes yourself, you will be added to our list of contributors automatically.

Our contributors are listed [here](https://github.com/barumau/panlexia/graphs/contributors)

If you have any questions, please contact us at our
[PhpBB discussion forum](https://pandunia.info/forum/viewforum.php?f=9&sid=73cace4ded824e36c4a05246a67273c6).
