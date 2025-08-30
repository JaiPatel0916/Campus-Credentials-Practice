try:
    no1=int(input("Enter no1: "))
    no2=int(input("Enter no2: "))
    ans =no1/no2
except ZeroDivisionError:
    print("Zero Division Error...")
    
except ValueError:
    print("Pleae check values")

except NameError:
    print("Please check Variables name")
print("Remaining CODE...")