'''
#1
number = [1,2,3,4,5,6,7]
print(len(number))
print(max(number))
print(min(number))
print(sum(number))
print(type(number))


#3
n = [2,3,4,5,6]
def emp():     
    num = [i**2 for i in n ]
    return num
            
z = emp()
print(z)


#3
def factorial(n):
    fact = 1
    for i in range(1,n+1) :
        fact *= i
    return fact
        
num = int(input(""))
z = factorial(num)
print(z)

#4
def name(n):
    ditto = {}
    for char in n:
        if char in ditto :
            ditto[char] += 1
        else:
            ditto[char] = 1
    return ditto
tour = input("")
z = name(tour)
print(z)


#5
def cube(v):
    return v**3
def name2(ton,numbers):
    return [ton(i) for i in numbers]

num = [3,4,5,6,7]    
z = name2(cube,num)
print(z)


#6
def nam(*demo):
    sum  = 0
    for i in demo:
        sum = sum +i
    return sum
def nam1(*demo):
    sum = 1 
    for i in demo:
        sum = sum*i
    return sum
z = nam(2,3,4,6,7)
w = nam1(2,3,4,6,7)
print(z)
print(w)


#7
def std(*demo):
    if demo==():
        print("The student list is empty")
    else :
        for i in demo :
            print(i)

std("namya","yug","jugal","rahi","vansh","rahul")


#8
def plot(*demo):
    string = tuple(i for i in demo if isinstance(i,str))
    integer = tuple(i for i in demo if isinstance(i,int))
    return string,integer 
z = plot(2,3,4,5,6,"namya","yug","jugal")
string,integer = z
print("String = ",string)
print("numbers = ",integer)


#9
def identity(**person):
    for i in person :
        print(i," = ",person[i])
    
identity(Name = "namya",Age = 18,City = "surat")
''' 


#10
def product(**demo):
    

product(k={name = "poko",price = "15000",quantity = "20"}, k2={name = "samsung",price = "20000",quantity = "10"}, k3={name = "oppo",price = "50000",quantity = "30"})