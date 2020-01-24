"""
@author: user
"""
a=(list(filter(lambda x :x % 2==0,[x for x in range(100)])))
print(a)

def asalmı(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

b = list(filter(asalmı,[x for x in range(1000)]))
print(b)
print(asalmı(20))
print(asalmı(134566744566788))

