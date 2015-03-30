"""
filename:       levenshtein.py
description:    Computes the Levenshtein Distance between 2 strings.
version:        0.1
author:         Matthew Mayo <mayo_matthew@columbusstate.edu>
modified:       2015-03-27
"""

# Compute Levenshtein distance between 2 strings
def lev(word1, word2):

    if len(word2) == 0:
        return len(word1)

    if len(word1) < len(word2):
        return lev(word2, word1)

    prev = range(len(word2) + 1)

    for i, c1 in enumerate(word1):
        this = [i + 1]

        for j, c2 in enumerate(word2):
            ins = prev[j + 1] + 1
            dels = this[j] + 1
            subs = prev[j] + (c1 != c2)
            this.append(min(ins, dels, subs))

        prev = this

    return prev[-1]
