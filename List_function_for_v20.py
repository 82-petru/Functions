# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 20:35:40 2019

@author: petru
"""


#prima varianta face suma item-uri din lista
n = [3, 5, 7]
def total(numbers):
    result = 0 
    for i in range(0, len(numbers)):
     result += numbers[i]
    return result
print(total(n))

# a doua varianta afiseaza primu item din lista
n = [3, 5, 7]
def total(numbers):
    for i in range(0, len(numbers)):
      return numbers[i]
print(total(n))

item = [1, 2, 4, 6, 7, 11]
def astazi(num):
    for i in range(0, len(num)):
        return num[i]
print(astazi(item))
    

n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(words):
  result = ""
  for i in words:
   result += i#intendentation error return si for pe aceeasi linie result trebuie sa fie sub for.
   #eroarea consta ca iti afiseaza doar primul item din lista 
  return result 

print(join_strings(n))

a = [1, 2, 3]
b = [4, 5, 6]
def join_list(x, y):
    return x + y
print(join_list(a, b))
#create a list which contans 2 items and each item is  a sublist 
list_of_lists = [[1, 2, 3], [4, 5, 6]]

for lst in list_of_lists:#iterate through our outer list
    for item in lst:#For each of the two inner lists (as lst), we iterate through the numbers (as item)
      print(item)

#Exemplu 
      n1 = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten(lists):
  result = []
  for numbers in lists:
    for item in numbers:
      result.append(item)
  return result #itendation of the return be equal with first iteration
         
print(flatten(n1))#TypeError: 'int' object is not iterable



