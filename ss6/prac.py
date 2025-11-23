import time

# Tạo danh sách 1 triệu phần tử
numbers = list(range(1_000_000))

# Cách 1: Dùng vòng lặp for
start_time = time.time()
total = 0
for num in numbers:
    total += num
end_time = time.time()
print("Cách 1 (for loop):", end_time - start_time, "giây")

# Cách 2: Dùng hàm sum()
start_time = time.time()
total = sum(numbers)
end_time = time.time()
print("Cách 2 (sum()):", end_time - start_time, "giây")
