'''
import mysql.connector as mc
z = mc.connect(host ="localhost",user="root",password="gj058555",database="namye")
print(z)
x = z.cursor()
y = int(input(""))
v = input("")
g = input("")
u = "insert into nam1 values('"+str(y)+"','"+v+"','"+g+"')"
w  = "delete from nam1 where first_name = 'namye'";
r = "drop table nam1;"
x.execute(r)
z.commit()      
import mysql.connector as ball
w = ball.connect(host = "localhost",user = "root",password = "gj058555",database = "namya")
print(w)
e = w.cursor()
print("1.add") 
print("2.remove") 
print("3.update") 
print("4.display")
q  = int(input(""))
if q==1 :
    t = int(input(""))
    y = input("")
    u = input("")
    i = "insert into nam1 values('"+str(t)+"','"+y+"','"+u+"')";
    e.execute(i)
    w.commit()
elif q==2 :
    o = "delete from nam1 where first_name = 'namya'";
    e.execute(o)
    w.commit()
elif q==3 :
    a = input("")
    s = input("")
    p = "update nam1 set first_name = '"+a+"' where first_name = '"+s+"' ;"
    e.execute(p)
    w.commit()
elif q==4 :
    d = "select * from nam1 ;"
    e.execute(d)
    data = e.fetchall()
    print(data)
'''
import mysql.connector as bat
z = bat.connect(host ="localhost",user="root",password="gj058555",database="Amazon")
print(z)
print("||[(AMAZON)]||")
try :
    while True :
        print("{1.Admin}")
        print("{2.Customer}")
        print("{3.Exit}")
        l = int(input(""))
        if l==1 :
            while True :
                try :
                    print("((ADMIN))")
                    print("_______________________________________________________________________________________")
                    print("{1.Login}")
                    print("{2.Register}")
                    print("{3.Exit}")
                
                    x = int(input(""))
                    if x==1 :
                        try :
                            x = z.cursor()
                            gmail = input("Enter Your Existing Gmail = ")
                            password = input("Enter Your Password = ")
                            w = "select * from users where gmail = '"+gmail+"' and password = '"+password+"' ;"
                            x.execute(w)
                            p = x.fetchall()
                            if len(p)>0 :
                                print("(Login Successfully)")
                                while True :
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
                                                x = z.cursor()  
                                                a = int(input("ID = "))
                                                name = input("Enter Your Product = ")
                                                details = int(input("Net Price ="))
                                                details1 = int(input("Net Quantity = "))
                                                details2 = input("Category = ")
                                                if int(details)>0 and int(details1)>0 :
                                                    q = "insert into product values('"+str(a)+"','"+name+"','"+str(details)+"','"+str(details1)+"','"+details2+"');"
                                                    x.execute(q)
                                                    z.commit()
                                                else :
                                                    print("(Value Not Supported)")
                                                    print("_______________________________________________________________________________________")
                                            except :
                                                print("(Invalid)")
                                                print("_______________________________________________________________________________________")
                                        elif p==2 :
                                            print("||Welcome To Remove||")
                                            print("_______________________________________________________________________________________")
                                            try :
                                                x = z.cursor()
                                                l = input("Enter Your Product = ")
                                                t = "delete from product where product_name = '"+l+"';"
                                                x.execute(t)
                                                z.commit()
                                                r = "select * from product where product_name = '"+l+"' ;"
                                                x.execute(r)
                                                p = x.fetchall()
                                                if len(p)>0 :
                                                    print("not removed")
                                                else :
                                                    print("removed")    
                                            except :
                                                print("(Invalid)")
                                                print("_______________________________________________________________________________________")
                                        elif p==3 :
                                            print("||Welcome To Update||")
                                            print("_______________________________________________________________________________________")
                                            try :
                                                x = z.cursor()
                                                s = input("Enter Your Product = ")
                                                name = input("Enter Your Product = ")
                                                details = int(input("Net Price ="))
                                                details1 = int(input("Net Quantity = "))
                                                details2 = input("Category = ")
                                                if int(details)>0 and int(details1)>0 :
                                                    g = "update product set product_name = '"+name+"',price = '"+str(details)+"',quantity = '"+str(details1)+"',category = '"+details2+"' where product_name = '"+s+"';" 
                                                    x.execute(g)
                                                    z.commit()
                                            except :
                                                print("(Invalid)")
                                                print("_______________________________________________________________________________________")
                                        elif p==4 :
                                            e = z.cursor()
                                            print("||Welcome To Display||")
                                            f = "select * from product ;"
                                            e.execute(f)
                                            l = e.fetchall()
                                            print(l)
                                        elif p==5 :
                                            print("{Exit}")
                                            print("_______________________________________________________________________________________")
                                            break
                                    except :
                                        print("(Invalid)")
                                        print("_______________________________________________________________________________________")
                            else :
                                print("(Login Unsuccessfully)")                
                        except Exception as e:
                            print(e)
                            print("_______________________________________________________________________________________")
                    elif x==2:
                        try :
                            x = z.cursor()
                            gmail = input("enter your gmail = ")
                            password = input("ener your password = ")
                            if "@" not in gmail:
                                raise ValueError("Invalid gmail format")
                            else:
                                Q = "insert into users values('"+gmail+"','"+password+"');"
                                x.execute(Q)
                                z.commit()
                        except ValueError as ve:
                            print(ve)
                            print("_______________________________________________________________________________________")
                    elif x==3 :
                        print("exit")
                        break
                except Exception as e:
                    print(e)
                    print("_______________________________________________________________________________________")
        elif l==2 :        
            while True :
                try :
                    print("((CUSTOMER))")
                    print("_______________________________________________________________________________________")
                    print("{1.Login}")
                    print("{2.Register}")
                    print("{3.Exit}")
                    x = int(input(""))
                    if x==1 :
                        try :
                            x = z.cursor()
                            gmail = input("Enter Your Existing Gmail = ")
                            password = input("Enter Your Password = ")
                            f = "select * from users1 where gmail = '"+gmail+"' and password = '"+password+"' ;"
                            x.execute(f)
                            p = x.fetchall()
                            if len(p)>0 :
                                print("(Login Successfull)")
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
                                            try :
                                                x = z.cursor()
                                                s = "select * from product ;"
                                                x.execute(s)
                                                p = x.fetchall()
                                                for i in p :
                                                    print("_______________________________________________________________________________________")
                                                    print("Product Name =  ",i[1])
                                                    print("Price =",i[2])
                                                    print("Product Quantity =",i[3])
                                                    print("Product Category =",i[4])
                                                    print("_______________________________________________________________________________________")
                                                d = "select * from product ; "
                                                m = input("Enter your Product to Search = ")
                                                x.execute(d)
                                                p = x.fetchall()
                                                c = 0
                                                for i in p :
                                                    if i[1]==m :
                                                        print("(Product Found)")
                                                        print("_______________________________________________________________________________________")
                                                        print("Product Name =  ",i[1])
                                                        print("Price =",i[2])
                                                        print("Product Quantity =",i[3])
                                                        print("Product Category =",i[4])
                                                        print("_______________________________________________________________________________________")
                                                        f = int(input("Enter How Much Quantity you Want = "))
                                                        if i[3]<f :
                                                            print("Not Available")
                                                            break
                                                        else :
                                                            if i[3]>f :
                                                                b = f*i[2]
                                                                v = i[3]-f
                                                                u = "update product set quantity = '"+str(v)+"'where product_name = '"+(i[1])+"' ;"
                                                                x.execute(u)
                                                                z.commit()
                                                                h = input("Do You Want To Add To Cart = ")
                                                                if h=="yes":
                                                                    print("(Product Added To cart Successfully)")
                                                                    j = "insert into cart values('"+str(i[0])+"','"+i[1]+"','"+str(i[2])+"','"+str(f)+"','"+i[4]+"') ;"
                                                                    x.execute(j)
                                                                    z.commit()
                                                                    break
                                                                else :
                                                                    print("(NO)")
                                                        break
                                                    c = c+1
                                                else :
                                                    print("(Product not Found )")
                                            except Exception as e :
                                                print(e)
                                                print("_______________________________________________________________________________________")
                                        elif l==2 :
                                            try :
                                                x = z.cursor()
                                                m = "select * from product;"
                                                a = input("Enter The Product To Search = ")
                                                x.execute(m)
                                                p = x.fetchall()
                                                c = 0
                                                for i in p :
                                                    if i[1]==a :
                                                        print("||Product Found||")
                                                        print("_______________________________________________________________________________________")
                                                        print("Product Name =  ",i[1])
                                                        print("Price =",i[2])
                                                        print("Product Quantity =",i[3])
                                                        print("Product Category =",i[4])
                                                        print("_______________________________________________________________________________________")
                                                        f = int(input("How much Quantity = "))
                                                        if i[3]<f :
                                                            print("Not Available")
                                                            break
                                                        else :
                                                            if i[3]>f :
                                                                b = f*i[2]
                                                                v = i[3]-f
                                                                u = "update product set quantity = '"+str(v)+"'where product_name = '"+(i[1])+"' ;"
                                                                x.execute(u)
                                                                z.commit()
                                                                h = input("Do You Want To Add To Cart = ")
                                                                if h=="yes":
                                                                    print("(Product Added To cart Successfully)")
                                                                    j = "insert into cart values('"+str(i[0])+"','"+i[1]+"','"+str(i[2])+"','"+str(f)+"','"+i[4]+"') ;"
                                                                    x.execute(j)
                                                                    z.commit()
                                                                    break
                                                                else :
                                                                    print("(NO)")
                                                        break
                                                    c = c+1
                                                else :
                                                    print("||Product Not Found||")
                                            except Exception as e :
                                                print(e)
                                                print("_______________________________________________________________________________________")
                                        elif l==3 :
                                            try :
                                                x = z.cursor()
                                                d = "select * from product order by price ASC"
                                                x.execute(d)
                                                p = x.fetchall()
                                                for i in p :
                                                    print("_______________________________________________________________________________________")
                                                    print("Product Name =  ",i[1])
                                                    print("Price =",i[2])
                                                    print("Product Quantity =",i[3])
                                                    print("Product Category =",i[4])
                                                    print("_______________________________________________________________________________________")
                                                m = "select * from product;"
                                                a = input("Enter The Product To Search = ")
                                                x.execute(m)
                                                p = x.fetchall()
                                                c = 0
                                                for i in p :
                                                    if i[1]==a :
                                                        print("||Product Found||")
                                                        print("_______________________________________________________________________________________")
                                                        print("Product Name =  ",i[1])
                                                        print("Price =",i[2])
                                                        print("Product Quantity =",i[3])
                                                        print("Product Category =",i[4])
                                                        print("_______________________________________________________________________________________")
                                                        f = int(input("How much Quantity = "))
                                                        if i[3]<f :
                                                            print("Not Available")
                                                            break
                                                        else :
                                                            if i[3]>f :
                                                                b = f*i[2]
                                                                v = i[3]-f
                                                                u = "update product set quantity = '"+str(v)+"'where product_name = '"+(i[1])+"' ;"
                                                                x.execute(u)
                                                                z.commit()
                                                                h = input("Do You Want To Add To Cart = ")
                                                                if h=="yes":
                                                                    print("(Product Added To cart Successfully)")
                                                                    j = "insert into cart values('"+str(i[0])+"','"+i[1]+"','"+str(i[2])+"','"+str(f)+"','"+i[4]+"') ;"
                                                                    x.execute(j)
                                                                    z.commit()
                                                                    break
                                                                else :
                                                                    print("(NO)")
                                                        break
                                                    c = c+1
                                                else :
                                                    print("||Product Not Found||")
                                            except Exception as e :
                                                print(e)
                                                print(_______________________________________________________________________________________)
                                        elif l==4 :
                                            try :
                                                x = z.cursor()
                                                d = "select * from product order by price DESC"
                                                x.execute(d)
                                                p = x.fetchall()
                                                for i in p :
                                                    print("_______________________________________________________________________________________")
                                                    print("Product Name =  ",i[1])
                                                    print("Price =",i[2])
                                                    print("Product Quantity =",i[3])
                                                    print("Product Category =",i[4])
                                                    print("_______________________________________________________________________________________")
                                                m = "select * from product;"
                                                a = input("Enter The Product To Search = ")
                                                x.execute(m)
                                                p = x.fetchall()
                                                c = 0
                                                for i in p :
                                                    if i[1]==a :
                                                        print("||Product Found||")
                                                        print("_______________________________________________________________________________________")
                                                        print("Product Name =  ",i[1])
                                                        print("Price =",i[2])
                                                        print("Product Quantity =",i[3])
                                                        print("Product Category =",i[4])
                                                        print("_______________________________________________________________________________________")
                                                        f = int(input("How much Quantity = "))
                                                        if i[3]<f :
                                                            print("Not Available")
                                                            break
                                                        else :
                                                            if i[3]>f :
                                                                b = f*i[2]
                                                                v = i[3]-f
                                                                u = "update product set quantity = '"+str(v)+"'where product_name = '"+(i[1])+"' ;"
                                                                x.execute(u)
                                                                z.commit()
                                                                h = input("Do You Want To Add To Cart = ")
                                                                if h=="yes":
                                                                    print("(Product Added To cart Successfully)")
                                                                    j = "insert into cart values('"+str(i[0])+"','"+i[1]+"','"+str(i[2])+"','"+str(f)+"','"+i[4]+"') ;"
                                                                    x.execute(j)
                                                                    z.commit()
                                                                    break
                                                                else :
                                                                    print("(NO)")
                                                        break
                                                    c = c+1
                                                else :
                                                    print("||Product Not Found||")
                                            except Exception as e :
                                                print(e)
                                                print("_______________________________________________________________________________________")
                                        elif l==5 :
                                            try :
                                                x = z.cursor()
                                                m = "select * from product ;"
                                                d = input("Enter The category To Search = ")
                                                x.execute(m)
                                                p = x.fetchall()
                                                for i in p:
                                                    if i[4]==d:
                                                        print("_______________________________________________________________________________________")
                                                        print("Product Name = ",i[1])
                                                        print("Price =",i[2])
                                                        print("Product Quantity =",i[3])
                                                        print("Product Category =",i[4])
                                                        print("_______________________________________________________________________________________")
                                                n = "select * from product;"
                                                a = input("Enter The Product To Search = ")
                                                x.execute(n)
                                                p = x.fetchall()
                                                c = 0
                                                for i in p :
                                                    if i[1]==a :
                                                        print("||Product Found||")
                                                        print("_______________________________________________________________________________________")
                                                        print("Product Name =  ",i[1])
                                                        print("Price =",i[2])
                                                        print("Product Quantity =",i[3])
                                                        print("Product Category =",i[4])
                                                        print("_______________________________________________________________________________________")
                                                        f = int(input("How much Quantity = "))
                                                        if i[3]<f :
                                                            print("Not Available")
                                                            break
                                                        else :
                                                            if i[3]>f :
                                                                b = f*i[2]
                                                                v = i[3]-f
                                                                u = "update product set quantity = '"+str(v)+"'where product_name = '"+(i[1])+"' ;"
                                                                x.execute(u)
                                                                z.commit()
                                                                h = input("Do You Want To Add To Cart = ")
                                                                if h=="yes":
                                                                    print("(Product Added To cart Successfully)")
                                                                    j = "insert into cart values('"+str(i[0])+"','"+i[1]+"','"+str(i[2])+"','"+str(f)+"','"+i[4]+"') ;"
                                                                    x.execute(j)
                                                                    z.commit()
                                                                    break
                                                                else :
                                                                    print("(NO)")
                                                        break
                                                    c = c+1
                                                else :
                                                    print("||Product Not Found||")
                                            except Exception as e :
                                                print("e")
                                                print("_______________________________________________________________________________________")
                                        elif l==6 :
                                            x = z.cursor()
                                            k = "select * from cart ;"
                                            x.execute(k)
                                            p = x.fetchall()
                                            for i in p:
                                                print("_______________________________________________________________________________________")
                                                print("Product Name = ",i[1])
                                                print("Price =",i[2])
                                                print("Product Quantity =",i[3])
                                                print("Product Category =",i[4])
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
                            else :
                                print("(Login Unsuccessfully)")
                        except Exception as e :
                            print("e")
                            print("_______________________________________________________________________________________")
                    elif x==2:
                        try :
                            x = z.cursor()
                            gmail = input("Enter Your Gmail = ")
                            password = input("Enter Your Password = ")
                            if "@" not in gmail :
                                raise ValueError("Invalid gmail format")
                            else :
                                g = "insert into users1 values('"+gmail+"','"+password+"');"
                                x.execute(g)
                                z.commit()
                        except ValueError as ve :
                            print(ve)
                            print("_______________________________________________________________________________________")
                    elif x==3 :
                        print("{Exit}")
                        break
                except Exception as e :
                    print(e)
                    print("_______________________________________________________________________________________")
        elif l==3 :
            print("{BYEEEE}")
            break
except:
    print("(Invalid)")
    print("_______________________________________________________________________________________")