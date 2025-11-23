import re

example = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/(19|20)\d{2}$"

while True:
    birth = input("Type in your birth date (dd/mm/yyyy): ")
    if re.match(example, birth):
        print("Valid Birth Date")
        break
    else:
        print("Invalid birth")

