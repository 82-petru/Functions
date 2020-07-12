# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 20:52:04 2019

@author: petru
"""
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
  count = 0
  for letter in letters:
    if letter in word:
      count += 1
  return count
# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4


