# 2nd example 

# Task: Create an abstract class Appliance with:

# turn_on() → abstract

# brand() → normal method that prints brand name
# Create Fan and WashingMachine classes implementing turn_on().


from abc import ABC, abstractmethod
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    def brand(self):
        print("LG")
class Fan(Appliance):
    def turn_on(self):
        print("Fan on")
class WashingMachine(Appliance):
    def turn_on(self):
        print("Washing Machine is on")
f=Fan()
w=WashingMachine()
f.turn_on()
f.brand()
w.turn_on()
w.brand()
