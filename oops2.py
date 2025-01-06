class time:
    def setdata(self,x,y,z):
        self.hour = x
        self.minute = y
        self.seconds = z
    def display(self):
        print(self.hour)
        print(self.minute)
        print(self.seconds)
    def add(self,w):
        temp = time()
        temp.hour = self.hour + w.hour
        temp.minute = self.minute + w.minute
        temp.seconds = self.seconds + w.seconds
        return temp
t1 = time()
t2 = time()
t3 = time()
t1.setdata(7,45,30) 
print()
t2.setdata(8,25,45)
print()
t3 = t1.add(t2)
t3.display()


