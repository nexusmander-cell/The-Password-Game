import re
pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()])[A-Za-z\d!@#$%^&*()]{8,}$"
password = input("Enter a password")
pass_input = re.search(pattern, password)

if pass_input:
    print("Valid password")
else:
    print("Not valid password")