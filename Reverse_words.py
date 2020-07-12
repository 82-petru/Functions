# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 20:36:27 2019

@author: petru
"""

def reverse(text):
    word = []
    l = len(text) 
    while l > 0:
        word.append(l)
        l -= 1
    return word
  
print(reverse([1, 2, 3, 4, 5]))