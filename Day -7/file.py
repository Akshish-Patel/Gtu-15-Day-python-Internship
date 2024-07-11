# file handeling operations

# create a file
# syntex : open(filename, mode)
# mode are : r: open an existing file for a read operation.
# w: open an existing file for a write operation. If the file already contains some data, then it will be overridden but if the file is not present then it creates the file as well.
# a:  open an existing file for append operation. It won’t override existing data.
# r+:  To read and write data into the file. This mode does not override the existing data, but you can modify the data starting from the beginning of the file.
# w+: To write and read data. It overwrites the previous file if one exists, it will truncate the file to zero length or create a file if it does not exist.
# a+: To append and read data from the file. It won’t override existing data.

# file open
f = open("Day -7/Demo.txt")
print(f.read()) # read() function is read the hole file in original formate
# print(f.readline())# read line function is read only single line
# print(f.readlines())# readlines functio is give the list of each lines

print("\nread file with helo of for loop")

for line in f:
    print(line)

f.close() #close function is use to close the file


# file open use by with  keyword

# when we are use with keyword file will automatictly colse by self
with open("Day -7/Demo.txt") as f:
    print(f.read())

# create a file
f = open("Day -7/main.txt", "w")
print(f.write("My name is Ram"))
f.close()

# file create use by with keyword
with open('Day -7/main.txt', 'w') as f:
    f.write("my name is akshish")