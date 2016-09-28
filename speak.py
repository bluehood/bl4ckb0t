# -*- coding: utf-8 -*-
import numpy as np


def produce_sentence():
    # load beginnigs, ends, and pairs of words
    begs = np.loadtxt('words_db/beginnings', dtype=[('w','S20'), ('p','f8')])
    ends = np.loadtxt('words_db/ends', usecols=(0,), dtype=str)
    pairs = np.loadtxt('words_db/pairs',
                       dtype=[('w1', 'S20'), ('w2', 'S20'), ('p','f8')])

    # normalise probabilities
    begs['p'] /= begs['p'].sum()

    # choose a beginning and start sentence
    word = np.random.choice(begs['w'], p=begs['p'])
    sentence = [word]

    # create rest of the sentence
    # if sentence reaches 15 words length, just stop
    while len(sentence) < 15 or word not in ends:
        while word not in pairs['w1']:
            # cannot continue from here. let's start again
            sentence[-1] += '.'
            word = np.random.choice(begs['w'], p=begs['p'])
            sentence.append(word)

        # add word to sentence
        tmp_pairs = pairs[pairs['w1'] == word]
        norm_probs = tmp_pairs['p'] / tmp_pairs['p'].sum()
        word = np.random.choice(tmp_pairs['w2'], p=norm_probs)
        sentence.append(word)

    return ' '.join(sentence) + '.'


if __name__ == "__main__":
    print produce_sentence()
