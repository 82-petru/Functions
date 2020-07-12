# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 20:27:40 2019

@author: petru
"""
def f(x):
    return x ** 3

def g(y):
    return y ** 4

def total(x, y):
    return (f(x) + g(y))
print(total(2, 3))