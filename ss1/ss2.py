try:
    with open('text.txt','r') as f:
        print(f.read())

except FileNotFoundError:
    print("Cant find file")

except IOError:
    print("Cant read file")