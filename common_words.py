"""
filename:       common_words.py
description:    Builds lists of common words in multiple languages.
version:        0.1
author:         Matthew Mayo <mayo_matthew@columbusstate.edu>
modified:       2015-03-27
notes:          http://en.wikipedia.org/wiki/Most_common_words_in_English
                https://github.com/terryyin/google-translate-python
"""

from translate import Translator

# Build list of common words in multiple languages
def build_corpus():

    # List of most common English words from file
    with open("corpus/en") as f:
        common_en = f.read().splitlines()

    # List of language codes from file
    with open("lang_codes") as f:
        lang_codes = f.read().splitlines()

    # Translations matrix
    all_langs = []

    # For each language code in lang_codes file...
    for lang_code in lang_codes:

        # This language's translations
        common_trans = []

        # Create a text file of translations
        outfile = "corpus/" + lang_code
        with open(outfile, "w") as f:

            # Translate the English words to this language
            translator = Translator(to_lang = lang_code)
            for word in common_en:
                translation = translator.translate(word)
                common_trans.append(translation)
                f.write(translation.encode('utf-8').strip())
                f.write("\n")

            # Testing
            print ', '.join(common_trans)

            # Add this language's list of translations to matrix
            all_langs.append(common_trans)


# Calls build_corpus, if file directly executed
def main():
    build_corpus()


main()
