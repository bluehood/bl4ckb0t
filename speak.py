# -*- coding: utf-8 -*-
import numpy as np
from scipy.stats import rv_discrete


def produce_sentence():
    # load person's beginnigs, ends, and pairs of words
    begs = np.loadtxt("words_db/beginnings", dtype=("S20, f8"))
    ends = np.loadtxt("words_db/ends", usecols=(1,), dtype=str)
    # we want an np.array of these for performance reasons, but this means
    # we have to keep all data as strings
    pairs = np.loadtxt("words_db/pairs", dtype=str)

    # choose a beginning
    whichbeg = rv_discrete(values=(range(begs.size), [ v[1] for v in begs ]))
    sentence = [ begs[whichbeg.rvs()][0], ]
    word = sentence[-1]

    # create rest of the sentence
    # if sentence reaches 15 words length, just stop
    while len(sentence) < 15:
        # if we don't know how to go on from that word,
        # it's a good point to stop
        while not word in pairs[:,0]:
            sentence[-1] += '.'
            word = begs[whichbeg.rvs()][0]
            sentence += (word,)

        # wpairs only contains pairs starting with word
        wpairs = pairs[pairs[:,0]==word]
        # create random discrete variable with weights == wpairs[:,2]
        values = (range(wpairs.shape[0]), [float(x) for x in wpairs[:,2]])
        whichword = rv_discrete(values=values)
        # choose word using random discrete variable
        word = wpairs[whichword.rvs(), 1]
        # add word to sentence
        sentence += (word,)
        
        # when sentence is more than 5 words long, stop at next end word
        if len(sentence) > 5 and word in ends:
            break

    return ' '.join(sentence)+'.'
