'''
#1
a = int(input(""))
if a%2==0 :
    print("a is even")
else :
    print("b is odd")
    
    
#2
Age = int(input("Enter the Age = "))
if Age <60 :
    if  Age <=12:
        print("You are Child")
    elif Age <=19:
        print("You are a Teenager")
    else :
        print("Yuo are Adult")
else:
    print("You are a Senior")
        
#3
a = int(input("Enter the value of a = "))
b = int(input("Enter the value of b = "))
c = int(input("Enter the value of c = "))

if a > b:
    if a > c:
        print("a is max")
    elif c > a:
        print("c is max")
    else:
        print("a and c are the same and the largest")
elif b > c:
    if b > a:
        print("b is max")
    else:
        print("b and a are the same and the largest")
elif c > b:
    print("c is max")
elif b == c == a:
    print("all are the same")
else:
    print("b and c are the same and the largest")
    
    
#4
a = int(input("Enter the number a = "))
b = int(input("Enter the number b = "))
choice = input("Enter the choice = ")
if choice == '+' :
    result = a + b
    print("the sum is =  ",result)
elif choice == '-' :
    result = a - b
    print("The sub is :-- " ,result)
elif choice == '*' :
    result = a * b
    print("The multipication  is :-- " ,result)
elif choice == '/':
    if a != 0:  
        result = a / b
        print("The result of division is:--   ",result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")


#5
i = int(input("enter the number = "))
while i <= 10:
    print(i)
    i += 1


#6
for i in range (1,11,1):
    print(i)
print()
for i in range (1,11,1):
    print(i**2)


#7
i = 1
while i <= 50:
    if  i%2 == 0:
        print(i)
    i = i + 1


#8
for i in range (1,21,1):
    print(i)
print()
for i in range (1,21,1):
    if i%2 == 1:
        print(i)


#9
for i in range (5,51,5):
    print(i)


#10
for i in range (10,0,-1):
    print(i)


#11
for i in range(1,51):
    if i%2 == 0 and  i%3 == 0:
        print(i,":-Both are divisible by 2 and 3")
    elif i%2 == 0 and i%3 != 0:
        print(i,":-The number is divisible by 2")
    elif i%2 != 0 and i%3 == 0:
        print(i,":-The number is divisible by 2")
    else:
        print(i)
'''