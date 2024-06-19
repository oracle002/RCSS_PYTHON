# 1.12. Use OS module for various operations

import os

# 1.12.1. Create a directory
directory_name = 'test_directory'
os.mkdir(directory_name)
print(f"Directory '{directory_name}' created.")

# 1.12.2. Directory Listing
print(f"Files in directory '{directory_name}':")
print(os.listdir(directory_name))

# 1.12.3. Search for ".py" files
py_files = [file for file in os.listdir('.') if file.endswith('.py')]
print(f"Python files in current directory: {py_files}")

# 1.12.4. Remove a particular file
file_to_remove = 'file_to_remove.txt'
if os.path.exists(file_to_remove):
    os.remove(file_to_remove)
    print(f"File '{file_to_remove}' removed.")
else:
    print(f"File '{file_to_remove}' does not exist.")


