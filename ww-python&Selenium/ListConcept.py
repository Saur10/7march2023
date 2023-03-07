# Define new list

list=['java','2021','C#',"python", True, False]

print(len(list))
print(list[4])

print(list[2:4])

print(list[2:])

print(list[:4])

print(list[::-1])

print(list[1][::-1])

# for i in range(len(list)+1):
#     print(list[i])

for data in list:
    print(data)

# write option >> update value on list

list=[2021,'java','C#',"python", True, False]

list[2]='c++'  # updating
print(list)

list.insert(2,'PHP') # insert is function
print(list)

# delete value
list.remove("java")
print(list)

list=[2021,'java','C#',"python", True, False]

list.pop(0)
print(list)

print("=========================================")

list=[2021,'java','C#',"python", True, False]

for item in list:
    print(item)

















