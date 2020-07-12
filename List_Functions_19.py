# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 21:00:58 2019

@author: petru
"""

n = [1, 3, 5, 16, 8, 9, 11]
print(n)
#print first element from the list 
print(n[1])
# multiply the second element of the n list by 5
n[1] = n[1] * 5
n.append(4)
n.pop(2) #will remove index mentioned in brakets, just one item
n.remove(15) #will remove 'item' from list if will find it 
del(n[4]) #is like .pop in that it will remove the item at the given index, but it won’t return it:
print(n)

#Example with 2 parameters 
m = 6 
n = 8 
def funct(x, y):
    return x + y 
print(funct(m, n))

#Example with string 
n = 'Hello'
def string(s):
    return s + ' world'
print(string(n))

#You pass a list to a function the same way you pass any other argument to a function.
#print item from a list , remove print operator otherwise shows 'none'
def list(item):
    print(item[0])
n = [3, 5, 8]
list(n)
# other posibility with return operator but have to use print, too
def list(item):
    return item[1]
    
n = [3, 5, 8]
print(list(n))

#modifying an item into the list 
def list(item):
    n[0] = n[0] * 2
    return item[0]
    
n = [3, 5, 8]
print(list(n))
#append function
n = [3, 5, 8]
n.append(11)
def list(item):
    n[0] = n[0] * 2
    return item[0]

print(list(n))
print(n)
#
n = [3, 5, 7]
# functie cu folosirea loop for si functia range 
def print_list(x):
  for i in range(0, len(x)):
    print(x[i])
    
print_list(n)

#un exemplu cu strings 
n = ['danemarca', 'anglia', 'belgia']

def listos(x):
    for i in range(0, len(x)):
        print(x[i])
listos(n)


def lisk(y):
    return y
print(lisk(range(5)))

for r in range(0, 61, 1):#printing all odd numbers 
    print(r, end=', ')# ca sa afiseze in linie dupa loop de for

#nice example 
sampleList = [3, 6, 9, 12, 15]
for i in range(len(sampleList)):
    print( "Element Index[", i, "]", "Previous Value ", sampleList[i], "Now ", sampleList[i] * 2)

for i in range(0, 19, 1):

  print(i, end= ',')

#Iterating over a list in a function
  
 #Method 1 - for item in list:
#for item in list:
 #print item
 #Method 1 is useful to loop through the list, but it’s not possible to modify the list this way.
#Method 2 - iterate through indexes:
#for i in range(len(list)):
 # print list[i]
#Method 2 uses indexes to loop through the list, making it possible to also modify the list if needed

