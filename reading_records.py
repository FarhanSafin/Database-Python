# Importing Libraries
import Libraries.binary_file_read as read
import Libraries.binary_file_append as append
import Libraries.record_to_string_convert as convert
from datetime import date, datetime
import re
from prettytable import PrettyTable

file = read.openFile("Data")
read.jumpToReadingOffset(0, file)
total = read.readBytes(9999999999, file)
string = total.decode()

for line in string.split("******"):
    print(line)