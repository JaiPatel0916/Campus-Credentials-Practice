# class Ex:
#     def acceptData(self,a):
#         self.roll = a
        
#     def showData(self):
#         print(self.roll)

# e1=Ex()

# e1.acceptData(5)

# e1.showData()


class Ex:

    def acp(self, x, y):
        self.a = x
        self.b = y

    def cal(self, e1):
        self.a = e1.a + self.a
        self.b = e1.b + self.b

    def dsp(self):
        print(self.a, "\t", self.b)


# main part
e1 = Ex()
e2 = Ex()

e1.acp(3, 4)
e2.acp(10, 20)

e2.cal(e1)
e2.dsp()