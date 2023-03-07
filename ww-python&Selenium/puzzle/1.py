'''14. Write a Python program to find the lengths of a given list of non-empty strings. Go to the editor
Input:
['cat', 'car', 'fear', 'center']
Output:
[3, 3, 4, 6]
Input:
['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
Output:
[3, 3, 7, 5, 2, 4, 0]'''




'''3. Write a Python program that accept an integer test whether an integer greater than 4^4 and which is 4 mod 34.
Input:
922
Output:
True
Input:
914
Output:
False
Input:
854
Output:
True
Input:
854
Output:
True
Click me to see the sample solution'''

n=916
#print(10%8)
if (n % 34 == 4) and n > 4 ** 4 :
    print(True)
else:
    print(False)










'''
2. Write a Python program that accept a list of integers and check the length and the fifth element.
 Return true if the length of the list is 8 and fifth element occurs thrice in the said list.
 Go to the editor
Input:
[19, 19, 15, 5, 5, 5, 1, 2]
Output:
True
Input:
[19, 15, 5, 7, 5, 5, 2]
Output:
False
Input:
[11, 12, 14, 13, 14, 13, 15, 14]
Output:
True
Input:
[19, 15, 11, 7, 5, 6, 2]
Output:
False
'''
l=[19, 19, 15, 5, 5, 5, 1, 2]
length=len(l)
fifthelem=l[4]
counter=0
for item in range(length):
    if l[item]==fifthelem:
        counter=counter+1

if (length==8) & (counter==3):
    print(True)
else:
    print(False)




'''
1. Write a Python program find a list of integers with exactly two occurrences of nineteen
and at least three occurrences of five. Go to the editor
Input:
[19, 19, 15, 5, 3, 5, 5, 2]
Output:
True
Input:
[19, 15, 15, 5, 3, 3, 5, 2]
Output:
False
Input:
[19, 19, 5, 5, 5, 5, 5]
Output:
True
'''

#inp= input("enter the list ::  ")

inp=[19, 15, 15, 5, 3, 3, 5, 2]
coun19=0
count5=0
l=len(inp)
for item in range (l):
    if inp[item]==19:
        coun19=coun19+1

    if inp[item] ==5:
        count5= count5+1
if (coun19==2) & (count5==3):
    print("exactly two occurrences of nineteen and at least three occurrences of five", True)
else:
    print(False)

