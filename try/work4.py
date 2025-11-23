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


