print("||[(AMAZON)]||")
amazon = [{'product': 'google 9', 'price': 78000, 'quantity': 10, 'category': 'cellphone'}, {'product': ' hp victus(24,1tb)', 'price': 90000, 'quantity': 10, 'category': 'laptop'}, {'product': 'rare rabit(white shirt)', 'price': 500, 'quantity': 50, 'category': 'clothes'}, {'product': 'jack and jones(grey pants)', 'price': 1800, 'quantity': 50, 'category': 'clothes'}, {'product': 'iphone 16 pro ', 'price': 98000, 'quantity': 40, 'category': 'cellphone'}, {'product': 'lenovo legion(16,1tb)', 'price': 140000, 'quantity': 25, 'category': 'laptop'}, {'product': 'samsung zfold', 'price': 150000, 'quantity': 40, 'category': 'cellphone'}, {'product': 'tommy hillfiger(shorts)', 'price': 1200, 'quantity': 500, 'category': 'clothes'}]
admin = []
customer = []
cart = []
while True :
    print("{1.Admin}")
    print("{2.Customer}")
    print("{3.Exit}")
    try :
        l = int(input(""))
        if l==1 :
            while True :
                print("((ADMIN))")
                print("_______________________________________________________________________________________")
                print("{1.Login}")
                print("{2.Register}")
                print("{3.Exit}")
                try :
                    x = int(input(""))
                    if x==1 :
                        k = 0
                        try :
                            gmail = input("Enter Your Existing Gmail = ")
                            password = input("Enter Your Password = ")
                        except :
                            print("(Invalid)")
                            print("_______________________________________________________________________________________")
                        for i in admin :
                            if i["y"]==gmail and i["z"]==password :
                                k = 1
                                print("(Login Successfully)")
                                print("_______________________________________________________________________________________")
                                print("_______________________________________________________________________________________")
                                while True:
                                    print("[[1.Add]]")
                                    print("[[2.Remove]]")
                                    print("[[3.Update]]")
                                    print("[[4.Display]]")
                                    print("[[5.Exit]]")
                                    try :
                                        p = int(input(""))
                                        if p==1 :
                                            print("||Welcome To Add||")
                                            print("_______________________________________________________________________________________")
                                            dict = {}
                                            try :
                                                name = input("Enter Your Product = ")
                                                details = int(input("Net Price ="))
                                                details1 = int(input("Net Quantity = "))
                                                details2 = input("Category = ")
                                            except :
                                                print("(Invalid)")
                                                print("_______________________________________________________________________________________")
                                            if int(details)>0 and int(details1)>0 :
                                                dict["product"] = name
                                                dict["price"] = details
                                                dict["quantity"] = details1
                                                dict["category"] = details2
                                                amazon.append(dict)
                                            else :
                                                print("(Value Not Supported)")
                                            print(amazon)
                                            print("_______________________________________________________________________________________")
                                        elif p==2 :
                                            print("||Welcome To Remove||")
                                            print("_______________________________________________________________________________________")
                                            c = 0
                                            try :
                                                z = input("Enter Your Product = ")
                                            except :
                                                print("(Invalid)")
                                                print("_______________________________________________________________________________________")
                                            for i in amazon :
                                                if i["product"]==z :
                                                    amazon.pop(c)
                                                    print("(Remote Successfully)")
                                                    print(amazon)
                                                    print("_______________________________________________________________________________________")
                                                    break
                                                c = c+1
                                            else :
                                                print("||Product Not Found||")
                                        elif p==3 :
                                            print("||Welcome To Update||")
                                            print("_______________________________________________________________________________________")
                                            c = 0
                                            dict = {}
                                            try :
                                                s = input("Enter Your Product = ")
                                            except :
                                                print("(Invalid)")
                                                print("_______________________________________________________________________________________")
                                            for i in amazon :
                                                if i["product"]==s :
                                                    print("(Found)")
                                                    try :
                                                        name = input("Enter Your Product = ")
                                                        details = int(input("Net Price ="))
                                                        details1 = int(input("Net Quantity = "))
                                                        details2 = input("Category = ")
                                                    except :
                                                        print("(Invalid)")
                                                        print("_______________________________________________________________________________________")
                                                    if int(details)>0 and int(details1)>0 :
                                                        dict["product"] = name
                                                        dict["price"] = details
                                                        dict["quantity"] = details1
                                                        dict["category"] = details2
                                                        amazon[c] = dict
                                                        print(amazon)
                                                        print("_______________________________________________________________________________________")
                                                        break
                                                c = c+1
                                            else :
                                                print("||Product Not Found||")
                                        elif p==4 :
                                            print("||Welcome To Display||")
                                            print("_______________________________________________________________________________________")
                                            print(amazon)
                                            print("_______________________________________________________________________________________")
                                        elif p==5 :
                                            print("{Exit}")
                                            print("_______________________________________________________________________________________")
                                            break
                                    except :
                                        print("(Invalid)")
                                        print("_______________________________________________________________________________________")
                        if k==0 :
                            print("(Login Unsuccessfully)")                
                    elif x==2:
                        dict = {}
                        try :
                            gmail = input("enter your gmail = ")
                            password = input("ener your password = ")
                        except :
                            print("(Invalid)")
                            print("_______________________________________________________________________________________")
                        dict["y"] = gmail
                        dict["z"] = password 
                        print(dict)
                        admin.append(dict)
                        print(admin)
                    elif x==3 :
                        print("exit")
                        break
                except:
                    print("(Invalid)")
                    print("_______________________________________________________________________________________")
        elif l==2 :        
            while True :
                print("((CUSTOMER))")
                print("_______________________________________________________________________________________")
                print("{1.Login}")
                print("{2.Register}")
                print("{3.Exit}")
                try :
                    x = int(input(""))
                    if x==1 :
                        k = 0
                        try :
                            gmail = input("Enter Your Existing Gmail = ")
                            password = input("Enter Your Password = ")
                        except :
                            print("(Invalid)")
                            print("_______________________________________________________________________________________")
                        for i in customer :
                            if i["y"]==gmail and i["z"]==password :
                                k = 1
                                print("(Login Successfully)")
                                print("_______________________________________________________________________________________")
                                print("_______________________________________________________________________________________")
                                while True :
                                    print("[[1.View Products]]")
                                    print("[[2.Search Products]]")
                                    print("[[3.Low To High]]")
                                    print("[[4.High To Low]]")
                                    print("[[5.Search By Category]]")
                                    print("[[6.Add To Cart]]")
                                    print("[[7.Help]]")
                                    print("[[8.Exit]]")                                
                                    try :
                                        l = int(input(""))
                                        if l==1:
                                            for i in amazon:
                                                print("_______________________________________________________________________________________")
                                                print("Product Name = ",i["product"])
                                                print("Price =",i["price"])
                                                print("Product Quantity =",i["quantity"])
                                                print("Product Category =",i["category"])
                                                print("_______________________________________________________________________________________")
                                            try :
                                                a = input("Enter The Product To Search = ")
                                            except :
                                                print("(Invalid)")
                                                print("_______________________________________________________________________________________")
                                            c = 0
                                            for i in amazon :
                                                if i["product"]==a :
                                                    print("||Product Found||")
                                                    try :
                                                        r = int(input("How much Quantity = "))
                                                    except :
                                                        print("(Invalid)")
                                                        print("_______________________________________________________________________________________")
                                                    if i["quantity"]<r :
                                                        print("Not Available")
                                                        break
                                                    else :
                                                        if i["quantity"]>=r :
                                                            z = r*i["price"]
                                                            i["quantity"]=i["quantity"]-r                                                
                                                            print({z})
                                                            try :
                                                                u = input("Do You Want To Add To Cart = ")
                                                            except :
                                                                print("(Invalid)")
                                                                print("_______________________________________________________________________________________")
                                                            if u=="yes" :
                                                                cart.append(i)
                                                                print("(Product Added To Cart Successfully)")
                                                                print("_______________________________________________________________________________________")
                                                                break
                                                c = c+1
                                            else :
                                                print("||Product Not Found||")
                                        elif l==2 :
                                            print("_______________________________________________________________________________________")
                                            try :
                                                a = input("Enter The Product To Search = ")
                                            except :
                                                print("(Invalid)")
                                                print("_______________________________________________________________________________________")
                                            c = 0
                                            for i in amazon :
                                                if i["product"]==a :
                                                    print("||Product Found||")
                                                    print("_______________________________________________________________________________________")
                                                    print("Product Name =  ",i["product"])
                                                    print("Price =",i["price"])
                                                    print("Product Quantity =",i["quantity"])
                                                    print("Product Category =",i["category"])
                                                    print("_______________________________________________________________________________________")
                                                    try :
                                                        r = int(input("How much Quantity = "))
                                                    except :
                                                        print("(Invalid)")
                                                        print("_______________________________________________________________________________________")
                                                    if i["quantity"]<r :
                                                        print("Not Available")
                                                        break
                                                    else :
                                                        if i["quantity"]>=r :
                                                            z = r*i["price"]
                                                            i["quantity"]=i["quantity"]-r                                                
                                                            print({z})
                                                            try :
                                                                u = input("Do You Want To Add To Cart = ")
                                                            except :
                                                                print("(Invalid)")
                                                                print("_______________________________________________________________________________________")
                                                            if u=="yes" :
                                                                cart.append(i)
                                                                print("(Product Added To Cart Successfully)")
                                                                print("_______________________________________________________________________________________")
                                                                break 
                                                c = c+1
                                            else :
                                                print("||Product Not Found||")
                                        elif l==3 :
                                            lst = []
                                            for i in amazon :
                                                lst.append(i["price"])
                                            lst.sort()
                                            for i in lst:
                                                for j in amazon:
                                                    if i==j["price"]:
                                                        print("_______________________________________________________________________________________")
                                                        print("Product Name = ",j["product"])
                                                        print("Price =",j["price"])
                                                        print("Product Quantity =",j["quantity"])
                                                        print("Product Category =",j["category"])
                                                        print("_______________________________________________________________________________________")
                                            try :
                                                a = input("Enter The Product To Search = ")
                                            except :
                                                print("(Invalid)")
                                                print("_______________________________________________________________________________________")
                                            c = 0
                                            for i in amazon :
                                                if i["product"]==a :
                                                    print("||Product Found||")
                                                    try :
                                                        r = int(input("How much Quantity = "))
                                                    except :
                                                        print("(Invalid)")
                                                        print("_______________________________________________________________________________________")
                                                    if i["quantity"]<r :
                                                        print("Not Available")
                                                        break
                                                    else :
                                                        if i["quantity"]>=r :
                                                            z = r*i["price"]
                                                            i["quantity"]=i["quantity"]-r
                                                            print({z})
                                                            try :
                                                                u = input("Do You Want To Add To Cart = ")
                                                            except :
                                                                print("(Invalid)")
                                                                print("_______________________________________________________________________________________")
                                                            if u=="yes" :
                                                                cart.append(i)
                                                                print("(Product Added To Cart Successfully)")
                                                                break
                                                c = c+1
                                            else :
                                                print("||Product Not Found||")
                                        elif l==4 :
                                            lst = []
                                            for i in amazon :
                                                lst.append(i["price"])
                                            lst.sort(reverse=True)
                                            for i in lst:
                                                for j in amazon:
                                                    if i==j["price"]:
                                                        print("_______________________________________________________________________________________")
                                                        print("Product Name = ",j["product"])
                                                        print("Price =",j["price"])
                                                        print("Product Quantity =",j["quantity"])
                                                        print("Product Category =",j["category"])
                                                        print("_______________________________________________________________________________________")
                                            try :
                                                a = input("Enter The Product To Search = ")
                                            except :
                                                print("(Invalid)")
                                                print("_______________________________________________________________________________________")
                                            c = 0
                                            for i in amazon :
                                                if i["product"]==a :
                                                    print("||Product Found||")
                                                    try :
                                                        r = int(input("How much Quantity = "))
                                                    except :
                                                        print("(Invalid)")
                                                        print("_______________________________________________________________________________________")
                                                    if i["quantity"]<r :
                                                        print("Not Available")
                                                        break
                                                    else :
                                                        if i["quantity"]>=r :
                                                            z = r*i["price"]
                                                            i["quantity"]=i["quantity"]-r
                                                            print({z})
                                                            try :
                                                                u = input("Do You Want To Add To Cart = ")
                                                            except :
                                                                print("(Invalid)")
                                                                print("_______________________________________________________________________________________")
                                                            if u=="yes" :
                                                                cart.append(i)
                                                                print("(Product Added To Cart Successfully)")
                                                                break
                                                c = c+1
                                            else :
                                                print("||Product Not Found||")
                                        elif l==5 :
                                            print("_______________________________________________________________________________________")
                                            try :
                                                p = input("Enter The Category To Search = ")
                                            except :
                                                print("(Invalid)")
                                                print("_______________________________________________________________________________________")
                                            for i in amazon:
                                                if i["category"]==p:
                                                        print("_______________________________________________________________________________________")
                                                        print("Product Name = ",i["product"])
                                                        print("Price =",i["price"])
                                                        print("Product Quantity =",i["quantity"])
                                                        print("Product Category =",i["category"])
                                                        print("_______________________________________________________________________________________")
                                            try :
                                                a = input("Enter The Product To Search = ")
                                            except :
                                                print("(Invalid)")
                                                print("_______________________________________________________________________________________")
                                            c = 0
                                            for i in amazon :
                                                if i["product"]==a :
                                                    print("||Product Found||")
                                                    try :
                                                        r = int(input("How much Quantity = "))
                                                    except :
                                                        print("(Invalid)")
                                                        print("_______________________________________________________________________________________")
                                                    if i["quantity"]<r :
                                                        print("Not Available")
                                                        break
                                                    else :
                                                        if i["quantity"]>=r :
                                                            z = r*i["price"]
                                                            i["quantity"]=i["quantity"]-r
                                                            print({z})
                                                            try :
                                                                u = input("Do You Want To Add To Cart = ")
                                                            except :
                                                                print("(Invalid)")
                                                                print("_______________________________________________________________________________________")
                                                            if u=="yes" :
                                                                cart.append(i)
                                                                print("(Product Added To Cart Successfully)")
                                                                break
                                                c = c+1
                                            else :
                                                print("||Product Not Found||")
                                        elif l==6 :
                                            for i in cart:
                                                print("_______________________________________________________________________________________")
                                                print("Product Name = ",i["product"])
                                                print("Price =",i["price"])
                                                print("Product Quantity =",i["quantity"])
                                                print("Product Category =",i["category"])
                                                print("_______________________________________________________________________________________")
                                        elif l==7 :
                                            print("_______________________________________________________________________________________")
                                            print("[For Any Query Contact Namya Shah]")
                                            print("_______________________________________________________________________________________")
                                            print("[Email Address = namyashah0508@gmail.com]")
                                            print("_______________________________________________________________________________________")
                                            print("[Contact Number = 9824168444]")
                                            print("_______________________________________________________________________________________")
                                        elif l==8 :
                                            break
                                    except :
                                        print("(Invalid)")
                                        print("_______________________________________________________________________________________")
                        if k==0 :
                            print("(Login Unsuccessfully)")
                    elif x==2:
                        dict = {}
                        try :
                            gmail = input("Enter Your Gmail = ")
                            password = input("Enter Your Password = ")
                        except :
                            print("(Invalid)")
                            print("_______________________________________________________________________________________")
                        dict["y"] = gmail
                        dict["z"] = password 
                        print(dict)
                        customer.append(dict)
                        print(customer)
                    elif x==3 :
                        print("{Exit}")
                        break
                except :
                    print("(Invalid)")
                    print("_______________________________________________________________________________________")
        elif l==3 :
            print("{BYEEEE}")
            break
    except:
        print("(Invalid)")
        print("_______________________________________________________________________________________")