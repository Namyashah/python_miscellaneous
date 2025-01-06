'''
class car :
    light = ""
    seat = ""
class farrari(car) :
    colour = ""
z = farrari()
z.light = "blue"     
z.seat = "ventilated"     
z.colour = "red"     

print(z.light)
print(z.seat)
print(z.colour)

class demo :
    def demo(q):
        print("i am steve")
class demo2(demo) :
    def demo2(w):
        print("i am namya")
class demo3(demo2) :
    def demo3(e):
        print("i am jugal")

y = demo3()
y.demo3()

class demo :
    def demo(q):
        print("i am steve")
class demo2(demo) :
    def demo2(w):
        print("i am namya")
class demo3(demo) :
    def demo3(e):
        print("i am jugal")

y = demo()
y.demo()

class demo :
    def demo(q):
        print("i am steve")
class demo2 :
    def demo(w):
        print("i am namya")
class demo3(demo,demo2) :
    def demo3(e):
        print("i am jugal")

y = demo3()
y.demo()
'''
class demo :
    def demo(q):
        print("i am steve")
class demo2(demo) :
    def demo1(w):
        print("i am namya")
class demo3(demo) :
    def demo3(e):
        print("i am jugal")
class demo4(demo2) :
    def demo4(p):
        print("i am adish")
class demo5(demo3) :
    def demo5(k):
        print("i am heet")
class demo6(demo4,demo5) :
    def demo6(l):
        print("i am me")

y = demo6x()
y.demo()