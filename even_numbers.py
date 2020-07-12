# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 11:23:34 2019

@author: petru
"""

def purify(lists):
    total = []
    for item in lists:
        if item % 2 == 0:
            total.append(item)
    return total
print(purify([7, 2, 3, 4]))