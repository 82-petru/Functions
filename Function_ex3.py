# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 18:20:56 2019

@author: petru
"""
import numpy as np
"""sentence = "All good things come to those who wait."

def break_words(stuff):
    words = stuff.split(' ')
    return words
print(break_words(sentence))

def sort_words(words):
    return sorted(words)
print(sort_words(sentence))

def print_first_word(words):
#Prints the first word after popping it off.
    word = words.pop(0)
    print(word)
who = break_words(sentence)    
print_first_word(who)

def print_last_word(words):
# Prints the last word after popping it off.
    word = words.pop(-1)
    print(word)
who = break_words(sentence)    
print_last_word(who)    
    
def sort_sentence(sentance):
#Takes in a full sentence and returns the sorted words.
    words = break_words(sentence)
    return sort_words(words)
print(sort_sentence(sentence))"""



global_list = 0.048

def defineAList():
    local_list = np.random.normal(0.095, 0.014, 20)
    print("For checking purposes: in defineAList, list is", local_list) 
    return local_list 

def useTheList(passed_list):
    print("For checking purposes: in useTheList, list is", passed_list)

def main():
    l = defineAList()
    useTheList(l)
    
    
def first_three_multiples(num):
  print(num)
  print(num*2)
  print(num*3)
  return num*3

first_three_multiples(2)  
first_three_multiples(4)    
first_three_multiples(6)
     
