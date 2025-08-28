# # Task: Create an abstract class Animal with:

# sound() → abstract method

# Implement it in Dog and Cat classes
# Expected Output:
#  Dog says Woof!
# Cat says Meow!



from abc import ABC , abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound():
        pass


class dog(Animal):
    def sound():
        print("Dog says Woof")
        
class cat(Animal):
    def sound():
        print("Cats says Meow")
        
d=dog
c=cat
d.sound()
c.sound()
        
        

        
    
        

    