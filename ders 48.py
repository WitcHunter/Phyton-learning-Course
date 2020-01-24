# -*- coding: utf-8 -*-
"""
@author: user Kümeler veri tipi

"""
küme = {1,2,3,4,4,5,6,4,3,2,145,6,78,8,9,9,20}
liste1 = {20,30,40,45,64,65,87,}

küme2 = set(küme)
print(küme2)

yazılım = {"C++","JAVA","PHP","PYTHON"}

for i in yazılım:
    print(i)
    
yazılım.add(50)
print(küme.isdisjoint(liste1))
print(küme.intersection(liste1))
print(küme.discard(2))
print(küme)
