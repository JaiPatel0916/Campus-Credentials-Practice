class Emp:
    companyNmae="Tata"
    totalEmp=0

    def _init_(self, eid, name,):
        self.eid=eid
        self.name=name
        Emp.totalEmp+=1

e1=Emp(1, "A")
e2=Emp(2, "B")
e3=Emp(3, "C")
print(Emp.totalEmp)
print(e1.companyNmae)
print(e2.companyNmae)
print(e2.eid)