# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 14:51:50 2020

@author: petru
"""
def add_greetings(names):
  greeting = []
  for item in names:
    greeting.append("Hello, " + item)
  return greeting
  

#
print(add_greetings(["Owen", "Max", "Sophie"]))
    
#functie in care sa selectezi odd indexes from a list 
def odd_indices(lst):
  odd_list = []
  count = 0
  for item in lst:
    if count % 2 != 0:
      odd_list.append(item)
    count += 1
  return odd_list

print(odd_indices([4, 3, 7, 10, 11, -2]))
   
#aceeasi functie dar alta modalitate de a selecta odd indexes
def odd_indices(lst):
  for item in lst:
    return lst[1::2]

print(odd_indices([4, 3, 7, 10, 11, -2]))

#list comprehensions alta modalitate de a selecta odd indexes
#how it works? one indices is selected the other one is skiped 
L = [4, 3, 7, 10, 11, -2]
odd_numbers = [y for x,y in enumerate(L) if x % 2 != 0]
print(odd_numbers)
#access index and items 
ints = [8, 23, 45, 12, 78]
for idx, val in enumerate(ints):
    print(idx, val)
print("")  
#access index and items
for index in range(len(L)):
    print(index, L[index])

print("")
#Write your function here
def exponents(bases, power):
  total = []
  for items in bases:
    for i in power:
      total.append(items ** i)
  return total

#Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))

def larger_sum(lst1, lst2):
    
    if sum(lst1) > sum(lst2):
        return sum(lst1)
    elif sum(lst1) < sum(lst2):
        return sum(lst2)
    else:
        return sum(lst1)
print(larger_sum([1, 9, 5], [2, 3, 7]))      
    
def larger_sums(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for i in lst1:
        sum1 += i
    for j in lst2:
        sum2 += j
    if sum1 > sum2:
        return lst1 
    elif sum1 < sum2:
        return lst2
    else:
        return lst1
    
print(larger_sums([1, 9, 5], [2, 3, 7]))
#same values of two lists, with indices similar values 
def sam_values(lst1, lst2):
  indices = []
  for i in range(len(lst1)):
      if lst1[i] == lst2[i]:
          indices.append(i)
  return indices
#Uncomment the line below when your function is done
print(sam_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))

#  asemanatoare cu cea de susu dar am folosit list comprehensions
def sames_values(lst1, lst2):
    return [i for i in range(len(lst1)) if lst1[i] == lst2[i]]
print(sames_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))


def contains(big_string, little_string):
  if little_string in big_string:
    return True 
  else:
    return False
print(contains("watermelon", "melon"))
print(contains("watermelon", "berry"))

def common_letters(string_one, string_two):
  count = []
  for i in string_one:
      if i in string_two:
        if i not in count:
          count.append(i)  
  return count 
print(common_letters("manhattan", "san francisco"))  
  