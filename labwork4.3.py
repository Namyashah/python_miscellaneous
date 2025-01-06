'''
#1
number = int(input("Enter the number = "))
arr = []
for i in range(number):
    element = int(input("Enter the element = "))
    arr.append(element)
    
for i in arr :
print(i)

#2
arr = []
rows = int(input("Enter the number of rows = "))
cols = int(input("Enter the number of column = "))

for i in range(rows) :
    arr.append([])
    for j in range(cols) :
        arr[i].append(int(input("Enter the numbers = ")))

for i in arr :
    for j in i :
        print(j,end = " ")
    print()
    
    
#3

#4
number = int(input("Enter the number = "))
arr = []
for i in range(number):
    element = int(input("Enter the element = "))
    arr.append(element)
    
sum = 0
for i in arr :
    sum = sum + i
print(sum)

#5
arr = []
rows = int(input("Enter the number of rows = "))
cols = int(input("Enter the number of column = "))

for i in range(rows) :
    arr.append([])
    for j in range(cols) :
        arr[i].append(int(input("Enter the numbers = ")))
sum = 0
for i in arr :
    for j in i :
        sum = sum + j
print(sum)

#6
arr = []
rows = int(input("Enter the number of rows = "))
cols = int(input("Enter the number of column = "))

for i in range(rows) :
    arr.append([])
    for j in range(cols) :
        arr[i].append(int(input("Enter the numbers = ")))

a = arr[0][0]
b = arr[0][0]
        
for i in arr :
    for j in i :
        if j > a :
            a = j 
        if j < b :
            b = j

print(a)
print(b)


#8
number = int(input("Enter the number = "))
arr = []
for i in range(number):
    element = int(input("Enter the element = "))
    arr.append(element)
print(arr)
    

print("Deleting the value!!")
demo = int(input("Enter the value you want to delete = "))
arr.remove(demo)
print(arr)

#9
number = int(input("Enter the number = "))
arr = []
for i in range(number):
    element = int(input("Enter the element = "))
    arr.append(element)
    
print("Changing the position!!")

postion = int(input("Enter the position = "))
arr[postion] = int(input("Enter the value you want change = "))     
print(arr)

#7
number = int(input("Enter the number = "))
arr = []
for i in range(number):
    element = int(input("Enter the element = "))
    arr.append(element)
    
print("Adding value at specific position!!")

position = int(input("Enter the position = "))
arr.insert(position,34)
print(arr)


#10
number = int(input("Enter the number = "))
arr = []
for i in range(number):
    element = int(input("Enter the element = "))
    arr.append(element)
print(arr)
    
print("Return the value!!")
demo = int(input("Enter the number you want index of = "))
z = arr.index(demo)
print(z)

#11
number = int(input("Enter the number = "))
print("1st array")
arr1 = []
for i in range(number):
    element = int(input("Enter the element = "))
    arr1.append(element)
    
print("2nd array")
arr2 = []
for i in range(number):
    element = int(input("Enter the element = "))
    arr2.append(element)

namya = arr1 + arr2
print(namya)

#12
number = int(input("Enter the number = "))
arr = []
for i in range(number):
    element = int(input("Enter the element = "))
    arr.append(element)
    
arr.sort()
print(arr)

#15
number = int(input("Enter the number = "))
sample = []
for i in range(number):
    element = int(input("Enter the element = "))
    sample.append(element)

print(f"The Original list is = {sample}")
sample.sort()
print(f"The New list after sort  = {sample}")
print("________________________________________________________________________")
print("________________________________________________________________________")
print("________________________________________________________________________")
print(f"The Original list is = {sample}")
new_list = sorted(sample)
print(f"The New sorted list is {new_list}")
print(f"The Original list is = {sample}")
'''

#13
namya = [(1,2,3,4,56),(24,65,32,78,1),(3,63,23,22,87),(2,3,54,3,5),(45,23,55,33),(9,8,7,6,4)]
demo = sorted(namya[(1)])
print(demo)