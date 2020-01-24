"""
@author: user #ders 49 ve 50 birleşik işlenmiştir.
"""
import sqlite3

baglantı = sqlite3.connect("Lawyers_Info.db")
mark = baglantı.cursor()
def LawyerStudio():
    
    
    mark.execute("create table if not exists Lawyers_Info(LAWYERS_NAME TEXT,LAWYERS_BUDGETS INT, PART TEXT)")
    baglantı.commit()
   
def giveainformation(LAWYERS_NAME,LAWYERS_BUDGETS,PART):
    mark.execute("insert into Lawyers_Info('{}',{},'{}')")
    baglantı.commit()

    
    
LawyerStudio()

giveainformation()
baglantı.close()