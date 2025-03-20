import os

# File Operation Modes:
# r = read | a = append | w = write | x = create

def read_file():
    """Reads and prints the file content line by line"""
    try:
        with open("names.txt", "r") as f:
            for line in f:
                print(line.strip())  # Removes unwanted newline gaps
    except FileNotFoundError:
        print("Error: 'names.txt' does not exist.")

def append():
    """Appends 'Neil' to the file only if it isn't already present"""
    try:
        with open("names.txt", "r") as f:
            content = f.read()

        if "Neil" not in content:
            with open("names.txt", "a") as f:
                f.write("\nNeil")
            print("Neil added to the file.")

        read_file()  # Display updated content

    except FileNotFoundError:
        print("Error: 'names.txt' does not exist. Creating a new file.")
        with open("names.txt", "w") as f:
            f.write("Neil\n")
        read_file()

def write_file():
    """Overwrites the content of 'content.txt'"""
    with open("content.txt", "w") as f:
        f.write("I deleted all of the content.")

    with open("content.txt", "r") as f:
        print(f.read())

def create_files():
    """Creates new files with different methods"""
    open("name_list.txt", "w").close()  # Creates or overwrites file

    try:
        open("name_list1.txt", "x").close()  # Creates file, errors if exists
    except FileExistsError:
        print("File 'name_list1.txt' already exists.")

def delete_file(filename):
    """Deletes a file if it exists"""
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Deleted '{filename}'.")
    else:
        print(f"File '{filename}' does not exist.")

def copy_file(source, destination):
    """Copies content from one file to another"""
    try:
        with open(source, "r") as f:
            content = f.read()
        
        with open(destination, "w") as g:
            g.write(content)

        print(f"Copied content from '{source}' to '{destination}'.")

    except FileNotFoundError:
        print(f"Error: '{source}' does not exist.")

# Run example operations
append()
write_file()
create_files()
delete_file("dave.txt")
copy_file("more_names.txt", "names_1.txt")
