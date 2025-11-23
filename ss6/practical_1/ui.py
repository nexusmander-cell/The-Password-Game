import time
import datetime
import timeit
import os

print("=== BỘ ĐO HIỆU NĂNG PYTHON ===")
print("1. timeitfile | 2. datetimefile | 3. timefile")

choice = input("Nhập lựa chọn (1/2/3): ")
file_path = input("Nhập đường dẫn có tên file .py chứa code cần dùng: ")

if not file_path.endswith(".py"):
    file_path += ".py"


if not os.path.exists(file_path):
    print("File does not exist:", file_path)
    exit()


with open(file_path, "r", encoding="utf-8") as f:
    code = f.read()

if choice == "1":
    print("Testing using code timeit module")
    t = timeit.timeit(stmt = code, number = 1000)
    print("Mean time over 1000 test run:", t/1000)
elif choice == "2":
    print("Testing using code datetime module")
    start = datetime.datetime.now()
    exec(code)
    end = datetime.datetime.now()
    print("The program lasted for:", end-start)
elif choice == "3":
    print("Testing code using time module")
    start = time.time()
    exec(code)
    end = time.time()
    print("The program lasted for: ", end-start)
else:
    print("Invalid choice")



