class Student:
    
    cn="SBJ" # staic variable is used to create a single copy that is used throughout the program
    def __init__(self, roll,name,m1,m2,m3):
        self.roll=roll
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
    # def dis(self):
    #     print("roll",self.roll)
    #     print("name",self.name)
    #     print("m1",self.m1)
    #     print("m2",self.m2)
    #     print("m3",self.m3)


s1= Student(99,"Jai",77,88,99)
s2= Student(100,"Rashi",77,88,99)

print(s1.cn)
print(s2.cn)
print(Student.cn)

    
    
