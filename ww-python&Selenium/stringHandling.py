
name="testing world"
a=10
print(name[2:5])
print(name+ str(a))
print(name,a)

data="This is testing world"

b=data[::-1]

print(b)

print(name.upper())
print(name.lower())
print(name.capitalize())

print(name.__contains__("is"))


data=" This is testing world  "

print(len(data.rstrip().lstrip()))

print("------------------------------------------------------")
s = "KarTIk"
new_string = "arkKTI"
upper=''
lower=''
for item in s:

    if item.isupper():
       upper=upper+item

    if item.islower():
       lower=lower+item

print(lower+upper)






