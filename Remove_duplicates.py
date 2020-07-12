# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 18:38:04 2019

@author: petru
"""

def remove_duplicates(double):
    total = []
    for item in double:
        if item not in total:
          total.append(item) 
    return total
print(remove_duplicates([1, 2, 3, 2, 4, 3]))
        
    