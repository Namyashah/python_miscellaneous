'''
x = int(input("enter your contact number = "))
sum = 0
while x :
    j=x%10
    sum=sum+j
    x=x//10
print(sum)

a = int(input(""))
b = int(input(""))
c = int(input(""))

if a>b :
    if a>c :
        print("a is highest")
    else :
        print("c is highest")
else :
    if b>c :
        print("b is highest")
    else :
        print("c is highest")

a = int(input(""))
b = int(input(""))
c = int(input(""))
d = int(input(""))

if a>b :
    if a>c :
        if a>d :
            print("a is highest")
    elif c>d :
            print("c is highest")
    else :
            print("d is highest")
else :
    if b>c :
        if b>d :
            print("b is highest")
    elif c>d :
            print("c is highest")
    else :
            print("d is highest")

a = int(input(""))

if a<13 :
    print("child")
elif a>12 and a<20 :
    print("teenager")
elif a>19 and a<65 :
    print("adult")
else :
    print("senior")

a = (input(""))

if len a<6 :
    print("weak")
elif len a>=6 and a<12 :
    print("moderate")
else :
    print("strong")
    
for i in range(1,5):
    for s in range(1,6):
        print(i,end="")
    print()
    
for i in range(5):
    for s in range(1,8,2):
        print(s,end="")
    print()

for i in range(5):
    for s in range(1,5):
        print(s,end="")
    print()
    
for i in range(1):
    for s in range(1,26):
        if s%5==0 :
            print(s,end="\n")
        else :
            print(s,end=" ")

for i in range(5):
    for s in range(5):
        if s==1 or s==3 :
            print("0",end="")
        else :
            print("1",end="")
    print()

for i in range(6):
    for s in range(5):
        if i==0 or i==2 or i==4 :
            print("1",end="")
        else :
            print("0",end="")
    print()
    
k = 1 
for i in range(5,0,-1):
    for s in range(1,6):
        if i==s :
            print("$",end="")
        elif s==k :
            print("$",end="")
        else :
            print("*",end="")
    k = k+1
    print()

k = 1
for i in range(5,0,-1):
    if i%2==0 :
        for s in range(1,6):
            if s%2==0 :
                print("1",end="")
            else :
                print("0",end="")
        print()
    else :
        for s in range(1,6):
            if s%2==0 :
                print("0",end="")
            else :
                print("1",end="")
        print()

for i in range(1,6):
        for s in range(1,6):
            if i!=s :
                print(s,end="")
        print()

k = 6
for i in range(1,6):
    for s in range(i,k):
        print(s,end="")
    k = k+1
    print()
   
k = 6
for i in range(1,6):
    for s in range(i,k,i):
        print(s,end=" ")
    k = k+5
    print()

k = 1
for i in range(5):
    for s in range(0,k):
        print("*",end="")
    k = k+1
    print()

k = 5
for i in range(5):
    for s in range(k,0,-1):
        print("*",end="")
    k = k-1
    print()

k = 2
for i in range(1,6):
    for s in range(1,k):
        print(s,end="")
    k = k+1
    print()

k = 6
for i in range(1,6):
    for s in range(1,k):
        print(s,end="")
    k = k-1
    print()

k = 2 
for i in range(1,6):
    for s in range(1,k,2):
        print(s,end=" ")
    k = k+2
    print()

k = 5
for i in range(0,6):
    for s in range(k,i,-1):
        print(s,end="")
    print()

k = 0 
for i in range(1,6):
    for s in range(i,k,-1):
        print(s,end="")
    print()

k = 6 
for i in range(1,6):
    for s in range(i,k):
        print(s,end="")
    print()

k = 5 
for i in range(1,6):
    for s in range(k,0,-1):
        print(s,end="")
    k = k-1
    print()

k = 5 
for i in range(1,6):
    for s in range(k,6):
        print(s,end="")
    k = k-1
    print()

k = 9
for i in range(1,6):
    for s in range(k,0,-2):
        print(s,end="")
    k = k-2
    print()

k = 1 
for i in range(1,6):
    for s in range(k,0,-2):
        print(s,end="")
    k = k+2
    print()

k = 10
for i in range(1,6):
    for s in range(1,k,2):
        print(s,end="")
    k = k-2
    print()

i = int(input(""))
while (i<50):
    print("*",end="")
    i = i+1

i = 0
while (i<=4):
    s = 0
    while (s<=4):
        print("*",end="")
        s = s+1
    i = i+1
    print()

i = 0 
while (i<=4):
    s = 0 
    while (s<=4):
        if s==2 :
            print("$",end="")
        else :
            print("*",end="")
        s = s+1
    i = i+1
    print()

i = 0
while (i<=4):
    s = 0
    while (s<=4):
        if s==0 or s==4 :
            print("$",end=" ")
        else :
            print("*",end=" ")
        s = s+1
    i = i+1
    print()

i = 0
while (i<=4):
    s = 0 
    while (s<=4):
        if i==2 :
            print("$",end="")
        else :
            print("*",end="")
        s = s+1
    i = i+1
    print()

i = 0 
while (i<=4):
    s = 0
    while (s<=4):
        if i==0 or i==4 :
            print("*",end="")
        else :
            if s==0 or s==4 :
                print("*",end="")
            else :

i = 1
while (i<=5):
    print("*",end="")
    i = i+1

i = 1
while (i<=5):
    s = 1
    while (s<=5):
        if i==3 :
            print("$",end="")
        else :
            if s==3 :
                print("$",end="")
            else :
                print("*",end="")
        s = s+1
    i = i+1
    print()

i = 1
while (i<=5):
    s = 1
    while (s<=5):
        if s==i :
            print("$",end="")
        else :
            print("*",end="")
        s = s+1
    i = i+1
    print()

i = 5
while (i>=1):
    s = 1
    while (s<=5):
        if s==i :
            print("$",end="")
        else :
            print("*",end="")
        s = s+1
    i = i-1
    print()

k = 1
i = 5 
while (i>=1):
    s = 1
    while (s<=5):
        if i==s :
            print("$",end="")
        elif s==k :
            print("$",end="")
        else :
            print("*",end="")
        s = s+1
    k = k+1
    i = i-1
    print()
lst 
z = [0,1,2,3,4,5,6,7,1,2,3,4,5,6,2,3,4,5,"namya"]
print(dir(z))


z.append(100)
print(z)
#z.clear()
print(z.count(1))
z.insert(5,560)
print(z.index("namya"))
z.pop(18)
z.remove("namya")
z.reverse()
z.sort(reverse=True)
print(z)

tuple
t = (1,2,3,4,5,6,7,8,9,2,1,2,21,"hi",2.3)
print(t)
print(dir(t))
print(t[7])
print(t.count(2))
print(t.index(9))
print(type(t))

print("1.add")
print("2.sub")
print("3.divide")
print("4.multiplications")

z = int(input(""))
x = int(input(""))
y = int(input(""))
if z==1 :
    print("add",end="")
    print()
    if z==1 :
        print(x+y,end="")
elif z==2 :
    print("sub",end="")
    print()
    if z==2 :
        print(x-y,end="")
elif z==3 :
    print("divide",end="")
    print()
    if z==3 :
        print(x//y,end="")
elif z==4 :
    print("multiplications",end="")
    print()
    if z==4 :
        print(x*y,end="")
else :
    print("",end="")

z = [1,2,3,4,5,6,7,8,3,2,2,1,1]
print("1.append")
print("2.remove")
print("3.update")
print("4.display")

x = int(input(""))
if x==1 :
    y = int(input(""))
    z.append(y)
    print(z)
elif x==2 :
    y = int(input(""))
    if  y in z :
        print("FOUND",end="")
        print()
        z.remove(y)
        print(z)
    else :
        print("NOT FOUND",end="")
elif x==3 :
    t = int(input(""))
    if t in z :
        print("FOUND",end="")
        index = z.index(t)
        s = int(input("enter the value of new number"))
        z[index]= s
        print(z)
    else :
        print("NOT FOUND",end="")
elif x==4 :
    print(z)
'''     







