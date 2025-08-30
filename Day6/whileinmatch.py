while True:
    print("Menu:")
    print("1. Addition")
    print("2. Square")
    print("100. Exit")
    
    choice = int(input("Enter you choice: "))
    match choice:
        case 1:
            a,b=input("Enter two numbers: ").split()
            print("Sum of two nummbers is: ",int(a)+int(b))
        case 2:
            no=int(input("Enter no.: "))
            print("Square is: ", no*no)
            
        case 100:
            exit(0)
            
        case _:
            print("Invalid choice")
    