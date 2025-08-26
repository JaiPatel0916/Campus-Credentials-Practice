''' 
def add(a,b):
    print("A:",a)
    print ("B:", b)
    print(a+b)
    

add(3,6)'''


''' Overwriting a function
def add(a,b):
    print(a+b)
    

def add(a,b,c):
    print(a+b+c)
    

add(1,2,3) '''


''' 3rd
def add(a,*b):
    print(a)
    print(b)
    
add(1,2,3,4,5,6)
'''

''' 4th 
use of split()
x="Hello coders how are you"

y=x.split()
print(y)'''

''' 5th
use of join()
x=["Hello", "Jai","Patel"];
y=" ".join(x)

print(y)'''

''' 6th
def add(a:int,b:int)->int:
    return(a+b)

print(add(3,5))
print(add(3.21,8.2))

'''

''' sort(), sorted(), min(),max()
x=[5,7,8,1,0,6]
x.sort()
print(x)
y=sorted(x)
print(y)

print(min(x))
print(max(x))
'''

''' sorting of string
x=["rashi","jai","shivam","ansh"]
x.sort()
print(x)'''




x=[5,10,20,40,60,20,20,20,20]

# for i,data in enumerate(x):
#     if data == 20:
#         print(i)

for i in range(len(x)):
    if x[i] == 20:
        print(i, end="\n")
    
