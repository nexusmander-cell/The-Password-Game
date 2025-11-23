import zipfile

with zipfile.ZipFile("D:\Lesson3Module2_python\zip compression\prac\prac2\Example.zip", 'r')as z:
    z.extractall("Decompressed_file")

    print("Successfully decompressed")