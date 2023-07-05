# Panlexia

## Contents

Panlexia is a collection of interlinked word lists.
Each language has its own word list file.
The file names consist of a three-letter language code from the ISO 639-3 standard and `.txt` suffix.
For example, the name of the word list file for English is `eng.txt` and the one for Mandarin Chinese is `cmn.txt`.

There can be also other language specific files for storing additional information,
such as pronunciation instructions in the International Phonetic Alphabet (IPA) or other systems.
Names of such files consists of the three-letter language code, a dash (`-`), the name of the transcription system, and `.txt` suffix.
For example, the name of IPA pronunciation file for English is `eng-ipa.txt`
and the name of Pinyin Romanized file for Mandarin Chinese is `cmn-pinyin.txt`.

If for some reason there is two word lists for one language,
the second and greater ones are suffixed with a number.
For example, `eng-2.txt` and `eng-2-ipa.txt`.

Each word list file consists of lines that include an entry identifier, a column (`|`) and words in the given language.
The entry identifier is a unique code.
The words are the translation of the concept to a given language.
The entry identifiers link translations in different languages together.

    001001sp|I
    001001op|me
    001002sp|you, thou
    001002op|you, thee

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
