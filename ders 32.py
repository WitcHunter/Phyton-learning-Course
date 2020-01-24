# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 15:30:44 2019

@author: user
"""
import time as zaman
import random as rastgele
class winamp():
    def __init__(self,şarkılar = []):
        self.şarkılar = şarkılar
        self.durum = True
        self.ses = 100
        self.çalanşarkı = ""
    def sesarrtır(self):
        if(self.ses >=96):
            pass
        else:
            print("SES ARTTIRILIYOR")
            zaman.sleep(2)
            print("SES ARTTIRILIYOR. Güncel ses = {}".format(self.ses))
            self.ses +=5
    def sesazalt(self):
     if(self.ses <= 0):
         pass
     else:
        print("SES AZALTILIYOR")
            zaman.sleep(2)
            print("SES AZALTILDI. Güncel ses = {}".format(self.ses)) 
         
         self.ses -=5
         
    def şarkıseç(self,şarkı):
        self.şarkılar.append(şarkı)
    def şarkıseç(self):
        sayaç = 2
        for i in self.şarkılar:
            print("{},{}".format(sayaç,i))
        
            
        
o1 = winamp(şarkılar = ["HARDAL-gitme"])

while True:
    
    