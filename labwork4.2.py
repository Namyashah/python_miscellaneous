'''
#1
def factorial(n):
    if n<=0 :
        return 1
    else :
        return n*factorial(n-1)
        
z = factorial(int(input("Enter the number = ")))
print(z)

#3
def demo(g):
    if len(g)<= 1 :
        return g 
    return demo(g[1:]) + g[0]

string = input("")
f = demo(string)
print(f)

#4
def namya(k):
    if k<= :
        return k
    else :
        return namya(k+1) 
namya(int(input("Enter the number = ")))


#6
num = [1,2,3,4,5,5]
namya = lambda x : x**2
squares = list(map(namya,num))
print(squares)

#7
num = [2,3,4,6,6,6,8,74,67,7,4,7]
demo = lambda x : x%2==1  
odd = list(filter(demo,num))
print(odd)

#8
dino = lambda a,b,c : max(a,b,c)
a = int(input(""))
b = int(input(""))
c = int(input(""))
result = dino(a,b,c)
print(f"The largest of {a}, {b}, and {c} is {result}.")

#9
num = 0 
def demo():
    global num
    num = num + 1
    print("Functions Called!")
    print(num)
demo()
demo()
demo()

#10
num = 0
def demo(*gun):
    global num
    for i in gun :     
        num = num + i
    print(num)
ton = int(input("Enter the value ton = "))
for i in ton :
    demo(int(input("Enter the value = ")))

#11
username = "Namya"

def update_username():
    global username
    new_name = input("Enter the new username: ")
    username = new_name
    print("Username updated successfully!")
def display_username():
    print(f"The current username is: {username}")
    print("_____________________________________________________________")

display_username()  
update_username()  
display_username() 
'''
#12
