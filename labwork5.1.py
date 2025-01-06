'''
#1
class Person:
    name = ""
    age = ""
    def setdata(self) :
        self.name = input("Enter the name = ")
        self.age = int(input("Enter the age = "))
    def getdata(self) :
        print(self.name,self.age)
        
p1 = Person()
p2 = Person()
p1.setdata()
p2.setdata()
p1.getdata()
p2.getdata()

#2
class counter:
    def __init__(self) :
        self.number = 0
    def setdata(self) :
        self.number+=1 
    def getdata(self) :
        print(f"The data has been called {self.number}")
        
C1 = counter()
C1.setdata()
C1.getdata()
C1.setdata()
C1.getdata()
C1.setdata()
C1.getdata()

#3
class namya:
    name = ""
    age = ""
    def setdata(self) :
        self.name = input("Enter the name = ")
        self.age = int(input("Enter the age = "))
    def getdata(self) :
        print(self.name,self.age)
n1 = namya()
n2 = namya()
n3 = namya()
del n1
del n2
del n3
n3.setdata()
n3.getdata()

#4
class namya:
    name = ""
    age = ""
    def setdata() :
        self.name = input("Enter the name = ")
        self.age = int(input("Enter the age = "))
    def getdata() :
        print(self.name,self.age)

n1 = namya()
n1.setdata()
n1.getdata()

#5
class animal:
    def __init__(self) :
        self.name = input("Enter the Name of the animal = ")
    def getdata(self) :
        print(f"The name of animal is {self.name}")
        
a1 = animal()
a2 = animal()
a1.getdata()
a2.getdata()

#6
class rectangle:
    def __init__(self,lenght,width):
        self.lenght = lenght
        self.width = width
    def area_of_rectangle(self) :
        self.area =self.lenght*self.width
    def getdata(self) :
        print(f"The area of rectangle is {self.area}")
    
r1 = rectangle(12,43)
r2 = rectangle(45,87)
r1.area_of_rectangle()
r2.area_of_rectangle()
r1.getdata()
r2.getdata()

#7
class emp:
    def __init__(self) :
        self.ID = int(input("Enter the id you want = "))
        self.Name = input("Enter the name you want = ")
        self.salary = int(input("Enter the salary you have = "))
    def __del__(self):
        print("Both object and data has been deleted!!")
    def getdata(self) :
        print(f"The following information has been showed = {self.ID,self.Name,self.salary}")
        
e1 = emp()
e2 = emp()
e1.getdata()
e2.getdata()

#8
class book:
    __title = ""
    __author = ""
    def setdata(self):
        self.__title = input("Enter the tile of the book = ")
        self.__author = input("Enter the name of the author= ")
    def getdata(self) :
        print(f"The name of the author is {self.__author} and the title of the book is {self.__title}")

b1 = book()
b2 = book()
b1.setdata()
b2.setdata()
b1.getdata()
b2.getdata()
'''

#9
class acc:
    def __init__(self) :
        self.balance = int(input("Enter the am"))
        