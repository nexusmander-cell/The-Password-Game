
import pdb

x = 10
y = 0

def divide(a, b):
    pdb.set_trace()
    result = a/b
    return result

try:
    print(divide(x,y))
except ZeroDivisionError as e:
    print(f"Error:{e}")