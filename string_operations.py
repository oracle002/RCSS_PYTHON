# 1.7. Menu-driven program for string operations

def string_operations_menu():
    string = input("Enter a string: ")
    while True:
        print("\nString Operations Menu:")
        print("1. Check if substring")
        print("2. Count occurrences of character")
        print("3. Replace substring")
        print("4. Convert to capital letters")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            substring = input("Enter substring to check: ")
            if substring in string:
                print(f"'{substring}' is a substring of '{string}'.")
            else:
                print(f"'{substring}' is not a substring of '{string}'.")
        elif choice == 2:
            char = input("Enter character to count: ")
            count = string.count(char)
            print(f"Occurrences of '{char}' in '{string}': {count}")
        elif choice == 3:
            old_substring = input("Enter substring to replace: ")
            new_substring = input("Enter new substring: ")
            new_string = string.replace(old_substring, new_substring)
            print(f"Modified string: '{new_string}'")
        elif choice == 4:
            print(f"String in capital letters: '{string.upper()}'")
        elif choice == 5:
            print("Exiting string operations menu.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

string_operations_menu()


