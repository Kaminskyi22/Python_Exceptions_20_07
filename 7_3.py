def calculate_square_root(num):
    try:
        if num < 0:
            return "Error: Negative number entered."
        return num ** 0.5
    except ValueError:
        return "Error: Invalid input. Please enter a valid number."

user_input = input("Enter a number to calculate its square root: ")

try:
    number = float(user_input)
    result = calculate_square_root(number)
    print(result)
except ValueError:
    print("Error: Invalid input. Please enter a valid number.")
