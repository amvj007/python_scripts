"""
# Function to read file and return a set of server names
def read_file(file_path):
    with open(file_path, 'r') as file:
        return set(file.read().splitlines())

# Function to find unique server names between two sets and write them to a new file
def write_unique_names(file1, file2, output_file):
    set1 = read_file(file1)
    set2 = read_file(file2)
    
    unique_names = set1 ^ set2  # Symmetric difference to find unique names
    
    with open(output_file, 'w') as file:
        for name in unique_names:
            file.write(f"{name}\n")
"""


# File paths (Change these to your actual file paths)
file1_path = 'C:\\Users\\Gokul\\Documents\\Pythoncode\\file1.txt'
file2_path = 'C:\\Users\\Gokul\\Documents\\Pythoncode\\file2.txt'
output_file_path = 'C:\\Users\\Gokul\\Documents\\Pythoncode\\unique_names.txt'

with open(file1_path, 'r') as file:
    set1 = set(file.read().splitlines())

with open(file2_path, 'r') as file:
    set2 = set(file.read().splitlines())

unique_names = set1 ^ set2  # Symmetric difference to find unique names

with open(output_file_path, 'w') as file:
    for name in unique_names:
        file.write(f"{name}\n")
