

try:
    user_input = int(input("Enter number to divide"))
    user_input2 = int(input("Enter number to divide by"))
    
    print(user_input/user_input2)
except ZeroDivisionError:
    
    print("Invalid")