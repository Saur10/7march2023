
expr= input("enter the expr ")
print("your entered ", expr)

# AAnswer =  enter the expr

'''
t=(1,2,3)
t=(t[0],)+(5,)+(t[-1])
print(t)
'''
mystr="hello"
print(mystr[::-1])


def divide(x,y):
    try:
        result=x/y

    except ZeroDivisionError:
        print("error")

    else:
        print("result is : ",result)

    finally:
        print("release")


divide('a','b')














