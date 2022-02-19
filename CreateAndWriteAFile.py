import os

file_name = input("Enter a file name: ")

check = os.path.isfile(file_name)

if not check:
    f = open(file_name, "w")
    print(
        "Since the file '" + file_name + "' was not existing in the path, an empty file '" + file_name + "'created.")
    print(
        "Now, write some text to be saved in this file. After you have written, enter 'EOL' for saving and closing the file.")

    while True:
        str1 = input()
        if not str1 == "EOL":
            f.write(str1 + "\n")
        else:
            break
    f.close()

elif check:
    f = open(file_name, "a")
    print("File '" + file_name + "' already exists in the path. File has been opened.")
    print(
        "Now, write some text to be saved in this file. After you have written, enter 'EOL' for saving and closing the file.")

    while True:
        str1 = input()
        if not str1 == "EOL":
            f.write(str1 + "\n")

        else:
            break
    f.close()