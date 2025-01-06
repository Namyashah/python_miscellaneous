'''
while True :
    z = [1,2,3,4,5,6,7,8,2,3,2,1,1]
    print("1.append")
    print("2.remove")
    print("3.update")
    print("4.display")
    print("5.exit")
    x = int(input(""))
    if x==1 :
        y = int(input(""))
        z.append(y)
        print(z)
    elif x==2 :
        y = int(input(""))
        if y in z :
            print("FOUND",end="")
            print()
            z.remove(y)
            print(z)
        else :
            print("NOT FOUND",end="")
    elif x==3 :
        y = int(input(""))
        if y in z :
            print("FOUND",end="")
            print()
            index = z.index(y)
            z[index] = int(input(""))
            print(z)
        else :
            print("NOT FOUND",end="")
    elif x==4 :
        print(z)
    elif x==5 :
        print("byeee",end="")
        break
'''
lst = [{1},{2},{3},{4}]
lst.sort(dict)
print(lst)        
print(dir(lst))