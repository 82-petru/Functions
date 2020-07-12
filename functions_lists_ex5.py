# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 18:20:56 2019

@author: petru
"""
def function(a,b):
    if a > b:
        y = "this is first string"
        x = "this is the second string"
    print(x)
    print(y)
function(9, 7)    

def function2(num1, num2):
    sum_num = num1 + num2 
    if 10 <= sum_num >= 10:
        return True
    else:
        return False
print(function2(9, -1))
print(function2(9, 1))

print(list(range(0, 4)))

list1 = ['a', 'b', 'c', 'd', 'e']

print(list1[-1])

#double the index
def double_index(lst, index):
  if index >= len(lst):
    return lst
  else:
    lst[index] = lst[index] * index
    return lst
#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))

#Write your function here remove middle
def remove_middle(lst, start, end):
  lst_start = lst[: start]
  lst_end = lst[end +1 :]
  new_lst = lst_start + lst_end
  return new_lst
#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

#middle item
def middle_element(lst):
  if len(lst) % 2 != 0:
    lst = lst[len(lst) // 2]
    return lst
  else:
    lst1 = lst[(len(lst) // 2) - 1]
    list2 = lst[(len(lst) // 2)]
    new_lst = (lst1 + list2) / 2
    return new_lst
#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))

#Write your function here mmore frequent item
def more_frequent_item(lst, item1, item2):
  count_item1 = lst.count(item1)
  count_item2 = lst.count(item2)
  if  count_item1 > count_item2:
    return item1 
  elif count_item1 < count_item2:
    return item2
  else:
    return item1
  
#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

#Write your function here more than n
def more_than_n(lst,item,n):
  count_list = lst.count(item)
  if count_list > n:
    return True
  else:
    return False 
  
#Write your function here_append sum
def append_sum(lst):
  new_lst = lst[-2:]
  lst.append(sum(new_lst))
  new_lst = lst[-2:]
  lst.append(sum(new_lst))
  new_lst = lst[-2:]
  lst.append(sum(new_lst))
  return lst
#Uncomment the line below when your function is done
print(append_sum([1, 1, 2])