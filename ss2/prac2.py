def calculate_sum(numbers):
    print("Debugging: number =", numbers)
    total = 0
    for num in numbers:
        print("Debugging: Addition", num, "into total")
        total += num
    print("Debugging: The total is =", total)
    return total
def main():
    numbers = [1, 2, 3, 4, 5]
    results = calculate_sum(numbers)
    print("Sum:", results)
main()