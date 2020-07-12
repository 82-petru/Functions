# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 11:48:33 2019

@author: petru
"""

def product(prod):
    total = 1
    for item in prod:
        total = total * item
    return total
print(product([3, 4, 5]))
        