# -*- coding: utf-8 -*-


bhv = []


calling_out_testicles = {
    'trigger' : ('ho sbagliato', 'Ho sbagliato', 'Ah no', 'ah no'),
    'reply_type' : 'text',
    'reply': ('Sei un cogliooooone',)
}
bhv.append(calling_out_testicles)

no_give_gerry = {
    'trigger' : ('no dai', 'No dai', 'dai no', 'Dai no'),
    'reply_type' : 'text',
    'reply' : ('no dai geeeeerry', 'no dai gerry')
}
bhv.append(no_give_gerry)

strong_reaction = {
    'trigger' : ('no beh', 'No beh', 'forte', 'Forte', 'stefano', 'Stefano',
                 'stefy', 'Stefy', 'hamiltoniana', 'Hamiltoniana',
                 'autovalori'),
    'reply_type' : 'sticker',
    'reply' : ('BQADBAADhQADnWzWBjYVjZV8OT1cAg',
               'BQADBAADnwADnWzWBuBUlm_lDucyAg',
               'BQADBAADnQADnWzWBj6GAtyTZtebAg')
}
bhv.append(strong_reaction)

kids_and_apples = {
    'trigger' : ('oh raga', 'Oh raga'),
    'reply_type' : 'text',
    'reply' : ('oh vale passa il coltello', 'oh vale ce l\'hai una mela?',
               'oh raga, l\'altro giorno la vale mi fa "oh raga"',)
                        
}
bhv.append(kids_and_apples)

my_opinion = {
    'trigger' : ('alla fine', 'Alla fine', 'Secondo me', 'secondo me',),
    'reply_type' : 'text',
    'reply' : ('Secondo me è una cazzata', 'Aspeeeeeetta!? No è una cazzata',)

}
bhv.append(my_opinion)

about_einstein = {
    'trigger' : ('Einstein', 'einstein', 'Albert', 'albert', 'Tutto sommato', 'tutto sommato', '1921', '1974',),
    'reply_type' : 'text',
    'reply' : ('Tutto sommato Einstein era un coglione', 'Se posso fare un commento Einstein nel 1921 era già come Hawking dopo il 1974, conferenze, libri divulgativi, soldi droga e puttane',)

}
bhv.append(about_einstein)

about_hawking = {
    'trigger' : ('Hawking', 'hawking', 'Stephen', 'stephen', 'paraplegico', 'handicap',),
    'reply_type' : 'text',
    'reply' : ('Boh Hawking si sa che ormai è un coglione che dice cazzate', 'Hawking è un paraplegico di merda',)

}
bhv.append(about_hawking)

grandma_love = {
    'trigger' : ('Nonna', 'nonna', 'Conto', 'conto', 'calcolo', 'lo sa fare', 'difficile'),
    'reply_type' : 'text',
    'reply' : ('Dai raga questo conto lo sa fare anche mia nonna',)

}
bhv.append(grandma_love)


behaviours = tuple(bhv)
