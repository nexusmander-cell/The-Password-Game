#p1
try:
    price = int(input("Enter the price of your product: "))
    amount = int(input("Enter the amount of the product you want to buy: "))
    print("Valid price and amount")
except ValueError:
    print("Error: Invalid input. Please enter numbers only.")
#p2
name = input("What is your username:")
password = input("Enter your password:")

try:
    if name == "":
        raise ValueError ("Username can't be nothing")
    if password == "":
        raise ValueError  ("Password can't be nothing")
    if len(password) < 6:
        raise Exception ("Password too long")

    print("Sucessfully logged in")
except ValueError as e:
     print("Error:", e)

finally:
       print("End Program")       

#p3
try:
    num1 = int(input("Enter the first number"))
    num2 = int(input("Enter the second number"))

    result = num1/num2
    print("Result is: ", result)
except ValueError as e:
    print("Error: Please enter an integer")
    with open ('D:/Lesson3Module2_python/exception/error_log.txt', 'a') as f:
        f.write(f"Value Error: {e}\n")
except ZeroDivisionError as d:
    print("Error: Cannot divide by or to zero")
    with open ('D:/Lesson3Module2_python/exception/error_log.txt', 'a') as f:
        f.write(f"Zero Division Error: {d}\n")

#p4
age = int(input("Enter your age "))

try:
    if 0 > age or age > 120:
        raise ValueError ("Invalid Age")
    print("Valid Age")
except ValueError as e:
    print("Error: ", e)
finally:
    print("End Program")
