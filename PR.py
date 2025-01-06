print("Welcome to the Pattern Generator and Number Analyzer")
print("______________________________________________________________________________________________________________")
while True :
    print("1.Generate a pattern")
    print("2.analyze a range of numbers")
    print("3.Exit")
    print("______________________________________________________________________________________________________________")
    l = int(input("Enter your choice = "))
    print("______________________________________________________________________________________________________________")
    if l==1 :
        print("Choose your pattern type : ")
        print("1.Right angle traingle")
        print("2.traingle")
        print("3.left angle traingle")
        
        print("______________________________________________________________________________________________________________")
        r = int(input("Enter your choice = "))
        t = int(input("Enter the number of rows for the patterns = "))
        if r==1 :
            for i in range(1,t+1):
                for j in range(1,i+1):
                    print("*",end = "",sep = "")
                print()
        elif r==2 :
            for i in range(1,t+1):
                for k in range(t,i,-1):
                    print(" ",end = "",sep = "")
                for j in range(1,i+1):
                    print("* ",end = "",sep = "")
                print()
        elif r==3 :
            for i in range(1,t+1):
                for k in range(t,i,-1):
                    print(" ",end = "",sep = "")
                for j in range(1,i+1):
                    print("*",end = "",sep = "")
                print()
        else :
            print("______________________________________________________________________________________________________________")
            print("(invalid)")
    elif l==2 :
        total = 0
        q = int(input("Enter the start of the range = "))
        w = int(input("Enter the end of the range = "))
        print("______________________________________________________________________________________________________________")
        for i in range(q,w+1):
            if i%2==0 :
                print(i,"is even")
            else :
                print(i,"is odd")
            total = total +i
        print(total)
        break                
    elif l==3 :
        print("Exiting the program Goodbye")
        break
    else :
        print("(sorry invalid)")
        print("______________________________________________________________________________________________________________")