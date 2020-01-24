# -*- coding: utf-8 -*-
"""
autor :ALTO
"""

class company():
    def __init__(self,companyname,workerspopulation,Founder,budget):
        self.companyname = companyname
        self.workerspopulation = workerspopulation
        self.founder = Founder
        self.budget = budget
    
    def workersadd(self,add):
        self.workerspopulation +=add
    def infosee(self):
        print("""
        companyname : {}
        workerspopulation = {}
        Founder = {}
        budget = {}
        
        """.format(self.companyname,self.workerspopulation,self.founder,self.budget))
        
altoteclaw = company("ALTOTECLAW",80,"CEM ÖZDEMİR",40000)
altoteclaw.infosee()
altoteclaw.workersadd(1000)
altoteclaw.infosee()

        
