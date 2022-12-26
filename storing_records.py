# Importing Libraries
import Libraries.binary_file_read as read
import Libraries.binary_file_append as append
import Libraries.record_to_string_convert as convert

# Prompt the user to enter the attributes
ID = input("Enter the ID: ")
Name = input("Enter the Name: ")
BirthDate = input("Enter the BirthDate: ")
Address = input("Enter the Address: ")

# Create a list-format record using the attributes
record = [ID, Name, BirthDate, Address]

# Converting to String
converted = convert.stringifyRecord(record)

# Open the database file for writing
with open("database.txt", "a") as f:
    # Write the record to the file as a string
    f.write(str(converted) + "\n")

