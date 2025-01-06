'''
class emp:
    name = ""
    age = ""
    salary = ""
e1 = emp()
e2 = emp()
e1.name = "namya"
e1.age = "18"
e1.salary = "45000"
e2.name = "yug"
e2.age = "23"
e2.salary = "52000"
if e1.salary>e2.salary :
    print(e1.name)
    print(e1.age)
    print(e1.salary)
else :
    print(e2.name)
    print(e2.age)
    print(e2.salary)
'''
class time:
    def setdata(self,x,y,z):
        self.hour = x
        self.minute = y
        self.seconds = z
    def display(s):
        print(s.hour)
        print(s.minute)
        print(s.seconds)
    def add(self,w,k):
        self.hour = self.hour + w.hour + k.hour
        self.minute = self.minute + w.minute + k.minute
        self.seconds = self.seconds + w.seconds + k.seconds
t1 = time()
t2 = time()
t3 = time()
t1.setdata(7,45,30)
print()
t2.setdata(8,25,45)
print()
t3.setdata(9,55,45)
t1.add(t2,t3)
t1.display()
