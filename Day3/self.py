class Ex:
    def acceptData(self,a):
        self.roll = a
        
    def showData(self):
        print(self.roll)

e1=Ex()

e1.acceptData(5)

e1.showData()