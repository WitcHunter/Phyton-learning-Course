# -*- coding: utf-8 -*-
"""
@author: user
"""

class country():
    def __init__(self,country,language,budget):
        self.country = country
        self.language = language
        self.budget = budget
    def conrtyfounder(self):
        return "MUSTAFA KEMAL ATATÜRK"
    
    def __str__(self):
        return("counrty = {},language = {},budget = {}".format(self.country,self.language,self.budget))
    def __len__(self):
        return self.budget

turkey =country("Turkey","turkish",860000000)

print(len(turkey))



