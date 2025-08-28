from abc import ABC , abstractmethod

class Boss(ABC):
    @abstractmethod
    def task1():
        pass
    
    def salary(self):
        print("90k")
        
        
class emp(Boss):
    def task1(self):
        print("Complete")
        
e=emp()
e.task1()
e.salary()
        
    