def calculate_factorial(number):
    result = 1
    for i in range(1, number + 1):

        result *= i
    return result

def main():
    numbers = [5, 7, 0, -3, 10]
    for num in numbers:
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            factorial = calculate_factorial(num)
            print(f"The factorial of {num} is {factorial}")

if __name__ == "__main__":
    main()