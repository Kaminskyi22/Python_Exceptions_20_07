def display_dictionary(d):
    print("Dictionary contents:")
    for key, value in d.items():
        print(f"{key}: {value}")

def search_value(d, key):
    return d[key]

def replace_value(d, key, new_value):
    d[key] = new_value

def display_value(d, key):
    return d[key]

def delete_value(d, key):
    del d[key]

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

    try:
        match choice:
            case '1':
                display_dictionary(dictionary)
            
            case '2':
                key = input("Enter key to search for: ")
                print(f"The value for '{key}' is: {search_value(dictionary, key)}")
            
            case '3':
                key = input("Enter key to replace value for: ")
                new_value = input("Enter new value: ")
                replace_value(dictionary, key, new_value)
                print(f"Value for '{key}' has been replaced.")
            
            case '4':
                key = input("Enter key to display value for: ")
                print(f"The value for '{key}' is: {display_value(dictionary, key)}")
            
            case '5':
                key = input("Enter key to delete value for: ")
                delete_value(dictionary, key)
                print(f"Value for '{key}' has been deleted.")
            
            case '6':
                break
            
            case _:
                print("Invalid choice. Please try again.")
    
    except KeyError:
        print("Error: Key not found.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
