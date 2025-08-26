li=[25,21,7,13,17,8,96,1]
p=[]

for no  in li:
    flag=False
    for i in range(2,no):
        if no%i==0:
            # print("Number is not prime")
            flag=True
            break

    if flag==False:
        p.append(no)
        # print("Number is  prime")

print(p)    