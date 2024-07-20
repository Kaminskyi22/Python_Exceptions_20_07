try:
    number = float(input("Enter a number to calculate its square root: "))
    if number < 0:
        raise ValueError("Negative number entered.")
    square_root = number ** 0.5
    print(f"The square root of {number} is {square_root}")
except ValueError as e:
    print(f"Error: {e}")