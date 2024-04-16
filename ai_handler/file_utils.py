import os


def create_file_or_read_content(file_path, default_content):
    if not os.path.exists(file_path):
        create_if_ai_file_not_exist(file_path, default_content)
    else:
        print("File already exist:")


def create_if_ai_file_not_exist(file_path, default_content):
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:
            return file.write(default_content)
    else:
        print(f"file {file_path} already exist")


def count_lines(file_path):
    """
    Count the number of lines in a file.
    """
    # Check if the file exists
    if os.path.exists(file_path):
        # Open the file in read mode and count the number of lines
        with open(file_path, "r") as file:
            return sum(1 for _ in file)
    else:
        # If the file does not exist, return 0
        return 0


def populate_existing_lines_set(file_path):
    """
    Populate a set with existing lines in the CSV file.
    """
    existing_lines = set()
    with open(file_path, "r") as file:
        for line in file:
            existing_lines.add(line.strip())
    return existing_lines


def read_file(file_path):
    """
    Read contents of a file if it doesn`t exist return None.
    """
    try:
        with open(file_path, "r") as file:
            return file.read()
    except FileNotFoundError:
        return None


def read_file_splitlines(file_path):
    """
    Read contents of a file and return as a list of lines.
    """
    try:
        with open(file_path, "r") as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []


def write_to_file(file_path, content):
    """
    Write content to a file.
    """
    with open(file_path, "w") as file:
        file.write(content)


def append_to_file(file_path, content):
    """
    Append content to the end of a file.
    """
    with open(file_path, "a") as file:
        file.write(content)


def file_exists(file_path):
    """
    Check if a file exists.
    """
    return os.path.isfile(file_path)
