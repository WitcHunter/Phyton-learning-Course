# -*- coding: utf-8 -*-
"""
@author: user
"""
def toplamal(liste):
    if type(liste) == list or type(liste)== tuple:
        toplam = 0
        for i in liste:
            toplam +=i
        return toplam
    else:
        raise ValueError("Bilader malmısın düzgün gir şunu" )
    
a = toplamal("Cem özdemir")
print(a)

