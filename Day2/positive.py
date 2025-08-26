# Count positive, negative, and zero values in a list


li=[0,0,1,2,54,56,-9,-8,-2]
positivecont =0
negativecont =0
zerocont =0
for i in li:
    if i>0:
        positivecont+=1
    elif i<0:
        negativecont+=1
    else:
        zerocont+=1
print("Positive: ",positivecont)
print("Negative: ",negativecont)
print("Zero: ",zerocont)
                
        