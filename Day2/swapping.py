# a=5
# b=3

# a,b=b,a

# print(a,b)


li=[78,45,1,96,38,2]

i=0
cnt=len(li)

while cnt-1:
    i=0
    while i<=cnt-2:
        if li[i] > li[i+1]:
            li[i],li[i+1] = li[i+1],li[i]
        i+=1
    cnt-=1
        

print(li)