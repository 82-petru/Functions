# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 19:20:37 2019

@author: petru
"""
# censor letter from a text 
def censor(text, word):
    leeds = '*' * len(word)
    variabila = text.split()
    count = 0 
    for item in variabila:
        if item == word:
            variabila[count] = leeds 
        count += 1          
    return ' ' .join(variabila)
print(censor("this is hack is wack hack", "hack"))
