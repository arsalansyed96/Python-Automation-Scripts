import os
import shutil


def copy_files(src, dst):
    if not os.path.exists(src):
        print("path "+src+" doesnt exist")
    if not os.path.exists(dst):
        print("path "+dst+" doesnt exist")

    shutil.copytree(src, dst)
    print("Copied files to kindle")


def main():
    input_directory = "temp"
    output_directory = "output"

    copy_files(input_directory, output_directory)


main()
