# -*- coding: utf-8 -*-
"""
Your task is to create a function that can take any string and randomly jumble the 
 within each word while leaving the first and last letters of the word in place.


"""
from random import shuffle

def shuffle_word(word):
    word = word.group()
    middle = list(word[1:-1])
    shuffle(middle)
    return word[:1] + ''.join(middle) + word[-1]
    
def mix_words(string):
    import re
    return re.sub(ur'\w{4,}', shuffle_word, string)
    
print mix_words("Hello, gooytryd world!")