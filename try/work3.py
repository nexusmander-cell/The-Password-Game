

try:
    file_object = open("D:/Lesson3Module2_python/try/data.csv", 'r')
    print(file_object)
    file_object.close()
except FileNotFoundError:
    file_object.close()

