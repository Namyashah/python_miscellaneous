'''
class time:
    # def __init__(self):
    # print("i am func that call autometically")
    def __init__(self,x,y,z):
        self.hour = x
        self.minute = y
        self.seconds = z
    def display(self):
        print(self.hour)
        print(self.minute)
        print(self.seconds)
class time :
    def __str__(self):
        print("i am new")
        return "hi" # must return str
t1 = time()
# print(t1.__str__())
print(t1)

    
	
t1 = time(2,3,4)
t2 = time(12,13,14)
print(t1)
print(t2)
# t1.display()
# t2.display()
class time :
    def __init__(self,q,w,e):
        self.hour = q
        self.minute = w
        self.seconds = e
    def __str__(self):
        print(self.hour)
        print(self.minute)
        print(self.seconds)
        return ""
    def __truediv__(self,x): 
        self.hour = self.hour // x.hour
        self.minute = self.minute // x.minute
        self.seconds = self.seconds // x.seconds
        return self
t1 = time(27,8,1)
t2 = time(3,2,1)
t3 = time(3,2,1)
t1/t2/t3
print(t1)
'''
    1
   22
  333
 4444
55555 

1*1=1
1*2=2
1*3=3
1*4=4
1*5=5 