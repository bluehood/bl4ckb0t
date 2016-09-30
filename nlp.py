# -*- coding: utf-8 -*-
import numpy as np
from random import random as rand


nouns = np.loadtxt('words_db/nouns', dtype=str, delimiter='#')
verbs = np.loadtxt('words_db/verbs_c', dtype=str, delimiter='#')
dets = np.loadtxt('words_db/determiners', dtype=str, delimiter='#')


def build_structure():
    if rand() < 0.5:
        return [verb_phrase(), pred_phrase()]
    else:
        return [noun_phrase(), verb_phrase(), pred_phrase()] 

def noun_phrase():
    if rand() < 0.5:
        return ['N']
    else:
        return ['D', 'N']

def verb_phrase():
    if rand() < 0.5:
        return ['V']
    else:
        return ['V', noun_phrase()]

def pred_phrase():
    return ['P', noun_phrase()]


if __name__ == '__main__':
    print build_structure()
