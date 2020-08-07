import os
import subprocess
from os import listdir
from os.path import isfile, join


def create_folder(directory):
    if not os.path.exists(directory):
        os.mkdir(directory)


def find_books(input_dir, valid_file_extensions):
    if not os.path.exists(input_dir):
        print("Please create an directory called '" + input_dir + "'")
        exit(1)

    book_file_names = [f for f in listdir(input_dir) if isfile(join(input_dir, f))
                       and f.split(".")[1] in valid_file_extensions]

    if len(book_file_names) == 0:
        print("There are no books to convert in directory 'input'")
        exit(0)
    else:
        print("Found " + str(len(book_file_names)) + " books to convert")

    return book_file_names


def extract_name(file_path: str) -> str:
    return file_path.split(".")[0]


def convert(temp_directory, file_path):
    try:
        output_file_format = ".azw3"
        file_name_without_extension = extract_name(file_path)
        new_file_path = temp_directory + "/" + file_name_without_extension + output_file_format
        print("Attempting to convert book " + file_path)
        subprocess.call(["ebook-convert", "input/" + file_path, new_file_path])
    except:
        print("Failed to convert book" + file_path)


def main():
    input_dir = "input"
    temp_directory = "temp"
    valid_file_extensions = ["pdf", "epub"]

    create_folder(temp_directory)
    book_file_names = find_books(input_dir, valid_file_extensions)

    for file_name in book_file_names:
        convert(temp_directory, file_name)


main()
