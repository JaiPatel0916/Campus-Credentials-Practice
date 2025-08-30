# choice = int(input("Entrt your chice: "))

# TYPE 1
# match choice:
#     case 1:
#         print("ONE")
#     case 2:
#         print("TWO")
#     case 3:
#         print("Three")
        
# TYPE 2
# match choice:
#     case 1|2|3:
#         print("Hello")
#     case 4|5|6:
#         print("JAI")


#TYPE 3
# x=["Jai","Rashi","Shivam"]

# match x:
#     case 8.2:
#         print("Float")
#     case ["Jai","Shivam"]:
#         print("Boys")
#     case ["Rashi"]:
#         print("Girl")
#     case [1,2,3]:
#         print("Numbers")
#     case x:
#         print("Printed x")


#TASK 2 
    
# t=("Car","Bike")

# match t:
#     case ("Car","Bike"):
#         print("Vehicles")
#     case ("8","50"):
#         print("Numbers")


#Task 3

# choice = int(input("Enter your choice: "))

# match choice:
#     case 1:
#        a= int(input("Enter first number: "))
#        b= int(input("Enter first number: "))
#        print(a+b)
#     case 2:
#         c= int(input("Enter your number: ")) 
#         print(c*c)
#     case 3:
#         r= int(input("Enter the radius: ")) 
#         print(3.14*r*r)


#Dictionary match

# x={"name":"Jai","Age":20}

# match x:
#     case{"name":"Shivam","Age":22}:
#         print("Student 1 ")
#     case{"name":"Jai","Age":20}:
#         print("Student 2")
        
        
#conditions in match case
per=29


match per:
    case per if per%2==1:
        print("Hii ODD ")
    case per if per%2 == 0:
        print("Hii EVEN")

