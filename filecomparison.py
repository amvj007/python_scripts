# File paths (Change these to your actual file paths)
file1_path = 'C:\\Users\\Gokul\\Gokul Github\\python_scripts\\\\file1.txt'
file2_path = 'C:\\Users\\Gokul\\Gokul Github\\python_scripts\\\\file2.txt'
output_file_path = 'C:\\Users\\Gokul\\Gokul Github\\python_scripts\\\\unique_names.txt'

with open(file1_path, 'r') as file:
    set1 = set(file.read().splitlines())

with open(file2_path, 'r') as file:
    set2 = set(file.read().splitlines())

# unique_names = set1 ^ set2  # Symmetric difference to find unique names
unique_names = set1.difference(set2)

with open(output_file_path, 'w') as file:
    for name in unique_names:
        file.write(f"{name}\n")
