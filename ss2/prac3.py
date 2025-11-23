def calculate_average(numbers):
    assert len(numbers) > 0, "The list cannot be empty"
    assert all(isinstance(num, (int, float))for num in numbers), "The list have to have numbers"
    total = sum(numbers)
    average = total/ len(numbers)
    return average

def main():
    raw = input("Enter a list of number, seperate with a comma: ")
    numbers = [float(x) for x in raw.split(',')]
    reuslt = calculate_average(numbers)
    print("Average = ", reuslt)
main()