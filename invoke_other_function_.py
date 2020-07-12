# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 20:52:04 2019

@author: petru
"""
'''A function returning a string and using a local variable'''

def lastFirst(firstName, lastName):
    separator = ', '
    result = lastName + separator + firstName
    return result

print(lastFirst('Benjamin', 'Franklin'))
print(lastFirst('Andrew', 'Harrington'))
#''User input supplies function parameter'''
def happy(person):
    print("Happy Birthday to you!")
    print("Happy Birthday, dear " + person + ".")
    
def main():
  userName = input("Enter the Birthday person's name: ")
  happy(userName)
main()


'''Display any number of sum problems with a function.
Handle keyboard input separately.
'''

def sumProblem(x, y):
    sum = x + y
    sentence = 'The sum of {} and {} is {}.'.format(x, y, sum)
    print(sentence)

def main():
    sumProblem(2, 3)
    sumProblem(1234567890123, 535790269358)
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    sumProblem(a, b)

main() 

'''A simple function returning a value, used in an expression'''

def f(x):
    return x*x

print(f(3))
print(f(3) + f(4)) 

'''Display a sum problems with a function returning a string,
not printing directly.
'''

def sumProblemString(x, y):
    sum = x + y
    return 'The sum of {} and {} is {}.'.format(x, y, sum)

def main():
    print(sumProblemString(2, 3))
    print(sumProblemString(1234567890123, 535790269358))
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    print(sumProblemString(a, b))

main() 

def test():
   print("test was invoked")

def invoker(func):
   func()

invoker(test)  # prints test was invoked