"""
@author: user  map() fonkisyonu 41.ders
"""
def kare(x):
    return x**2

print(list(map(kare,[1,2,3,4,5,6,78,9,90])))

a = list(map(lambda x:x**2,[1,2,3,4,5]))
print(a)

#ders 42 de burada olacak reduce()

from functools import reduce
a = reduce(lambda x,y: x+y,[20,30,42,288,365,7])
print(a)

