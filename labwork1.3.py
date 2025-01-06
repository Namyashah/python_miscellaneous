'''
#1
a = input("")
b = int(a)
print(type(b))

b = float(a)
print(type(b))


a = input("")
boolvalue = a.lower() == a  
print(boolvalue)
  
#2
a = float(input(""))
b = int(a)
print(b)
print(type(b))
print(a)
print(type(a))

#3
bool_value = input("bool = ")
if bool_value=="True" :
    bool_value = True 
elif bool_value=="False" :
    bool_value = False
else :
    raise ValueError("Invalid boolean value! Please enter True or False.")

str_value = str(bool_value)
int_value = int(bool_value)
print(str_value)
print(int_value)
print(bool_value)

#4
a = int(input(""))
print(a)
print(type(a))
print(id(a))

a = float(input(""))
print(a)
print(type(a))
print(id(a))

a = input("")
print(a)
print(type(a))
print(id(a))

bool_value = input("bool = ")
if bool_value=="True" :
    bool_value = True 
elif bool_value=="False" :
    bool_value = False
print(bool_value)
print(type(bool_value))
print(id(bool_value))

lst = [1,2,3,4,5,6,7]
print(lst)
print(type(lst))
print(id(lst))

tple = (2,3,4,5,6,7)
print(tple)
print(type(tple))
print(id(tple))

dict = {"key":1,"keys":2}
print(dict)
print(type(dict))
print(id(dict))


#5
a = int(input(""))
b = float(input(""))
print(id(a))
print(id(b))
'''