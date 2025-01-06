question =[{'questionn': 'which one is flower', 'option': ['rose', 'lotus', 'krish', 'namya'], 'right answer': 'lotus'}, {'questionn': 'salary of an employee', 'option': ['12000', '3000', '20000', '10000'], 'right answer': '3000'}, {'questionn': 'who is who', 'option': ['namya', 'yug', 'adish', 'akshit'], 'right answer': 'yug'}, {'questionn': 'core of laptop', 'option': ['i5', 'i7', 'i9', 'i11'], 'right answer': 'i7'}]
teacher =[]
student =[]
while True :
    print("1.teacher")
    print("2.student")
    print("0.exit")
    
    l = int(input(""))
    if l==1 :    
        while True :
            print("teacher")
            print("1.login")
            print("2.registar")
            print("3.exit")
            x = int(input(""))
            if x==1 :
                k = 0
                gmail = input("enter your existing gmail = ")
                password = input("enter your password = ")            
                for i in teacher: 
                    if i["y"]==gmail and i["z"]==password :
                        k = 1
                        print("login successfull")
                        while True :
                            print("1.add")
                            print("2.remove")
                            print("3.update")
                            print("4.display")
                            print("5.exit")
                            
                            u = int(input("enter your choice = "))
                            if u==1 :
                                print("welcome to add")
                                dict = {}
                                ab = input("enter your question = ")
                                op1 = input("")
                                op2 = input("")
                                op3 = input("")
                                op4 = input("")
                                t = input("")
                                if t==op1 or t==op2 or t==op3 or t==op4 :
                                        print("correct")
                                        dict["questionn"] = ab
                                        dict["option"] = [op1,op2,op3,op4]
                                        dict["right answer"] = t
                                        question.append(dict)
                                else :
                                    print("incorrect")
                                
                                print(question)
                            elif u==2 :
                                print("welcome to remove")
                                c = 0
                                z = input("enter your Q for remove = ")
                                for i in question :
                                    if i["questionn"]==z :
                                        question.pop(c)
                                        print("remote successfull")
                                        print(question)
                                        break 
                                    c = c+1
                                else :
                                    print("not found")
                            elif u==3 :
                                c = 0
                                dict = {}
                                print("welcome to update")
                                z = input("enter your question = ")
                                for i in question :
                                    if i["questionn"]==z :
                                        print("found")
                                        ab = input("enter your question = ")
                                        op1 = input("")
                                        op2 = input("")
                                        op3 = input("")
                                        op4 = input("")
                                        t = input("")                                        
                                        dict["questionn"] = ab
                                        dict["option"] = [op1,op2,op3,op4]
                                        dict["right answer"] = t
                                        question[c] = dict
                                        print(question)
                                        break 
                                    c = c+1
                                else :
                                    print("not found")
                            elif u==4 :
                                print("welcome to display")
                                print(question)
                            elif u==5 :
                                print("exit")
                                break 
                        break
                if k==0 :
                    print("login unsuccessful")
            elif x==2 :
                dict = {}
                gmail = input("enter your gmail = ")
                password = input("enter your password = ")
                dict["y"] = gmail
                dict["z"] = password
                print(dict)
                teacher.append(dict)
                print(teacher)
            elif x==3 :
                print("exit")
                break
    elif l==2 :
        while True:
            print("student")
            print("1.login")
            print("2.registar")
            print("3.exit")
            x = int(input(""))
            if x==1 :
                k = 0
                gmail = input("enter your existing gmail = ")
                password = input("enter your password = ")    
                total=0
                for i in student: 
                    if i["y"]==gmail and i["z"]==password :
                        k = 1
                        print("login successfull")   
                        for i in question :
                            print(i["questionn"])
                            print(i["option"][0])
                            print(i["option"][1])
                            print(i["option"][2])
                            print(i["option"][3])
                            rop = input("enter your right op = ")
                            if rop==i["right answer"]:
                                    total = total+1
                        print("your total score is = ",total,"/",len(question))
                        break 
                if k==0 :
                    print("login unsuccessful")
            elif x==2 :
                dict = {}
                gmail = input("enter your gmail = ")
                password = input("enter your password = ")
                dict["y"] = gmail
                dict["z"] = password
                print(dict)
                student.append(dict)
                print(student)
            elif x==3 :
                print("exit")
                break
    elif l==0 :
        print("bye")
        break