# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 18:45:26 2019

@author: petru
"""

def anti_vowel(text):
  vowels = ('aeiouAEIOU')
  fl = []
  for i in text:
      if i not in vowels:
          fl.append(i)
  return "" .join(fl)

text = "GeeksforGeeks - A Computer Science Portal for Geeks"
print(anti_vowel(text))
