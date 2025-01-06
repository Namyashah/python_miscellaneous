'''
d ={"a":12,"cdvs":23,"bb":89,"a":56,"m":56 }
print(d)
print(d["a"])
#print(d["llll"])
d["llll"] = 9

print(d)


print(dir(d))

print(d.get("bb"))
print(d.items())

while True:
    z = {"a":1,"b":2,"c":3,"d":4}
    print("1.create")
    print("2.remove")
    print("3.update")
    print("4.display")
    print("0.exit")

    x = int(input(""))
    if x==1 :
        key = input("")
        value = int(input(""))
        z[key] = value
        print(z)
    elif x==2 :
        y = input("")
        if y in z :
            print("FOUND",end="")
            print()
            z.pop(y)
            print(z)
        else :
            print("NOT FOUND",end="")
    elif x==3 :
        key = input()
        y = int(input(""))
        if key in z :
            print("FOUND",end="")
            print()
            z[key]=y
            print(z)
        else :
            print("NOT FOUND",end="")
    elif x==4 :
        print(z)
    elif x == 0:
        print("bye..!jay jindra")
        break
    else :
        print("")
'''
