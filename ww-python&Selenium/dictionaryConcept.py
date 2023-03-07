
dict= {"a":100,"b":200,"c":"hello"}

print(dict)
print(dict["a"])

print(len(dict))

print(dict.keys())

print(dict.values())

for i in dict:
    print(dict[i])

dict= {"a":100,"b":200,"c":"hello", "d":"abc"}

dict["d"]="updated value"

print(dict)

#Delete values from dict
dict.pop("b")
print(dict)

# to add items in dict
dict= {"a":100,"b":200,"c":"hello", "d":"abc"}
dict['g']='ggg'

print(dict)

#dict.update('ffff')

#dict= {"user","bill","password","hillary"}
#print(dict["password"])
dict1= {"a":100,"b":200,"c":"hello", "d":"abc"}
#dict1.ap
#dict1['new']='Value'
print("dict 1 is ",dict1)


di= {"user","bill","password","hillary"}
#print(di["password"])

print("length ::: ", len(dict1))

for item in dict1:
    print(item)
    print(dict1[item])


