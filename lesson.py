#1
# try:
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
    
#     result = num1 / num2
    
#     print(f"Result of division: {result}")

# except ZeroDivisionError:
#     print("Error: Division by zero!")
# except ValueError:
#     print("Error: Invalid input. Please enter numbers.")


#2_1  аутсайд


# def divide(num1, num2):
#     return num1 / num2
# try:
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
    

#     result = divide(num1, num2)
    
#     print(f"Result of division: {result}")

# except ZeroDivisionError:
#       print("Error: Division by zero!")
# except ValueError:
   
#     print("Error: Invalid input. Please enter numbers.")


#2_2 інсайд

# def divide(num1, num2):
#     try:
#         return num1 / num2
#     except ZeroDivisionError:
#         print("Error: Division by zero!")
#         return "undefined"

# try:
#     num1 = float(input("Enter the first number: "))
#     num2 = float(input("Enter the second number: "))
    
#     result = divide(num1, num2)
    
#     print(f"Result of division: {result}")

# except ValueError:
#     print("Error: Invalid input. Please enter numbers.")


#3_3

# try:
#     user_input = input("Enter a string to convert to a number: ")
#     number = float(user_input)
#     print(f"The converted number is: {number}")
# except ValueError:
#     print("Error: The input cannot be converted to a number.")

#4_1 INSIDE
# def convert_to_number(s):
#     return float(s)

# try:
#     user_input = input("Enter a string to convert to a number: ")
#     number = convert_to_number(user_input)
#     print(f"The converted number is: {number}")
# except ValueError:
#     print("Error: The input cannot be converted to a number.")


#4_2 OUTSIDE

# def convert_to_number(s):
#     return float(s)

# try:
#     user_input = input("Enter a string to convert to a number: ")
#     number = convert_to_number(user_input)
#     print(f"The converted number is: {number}")
# except ValueError:
#     print("Error: The input cannot be converted to a number.")


#4_3

# def convert_to_number(s):
#     try:
#         return float(s)
#     except ValueError:
#         return "Error: The input cannot be converted to a number."

# user_input = input("Enter a string to convert to a number: ")
# result = convert_to_number(user_input)

# print(result)

