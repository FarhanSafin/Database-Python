# Importing Libraries
import Libraries.binary_file_read as read

file = read.openFile("Data")
read.jumpToReadingOffset(0, file)
total = read.readBytes(9999999999, file)
string = total.decode()

for line in string.split("******"):
    list = line.split("||||")
    print(list)
