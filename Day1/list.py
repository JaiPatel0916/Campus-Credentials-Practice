# 1st method
# x = [1,2,3,4,5,6]

# y=[]

# for i in x:
#     y.append(i)
    
# x[0] = 9
    
# print(x)
# print(y)
    
'''2nd method
 x=[5,10,15,20]

 y=[i for i in x]

 x[0]=8
 print(x)
 print(y)'''
 
''' 3rd method 
x=[5,10,15,20]

y=x.copy()
x[0] = 8 

print(x)
print(y)'''


# x=[[1,2],[3,4],[5,6]]


# y = [j if j%2 == 0 else 0 for i in x for j in i ]
# print(y)

i=range(2,51)
print ( i for i in i  for i in range(2,51) if i%i==0 and i%1 == 1 )
 