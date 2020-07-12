# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 09:15:31 2019

@author: petru
"""
def median(lists):
    s= sorted(lists)
    n = len(s)
    m = n // 2
    if n % 2 == 0:
        even_m = (s[m] + s[m - 1]) / 2.0
        return even_m
    elif n == 1:
        return s[0]
    else:
        even = s[m]
        return even 
text = [10, 2, 11, 16, 8, 9]
text1 = [ 41, 94, 38, 76, 59, 25, 19, 63, 81 ]
print(sorted(text))
print(median(text))
print(sorted(text1))    
print(median(text1))       
        
        
def median(lists):
    sort = sorted(lists)
    length = len(sort)
    med = length // 2
    if length % 2 == 0:
        avg = (sort[med] + sort[med - 1]) / 2.0
        return avg
    elif length == 1:
       return sort[0]
    else:
       avege = sort[med]
       return avege
text = [ 1, 9, 6, 2, 7, 3, 34, 87]
print(median(text))
print(sorted(text))           