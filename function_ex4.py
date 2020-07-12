# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 20:35:45 2020

@author: petru
"""
def cost_ground_shipping(weight):
    if weight < 2:
        cost = 1.5
    elif weight <= 6:
        cost = 3
    elif weight <= 10:
        cost = 4
    else:
        cost = 4.5
    return 20 + (cost * weight)


premiere_gold_shipping = 125

def cost_drone_shipping(weight):
    if weight < 2:
        cost = 4.5
    elif weight <= 6:
        cost = 9
    elif weight <= 10:
        cost = 12
    else:
        cost = 14.5
    return cost * weight 


def cost_shipping(weight):
    ground = cost_ground_shipping(weight)
    drone = cost_drone_shipping(weight)
    gold = premiere_gold_shipping
    if ground < drone and ground < gold:
        method = " Ground Shipping"
        cost = ground
    elif gold < ground and gold < drone:
        method = "Premiere gold"
        cost = gold 
    else:
        method = "Drone Shipping"
        cost = drone
    
    print("This is the cheapest option %s and the cost is $%.2f." % (method, cost))
cost_shipping(4.8)
cost_shipping(45)
    
    
    
    
    
    