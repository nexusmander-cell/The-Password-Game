import re

pattern = r'^(0[1-9]|[12][0-9]|3[01])/' \
              r'(0[1-9]|1[0-2])/' \
              r'(19[0-9]{2}|20[0-9]{2})$'

date = input("What date do you want to verify?")

match = re.match( pattern, date)

if match:
    print("Valid Date")
else:
    print("Invalid Date")