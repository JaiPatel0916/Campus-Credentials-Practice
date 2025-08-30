try: 
    age = int(input("Enter your age: "))
    if age<18:
        raise ValueError("Your age must be greater than 18")
    print("You can vote")

except ValueError as e:
    print("Exception reason: ",e)

finally:
    print("Log out")

print("Remaining code ")