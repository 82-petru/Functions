# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 13:45:56 2019

@author: petru
"""
import math 

def strin(n):
    n = str(n)
    total = 0
    for elem in n:
      total += int(elem)
    print(total)
strin(12345)

total = 0
x = 123456789
while x > 0:
    total += x % 10
    x //= 10

    
print (total)

def factorial(y):
    total = 1
    for t in range(1, y +1):
        total *= t    
    print(total)
factorial(5)

def is_prime(z):
    if z < 2:
        return False
    if z == 2:
        return True
    for p in range(2, z-1):
        if z % p == 0:
            return False
    else:
        return True
print(is_prime(11))


def reverse(punte):
  total = ""
  for i in punte:
    total = i + total
  return total
print(reverse("string"))
    
def anti_vowel(text):
    total = ''
    vowels = "AEIOUaeiou"
    for v in text:
      if v not in vowels:
          total += v
    return total
print(anti_vowel("Hello World, i am home"))

def anti_vowel(text):
    total = ''
    for item in text:
        if item not in "AEIOUaeiou":
            total += item
    return total
print(anti_vowel("Hello World, i am home"))


score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
def function(text):
  total = 0
  lower = text.lower()
  for i in lower:
      total += score[i]
  return total
print(function("Deviatie"))

def count(sequence, item):
    total = 0 
    for item in sequence:
        total += item 
    return total
print(count([1, 2, 3, 1, 1, 2, 5, 6], 1))
    
def remove_duplicates(double):
     total = []
     for i in range(len(double)):
         if double[i] not in total:
            total.append(double[i])
     return total
print(remove_duplicates([1, 2, 3, 1, 1, 2, 5, 6, 7, 5, 4, 2,]))

print("end")
def median(mid):
    total = 0
    sort = sorted(mid)
    print(sort)
    length = len(sort)
    h = length // 2
    print(h)
    for i in sort:
      #print(i)
      #print(total)
        if length % 2 == 0:
           total += (sort[h - 1] + sort[h]) / 2.0
           return total 
        else:
           total += sort[h]
           return total 
a = [11, 4, 6, 5, 8, 1, 12, 17]
t = [11, 4, 6, 5, 8, 1, 12, 17, 34]
print(median(a))
print(median(t))


