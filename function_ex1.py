# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 17:56:30 2019

@author: petru
"""
#playing wit return functions
print("...........")
print("Let's practice everything")

def function(start_point): 
    jelly = start_point + 400 #variables are temporary inside the  function
    hinge = jelly - 235
    grows = hinge - 678
    return jelly, hinge, grows

start_points = 1000 
beans, hinge, grows = function(start_points)

print("Let be creative with %s and \nunder effect %s will %s load" % (beans, hinge, grows))

start_points //= 10 
print("Let be creative with %s and \nunder effect %s will %s load" % function(start_points))         
          