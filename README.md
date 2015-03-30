## Levenshtein Lexical Similarity

### Introduction

*Note: This is not a scientific study*

This project attempts to measure [lexical similarity](http://en.wikipedia.org/wiki/Lexical_similarity) using [Levenshtein Distance](http://en.wikipedia.org/wiki/Levenshtein_distance) as a comparative metric. A group of [the most commonly-used English words](http://en.wikipedia.org/wiki/Most_common_words_in_English), according to Wikipedia, are cross-compared with translations of these words in multiple languages, with the mean of the means between 4 Germanic (English, German, Dutch, Afrikaans) and 4 Romance (Spanish, Portuguese, Italian, French) languages compared to determine which group is more lexically similar than the other.

### Description

The project includes:

```
common_words.py
```
This script uses the [google-translate-python](https://github.com/terryyin/google-translate-python) module to attain translations of the 100 most common English words. Of course there are all sorts of potential problems with both this list and using this list as a basis for lexical similarity measurements, but we intentionally overlook these. The target languages that translations are made for are stored by their 2-letter international language codes, one per line, in the lang_codes file. The resulting translations of the common words are saved in the /corpus directory in files with names matching their 2-letter international language codes.

```
score_corpus.py
```
This script then cross-compares the Levenshtein scores of each word of each pair of languages in the 2 categories (Germanic, Romance), finds the mean of each pair of languages comparisons, and then compares the means of the 2 language groups to one another to find which group is more similar (the lower the score, the greater the similarities).

```
levenshtein.py
```
This contains the Levenshtein Distance function used by the score_corpus script.

### Results

![Results](https://raw.githubusercontent.com/mmmayo13/levenshtein-lexical-similarity/master/results.gif)

In the case of this experiment, the Germanic languages scored a mean of means of 3.33, while the Romance languages scored a mean of means of 3.01166666667. The lower the score, the better, meaning that this result can be interpreted as the selected 4 Romance languages being more lexically similar than the 4 chosen Germanic languages.

### Usage

To replicate the experiment outlined above, simply execute the scripts in the order above. To do something different, modify the scripts as desired and execute.

### Requirements

This project is written in Python, and requires a Python installation. Tested with Python 2.7.6.

### Installation

Simply clone or download the scripts and execute.

### Author

[Matt Mayo](http://about.me/mattmayo)

### License

This software is made available under the [MIT License](http://choosealicense.com/licenses/mit/)
