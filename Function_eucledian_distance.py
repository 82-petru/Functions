# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 20:52:04 2019

@author: petru
"""
def euclidean_distance(pt1, pt2):
  distance = 0
  for point1 in range(len(pt1)):
      distance += (pt1[point1] - pt2[point1]) ** 2
      num = distance ** 0.5
  return num
print(euclidean_distance([1,2], [4,0]))
print(euclidean_distance([5,4,3], [1,7,9]))
