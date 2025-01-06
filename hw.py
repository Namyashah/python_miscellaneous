x = open('yes.txt',"a")
w = open('even.txt',"a")
c = open('odd.txt',"a")
y = input("")
x.write(y)
x = open('yes.txt',"r")

m = x.read()
for i in m:
    if int(i)%2==0 :
        w.write(i)
    else :
        c.write(i)
print(m)
x.close()
w.close()
c.close()