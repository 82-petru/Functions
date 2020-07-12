# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 09:15:31 2019

@author: petru
"""
a = "This is sparta but not romania"
print(a.count('i', 6))
print(type(a.count('i', 6)))

def count(sequence, item):
    total = 0 
    for c in sequence:
        if c == item:
          total += 1
    return total
print(count([1, 2, 3, 1, 1, 2, 5, 6], 1))

print('end')


def purify(high):
    total = []
    for i in high:
        if i % 2 == 0:
           total.append(i)
    return total
print(purify([1, 2, 3, 1, 1, 2, 5, 6]))

def purify(high):
    total = []
    for i in high:
        if i % 2 == 0:
           total += [i]
    return total
print(purify([1, 2, 3, 1, 1, 2, 5, 6]))


def product(lists):
    total = 1
    for p in lists:
        total *= p
    return total
print(product([1, 2, 3, 1, 1, 2, 5, 6]))

def remove_duplicates(double):
     total = []
     for i in range(len(double)):
         if double[i] not in total:
            total.append(double[i])
     return total
print(remove_duplicates([1, 2, 3, 1, 1, 2, 5, 6, 7, 5, 4, 2,]))    
         
         
         
double =[ 1, 2, 3, 1, 1, 2, 5, 6, 7, 5, 4, 2,]      
         
print(range(len(double)))
rang = range(len(double))        
print(range(0, 12))      
         
def try_to_modify(x, y, z):
    x += 23
    y.append(42)
    z += [99] # new reference
    print(x)
    print(y)
    print(z) 
a = 77    # immutable variable
b = [99]  # mutable variable
c = [28]
try_to_modify(a, b, c)     
print(a)
print(b)
print(c)     

print('end')

x = "Holberton"
y = "Holberton"
id(x)
id(y)
print(x is y)
print('end')

def f(n):
    n += [10]
d = [5, 6]
f(d)
print(d)
    
def updateNumber(n):
    print(id(n))
    n += 10
b = 5
print(id(b))                   # 10055680
updateNumber(b)                # 10055680
print(b)                       # 5    

def variable_args(*args, **kwargs):
     print('args is', args)
     print('kwargs is', kwargs)   
variable_args('one', 'two', 'three',1 ,[2], x=1, y=2, z=3)
#*args: any number of positional arguments packed into a tuple
#**kwargs: any number of keyword arguments packed into a dictionary

def remove_duplicates(double):
     total = []
     for i in range(len(double)):
         #print(i)
         print(double[i])
         print (total)
         if double[i] not in total: 
            total.append(double[i])
            
     return total
print(remove_duplicates([45, 23, 13, 34, 45, 13, 7, 23, 7, 5, 67, 34,]))  

