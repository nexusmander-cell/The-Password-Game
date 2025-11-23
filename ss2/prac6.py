import re

credit_card_pattern =  r'^(?:\d{4}-){3}\d{4}$|^\d{16}$|^(?:\d{4}\s){3}\d{4}$'
users_credit_card_number = input("Enter your credit card number")

match = re.search(credit_card_pattern, users_credit_card_number)

if match:
    print("Valid credit card number")
else:
    print("Invalid credit card number")