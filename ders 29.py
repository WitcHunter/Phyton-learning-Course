# -*- coding: utf-8 -*-
"""

@author: user
"""
class araba():
    model = "BMW"
    plaka = "34 ASD 34"
    silindir = "6"
    motor = "BMW engine"
    
araba1 = araba()
print(araba1.plaka)


class arabax():
    def __init__(self,mod,colour,engine):
        self.m = mod
        self.c = colour
        self.e = engine
        
        
car1 = arabax("A8","blue",8)
print(car1.c,car1.e,car1.m)
car2 = arabax("Nissan","white",3.2)
print(car2.m,car2.c,car2.e) 
    