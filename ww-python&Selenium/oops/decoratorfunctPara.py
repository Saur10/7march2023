'''
 Decorator >>

Python decorators allow you to change the behavior of a function without modifying the function itself.

Basically, a decorator takes in a function, adds some functionality and returns it
'''

def smartdiv(func):
    def inner (a,b):
        print("we ar dividing",a,"by",b)
        if b==0:
            print("we can not divide by : ",b)
            return
        return func(a,b)
    return inner


@smartdiv
def divide(a,b):
    return a/b

value1=divide(10,0)
print(value1)
value2=divide(5,2)
print(value2)

