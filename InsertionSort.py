def read_numbers():
    while True:
        try:
            num_count = int(input("Enter the number of numbers you want to input (between 10 and 20): "))
            if 10 <= num_count <= 20:
                break
            else:
                print("Please enter a number between 10 and 20.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    numbers = []

    print("Enter the numbers:")
    for i in range(num_count):
        while True:
            try:
                num = int(input(f"Number {i+1}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")

    return numbers

numbers = read_numbers()
print("Numbers entered:", numbers)
