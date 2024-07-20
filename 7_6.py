def display_dictionary(d):
    print("Dictionary contents:")
    for key, value in d.items():
        print(f"{key}: {value}")

def search_value(d, key):
    try:
        return d[key]
    except KeyError:
        return "Error: Key not found."

def replace_value(d, key, new_value):
    try:
        d[key] = new_value
    except KeyError:
        return "Error: Key not found."
    return f"Value for '{key}' has been replaced."

def display_value(d, key):
    try:
        return d[key]
    except KeyError:
        return "Error: Key not found."

def delete_value(d, key):
    try:
        del d[key]
    except KeyError:
        return "Error: Key not found."
    return f"Value for '{key}' has been deleted."

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
            display_dictionary(dictionary)
        
        case '2':
            key = input("Enter key to search for: ")
            print(search_value(dictionary, key))
        
        case '3':
            key = input("Enter key to replace value for: ")
            new_value = input("Enter new value: ")
            print(replace_value(dictionary, key, new_value))
        
        case '4':
            key = input("Enter key to display value for: ")
            print(display_value(dictionary, key))
        
        case '5':
            key = input("Enter key to delete value for: ")
            print(delete_value(dictionary, key))
        
        case '6':
            break
        
        case _:
            print("Invalid choice. Please try again.")
