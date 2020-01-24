"""
@author: user
"""
with open("Bilgiler.txt","r+") as file:
    liste = file.readlines()
    liste.insert(3,"Blame Game\n")
    file.seek(0)
    for i in liste:
        file.write(i)
        
        
        
    

    
    
    
