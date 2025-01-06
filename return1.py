'''
def sum1(a,b):
    c = a+b
    return c,a
    # return a
    # print("hello")
x = sum1(2,3)
print(x)

def sum(k) :
    m = 0
    for i in k :
        m = m+i
    return m



lst = [1,2,3,4,5,6]
lst1 = [2,3,4,3,2,1]
x = sum(lst1)
z = sum(lst)
print(z)        

def mul(a) :
    for i in range(a,0,-1) :
        print(i)
    
    
    
mul(10)

def max(a,b,c):
    if a>b :
        if a>c :
            print("a is max")
            return a
        else :
            print("c is max")
            return c
    else :
        if b>c :
            print("b is max")
            return b
        else :
            print("c is max")
            return c
            
z = max(20,30,50)
print(z)

def demo():
    print("namya")
    demo()
demo()

def demo():
    print("namya shah")
    def menu():
        print("123456")
    menu()
demo()

def demo(a):
    k = 1
    for i in range(a,0,-1):
        k = k*i
        # print(k)
    return k
    
z = demo(5)
print(z)

def fact(a):
    if a==1 :
        return 1
    else :
        return a*fact(a-1)
z = fact(5)
print(z)

def demo(k):    
    return k[::-1]
    
lst = [1,2,3,4,5,6,7]
z = demo(lst)
print(z)
'''