
"""
In this tutorial, you'll learn how to create iterations easily using Python generators,
how it is different from iterators and normal functions, and why you should use it.

Itarators and generators are used to handle large stream of data , large stream of data we can not
store in memory at once, to handle this we use generators to handle at a time
"""

def even_generator():

    n=0
    n+=2
    yield n

    n += 2
    yield n

    n += 2
    yield n

    pass

number= even_generator()

print(next(number))
print(next(number))

def ev_generator(max):
    n=2
    while n <= max:
        yield n
        n+=2


num=ev_generator(10)
print(next(num))
print(next(num))
print(next(num))
print(next(num))
print(next(num))

print("------------------ febonocii  --------------------")
# 0 1 1 2 3 5 8 13 21 34 55
def febonaci(max):
    n=0
    b=1
    while n <= max:
        yield n
        b, n = n,n+b

fb= febonaci(40)
print(next(fb))
print(next(fb))
print(next(fb))
print(next(fb))
print(next(fb))
print(next(fb))
print(next(fb))
print(next(fb))
print(next(fb))