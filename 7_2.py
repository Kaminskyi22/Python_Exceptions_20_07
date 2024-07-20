def calculate_square_root(num):
    if num < 0:
        raise ValueError("Negative number entered.")
    return num ** 0.5

try:
    user_input = float(input("Enter a number to calculate its square root: "))
    result = calculate_square_root(user_input)
    print(f"The square root of {user_input} is {result}")
except ValueError as e:
    print(f"Error: {e}")
