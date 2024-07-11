import os

def create_file(filename):

    with open("Day -7/"+filename, 'w') as f:
        f.write("Hello world!!!\n")
        f.write("welcome to the python world!!!\n")
        f.write('123 456\n')


def read_file(filename):

    with open("Day -7/"+filename, 'r') as f:
        return f.read()

def file_append(filename, text):

    with open("Day -7/"+filename, 'a') as f:
        f.write(text)


def rename_file(filename, newName):

    os.rename("Day -7/"+filename, "Day -7/"+newName)

def delete_file(filename):

    os.remove("Day -7/"+filename)

create_file("myFile.txt")
print(read_file("myFile.txt"))
file_append("myFile.txt", "Appended text\n")
rename_file("myFile.txt", "newFile.txt")
rename_file("newFile.txt", "myFile.txt")
delete_file("myFile.txt")