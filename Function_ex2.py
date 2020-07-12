# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 20:52:04 2019

@author: petru
"""
def break_words(stuff):# def 1 break up words for us and create a list 
    word = stuff.split()
    return word 

def sort_words(words):# def 2 sorts the elemnets inside a list tulip in sorted manner(ordina alfabetica)
    return sorted(words)

def print_first_word(words): #def 3 displays the first word from def 1 output and popp it off from list
    word = words.pop(0)
    print(word)
  


def print_last_word(words):# def 3 displays the last word from def 1 output and popp it off from list
     word = words.pop(-1)
     print(word)
     
def sort_sentence(sentence): # def 5 returns the sorted words from def 2
    words = break_words(sentence)
    return sort_words(words)

def print_first_last(sentence):# def 6 prints output of def 1 
    words = break_words(sentence)#use list of strings from def 1 
    print_first_word(words)
    print_last_word(words)
    
def print_first_last_sorted(sentence):#def 7 prints output of def 2
    words = sort_sentence(sentence)# use list of string from def 2
    print_first_word(words)
    print_last_word(words)

#ce-am observat este ca daca pui rezultatul unei functii sub alta functie va afisa rezultatul lor
  


