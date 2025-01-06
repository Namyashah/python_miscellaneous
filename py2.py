import pickle
'''
x = open("one1.txt","ab")

pickle.dump("bye",x)
x.close()
'''
x = open("one1.txt","rb")

try:
    while True:
        print(pickle.load(x))
        
except:
        print("END of the file")
# print(pickle.load(x))
x.close()

