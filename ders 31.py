# -*- coding: utf-8 -*-
"""

@author: user
"""
class worker():
    def __init__(self,name,age,adress):
        self.name = name
        self.age = age
        self.adress = adress
        
    def infosee(self):
        print("""
        name: {}      
        age: {}
        adress: {}
        
        
        """.format(self.name,self.age,self.adress))
        
        
class workersheader(worker):
    def sallaryascend(self):
        self.age



i2 = worker("Ali Tütüncü",32,"eski sille cad bizim sitesi b blok no:6")
i2.infosee()
y1 = workersheader("Faruk Büyükafacan",25,"hızlı tren garı yakını Meram")
y1.infosee()