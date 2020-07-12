# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:29:39 2020

@author: petru
"""
import statistics as sts
import matplotlib.pyplot as plt 
x = [15, 25, 40, 58, 60, 64, 73, 85, 88, 90, 95]
y = [13, 35, 20, 43, 6, 25, 40, 12, 45, 36, 15]
x_mean = sts.mean(x)
#print(x_mean)
y_mean = sts.mean(y)
x_distance = [x_point - x_mean for x_point in x]
#print(x_distance)
y_distance = [y_point - y_mean for y_point in y]
#print(y_distance)   
xdistance_squared = [(x_point - x_mean)**2 for x_point in x]
xdistance_squared = sum(xdistance_squared)
#print(xdistance_squared)
total_list = [x * y for x, y in zip(x_distance, y_distance)]
total_list = sum(total_list)
#print(total_list)
slope = total_list / xdistance_squared 
interception = y_mean - slope * x_mean 
print("The mean value of y points {:5.3f}".format(y_mean))
print("The mean value of x points {:5.3f}".format(x_mean))
print("The slope value is: {:5.3f}".format(slope))
print("The interception with y axis: {:5.3f}".format(interception))
#linear regresion formula 
def get_y(m, b, x):
    y = m * x + b 
    return y
#calculate the  y predict   
def calculate_all_values(m, b, points):
    y_pred = []
    for point in points:
        calculate_y = get_y(m, b, point)
        y_pred.append(calculate_y)
    return(y_pred)
#print(calculate_all_values(slope, interception, x))
        
def plot_regression_line(x, y):
    #plot the scattering points or datapoints
    plt.scatter(x, y, color = "black",  marker= 'o', s = 30)
    y_predict = calculate_all_values(slope, interception, x)
    #plot the regresion line
    plt.plot(x, y_predict, linewidth = 3, color = "red")
    # putting labels 
    plt.xlabel('x') 
    plt.ylabel('y')
    plt.show()
plot_regression_line(x, y)
    
