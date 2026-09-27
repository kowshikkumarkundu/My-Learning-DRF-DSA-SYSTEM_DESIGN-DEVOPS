def write_file(filename: str,content: str):
    """
    create a file or append content to the existing file. take two argument
    filename as filename.txt and content as string
    """
    with open(filename, "a") as file:
        file.write(content)

def read_file(filename: str):
    """
    open file and read content. take one parameter as "filename.txt" string
    """
    with open(filename,'r') as file:
        content = file.read()
        return content

import os

def list_files():
    """
    Return the names of files and directories
    in the current directory.
    """
    dir_list = os.listdir()
    return dir_list

