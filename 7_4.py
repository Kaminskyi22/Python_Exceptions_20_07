dictionary = {}
print("Enter key-value pairs (type 'done' to finish):")

while True:
    key = input("Enter key: ")
    if key == 'done':
        break
    value = input("Enter value: ")
    dictionary[key] = value

while True:
    print("\nMenu:")
    print("1. Display dictionary")
    print("2. Search for a value by key")
    print("3. Replace a value by key")
    print("4. Display value by key")
    print("5. Delete a value by key")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    match choice:
        case '1':
            print("Dictionary contents:")
            for key, value in dictionary.items():
                print(f"{key}: {value}")
        
        case '2':
            key = input("Enter key to search for: ")
            try:
                print(f"The value for '{key}' is: {dictionary[key]}")
            except KeyError:
                print("Error: Key not found.")
        
        case '3':
            key = input("Enter key to replace value for: ")
            if key in dictionary:
                new_value = input("Enter new value: ")
                dictionary[key] = new_value
                print(f"Value for '{key}' has been replaced.")
            else:
                print("Error: Key not found.")
        
        case '4':
            key = input("Enter key to display value for: ")
            try:
                print(f"The value for '{key}' is: {dictionary[key]}")
            except KeyError:
                print("Error: Key not found.")
        
        case '5':
            key = input("Enter key to delete value for: ")
            try:
                del dictionary[key]
                print(f"Value for '{key}' has been deleted.")
            except KeyError:
                print("Error: Key not found.")
        
        case '6':
            break
        
        case _:
            print("Invalid choice. Please try again.")
