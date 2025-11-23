import zipfile
with zipfile.ZipFile("tai_lieu_nen.zip", 'w') as zip_file:
    zip_file.write(r"D:\Lesson3Module2_python\zip compression\prac\file1.txt")
    zip_file.write(r"D:\Lesson3Module2_python\zip compression\prac\file2.csv")
    zip_file.write(r"D:\Lesson3Module2_python\zip compression\prac\file3.json")
    zip_file.write(r"D:\Lesson3Module2_python\zip compression\prac\file4.png")
print("Successfully created a backup")