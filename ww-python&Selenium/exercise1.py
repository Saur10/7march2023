'''
a=int(input("a = "))
b=int(input("b = "))

# c=a+b
# print(c)
# b=c-b
# a=c-a
# print("a = ",a)
# print("b = ",b)

a,b=b,a

print(b)
'''
#print rectange of starts

'''
for item in range(0,4):

    for j in range(0,5):
        print("*", end=" ")

    print()
'''

for i in range(0,4):
    for j in range(0,5):
        if (i==0 or i==3):
            print("*", end=" ")

        else:
            if (j==0 or j==4):
                print("*", end=" ")

            else:
                print("@", end=" ")



    print()


























