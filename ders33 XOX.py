# -*- coding: utf-8 -*-
"""
XOX OYUNU 

@author: user
"""
class XOX():
    class __init__(self,tahta = [["","",""],["","",""],["","",""]]):
        self.tahta = tahta
        self.oyundurum = True
    def oyunbaşlat():
        for i in self.tahta:
            print(i)
    def p1seçim(self,satır,sutun):
        if self.kontrol(satır,sutun):
            self.tahta[satır -1][sutun -1] = "X"
            self.durum()
        else:
            print("Girdiğiniz  değerdeki bölge dolu!")
    def p2seçim():
         if self.kontrol(satır,sutun):
            self.tahta[satır -1][sutun -1] = "O"
            self.durum()
         else:
            print("Girdiğiniz  değerdeki bölge dolu!")
        
    def kontol(self,satır,sutun):
        if(self.tahta[satır -1][sutun -1] != ""):
            return False
        else:
            return True
    def durum(self):
        if(self.tahta[0][0] and self.tahta [0][1] and self.tahta[0][2] == "X"):
            return False
        self.oyundurum = False
xox = XOX()
while xox.oyundurum :
    xox.oyunbaşlat()
    satır == int(input("p1 satır giriniz:"))
    sutun == int(input("p1 sutun giriniz:"))
    xox.p1seçim(satır,sutun)
    xox.oyunbaşlat()
    satır == int(input("p2 satır giriniz:"))
    sutun == int(input("p2 sutun giriniz:"))
    xox.p2seçim(satır,sutun)
    

            
