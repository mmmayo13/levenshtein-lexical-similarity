"""
filename:       score_corpus.py
description:    Generates Levenshtein Distance scores for all pairs of common
                word translations.
version:        0.1
author:         Matthew Mayo <mayo_matthew@columbusstate.edu>
modified:       2015-03-27
"""

from levenshtein import lev

# Score the Germanic languages
def germanic():

    # Levenshtein scores
    scores_en_de = []
    scores_en_nl = []
    scores_en_af = []
    scores_de_nl = []
    scores_de_af = []
    scores_nl_af = []

    # Score summation
    sum_en_de = 0
    sum_en_nl = 0
    sum_en_af = 0
    sum_de_nl = 0
    sum_de_af = 0
    sum_nl_af = 0

    # Read in corpuses
    with open("corpus/en") as f:
        en = f.read().decode('utf-8').splitlines()
    with open("corpus/de") as f:
        de = f.read().decode('utf-8').splitlines()
    with open("corpus/nl") as f:
        nl = f.read().decode('utf-8').splitlines()
    with open("corpus/af") as f:
        af = f.read().decode('utf-8').splitlines()

    # Generate Levenshtein scores
    for x in range(0, 100):
        scores_en_de.append(lev(en[x], de[x]))
        scores_en_nl.append(lev(en[x], nl[x]))
        scores_en_af.append(lev(en[x], af[x]))
        scores_de_nl.append(lev(de[x], nl[x]))
        scores_de_af.append(lev(de[x], af[x]))
        scores_nl_af.append(lev(nl[x], af[x]))

    # Score sums
    for x in range(0, 100):
        sum_en_de += scores_en_de[x]
        sum_en_nl += scores_en_nl[x]
        sum_en_af += scores_en_af[x]
        sum_de_nl += scores_de_nl[x]
        sum_de_af += scores_de_af[x]
        sum_nl_af += scores_nl_af[x]

    # Score means
    mean_en_de = sum_en_de / 100.0
    mean_en_nl = sum_en_nl / 100.0
    mean_en_af = sum_en_af / 100.0
    mean_de_nl = sum_de_nl / 100.0
    mean_de_af = sum_de_af / 100.0
    mean_nl_af = sum_nl_af / 100.0

    # Testing
    print "[EN, DE]", "\t", sum_en_de, "\t", mean_en_de
    print "[EN, NL]", "\t", sum_en_nl, "\t", mean_en_nl
    print "[EN, AF]", "\t", sum_en_af, "\t", mean_en_af
    print "[DE, NL]", "\t", sum_de_nl, "\t", mean_de_nl
    print "[DE, AF]", "\t", sum_de_af, "\t", mean_de_af
    print "[NL, AF]", "\t", sum_nl_af, "\t", mean_nl_af

    # Return the mean of the means
    mean_ger = (mean_en_de + mean_en_nl + mean_en_af + mean_de_nl
        + mean_de_af + mean_nl_af) / 6
    return mean_ger


# Score the Romance corpus languages
def romance():

    # Levenshtein scores
    scores_es_pt = []
    scores_es_it = []
    scores_es_fr = []
    scores_pt_it = []
    scores_pt_fr = []
    scores_it_fr = []

    # Score summation
    sum_es_pt = 0
    sum_es_it = 0
    sum_es_fr = 0
    sum_pt_it = 0
    sum_pt_fr = 0
    sum_it_fr = 0

    # Read in corpuses
    with open("corpus/es") as f:
        es = f.read().decode('utf-8').splitlines()
    with open("corpus/pt") as f:
        pt = f.read().decode('utf-8').splitlines()
    with open("corpus/it") as f:
        it = f.read().decode('utf-8').splitlines()
    with open("corpus/fr") as f:
        fr = f.read().decode('utf-8').splitlines()

    # Generate Levenshtein scores
    for x in range(0, 100):
        scores_es_pt.append(lev(es[x], pt[x]))
        scores_es_it.append(lev(es[x], it[x]))
        scores_es_fr.append(lev(es[x], fr[x]))
        scores_pt_it.append(lev(pt[x], it[x]))
        scores_pt_fr.append(lev(pt[x], fr[x]))
        scores_it_fr.append(lev(it[x], fr[x]))

    # Score sums
    for x in range(0, 100):
        sum_es_pt += scores_es_pt[x]
        sum_es_it += scores_es_it[x]
        sum_es_fr += scores_es_fr[x]
        sum_pt_it += scores_pt_it[x]
        sum_pt_fr += scores_pt_fr[x]
        sum_it_fr += scores_it_fr[x]

    # Score means
    mean_es_pt = sum_es_pt / 100.0
    mean_es_it = sum_es_it / 100.0
    mean_es_fr = sum_es_fr / 100.0
    mean_pt_it = sum_pt_it / 100.0
    mean_pt_fr = sum_pt_fr / 100.0
    mean_it_fr = sum_it_fr / 100.0

    # Testing
    print "[ES, PT]", "\t", sum_es_pt, "\t", mean_es_pt
    print "[ES, IT]", "\t", sum_es_it, "\t", mean_es_it
    print "[ES, FR]", "\t", sum_es_fr, "\t", mean_es_fr
    print "[PT, IT]", "\t", sum_pt_it, "\t", mean_pt_it
    print "[PT, FR]", "\t", sum_pt_fr, "\t", mean_pt_fr
    print "[IT, FR]", "\t", sum_it_fr, "\t", mean_it_fr

    # Return the mean of the means
    mean_rom = (mean_es_pt + mean_es_it + mean_es_fr + mean_pt_it
        + mean_pt_fr + mean_it_fr) / 6
    return mean_rom


# Scores the 2 separate clusters
def main():

    print "Langs\t\tTotal\tMean"
    print "=====\t\t=====\t===="

    mean_ger = germanic()
    mean_rom = romance()

    print "Germanic mean of means: ", mean_ger
    print "Romance mean of means: ", mean_rom


main()
