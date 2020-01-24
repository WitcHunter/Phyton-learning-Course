"""
@author: user
"""
try:   
     with open("Lawyers.txt","r") as file:
         print(file.tell())
         a =file.read()
         print(a)
         print(file.tell())
         file.seek(31)
         print(file.tell())
         b= file.read()
         print(b)
        
except FileNotFoundError:
    print("Böyle bir dosya bulunamadı.")
     