# Created by vidit.singh at 27-02-2022
# Working with files

file = open("D:\\vidit.txt")
print(file.read())

file.seek(0)  # To reset the read cursor.
print(file.read())
file.close()  # Manually close this file.

# To automatically close file, open file as .
with open("D:\\vidit.txt") as my_file:
    content = my_file.read()
    print(content)

# Create a new file in Write mode.
with open("D:\\vidit_new.txt", mode='w') as my_new_file:
    my_new_file.write("Hello world!")

# Appending in a file.
with open("D:\\vidit_new.txt", mode='a') as my_new_file:
    my_new_file.write("\n Hi, This is new line appended.")

# Reading and writing.
with open("D:\\vidit_new.txt", mode='r+') as my_new_file1:
    my_new_file1.write("Hi, File is in read and write mode.")
    content = my_new_file1.read()

# Writing and Reading mode. Overwrites existing file or create a new file.
with open("D:\\vidit_new.txt", mode='w+') as my_new_file2:
    my_new_file2.write("Hi, File is in write & read mode.")
    con = my_new_file2.read()
    print(con)

