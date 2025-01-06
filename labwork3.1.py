'''
#1
First_name = input("first name = ")
Last_name = input("last name = ")

print("Hello!",[First_name],[Last_name],"!")
#2
item = "apple"
price = 5.50
print(f"The price of {item} is {price} dollors")

#3
string = input("")
a = string[::-1]
if a==string :
    print("It is palindrome")
else :
    print("It is not palindrome")
    
#4
string = input("")
a = string.upper()
print(a)

a = string.lower()
print(a)

a = string.title()
print(a)

#5
namya = [i for i in range(1,11)]
print(namya)
namya.append(11)
print(namya)

#6
a = int(input(""))
numbers = [i for i in range(1,a)]
print(numbers)
numbers.reverse()
print(numbers)
print(max(numbers))
print(min(numbers))

#7
tuple = (1,2,2,3,3,4,5,5,5,6,6,7)
z = tuple 
z = set()
z = tuple(z)
print(tuple)
#8
a = int(input(""))
lst = [i for i in range(1,a)]
print(lst)
lst[3] = 'namya'
print(lst)

#9
a = [1,2,3]
a.append([22,33,44,55])
a.append(["namya"])
print(a)
a[3] = ["hiiiiii"]
print(a)

#10
lst = [1,2,3,4,5,6,7,8,9]
lst.append(10)
lst.remove(3)
lst[1] = '20'
print(lst)

#this are not suitable for tuples because they are immutable and list are not .

#11
tuple = ([1,2,3],[4,5,6],[7,8,9])
tuple[0] = [1,2,3,4,5,6,7]
print(tuple)
#tuple is only meant for seeing and it is not used for modifying data or tuple.

#12
a = [23,56,56,78,43]
b = [84,36,45,78,23]
a = b
a.append(87)
print(a)
print(b) 


#13
a = [23,56,56,78,43]
b = [84,36,45,78,23]
a = b.copy()
b.append(100)
print(a)
print(b)
'''