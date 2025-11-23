lst = [10, 20, 30]
try:
    user_input = int(input("Enter a number"))
    print(lst[user_input])
except IndexError:
    print("Invalid number")


