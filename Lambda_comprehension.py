# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 16:09:18 2019

@author: petru
"""
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = [x for x in garbled if x != 'X']
mesage = ''.join(message[::-1])
print(mesage)

mesages = garbled[::-2]
print(mesages)

garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = list(filter(lambda x: x != 'X', message))
print(message)