# Importing Libraries
import Libraries.binary_file_append as append
import Libraries.record_to_string_convert as convert

# Continuously prompt the user for input until they choose to quit
while True:
    ID = input("Enter the ID (or 'q' to quit): ")
    if ID == 'q':
        break
    Name = input("Enter the Name: ")
    BirthDate = input("Enter the BirthDate: ")
    Address = input("Enter the Address: ")

    # Create a list-format record using the attributes
    record = [ID, Name, BirthDate, Address]
    record_str = convert.stringifyRecord(record)
    file = append.createOrOpenFileForAppend("Data")
    append.appendToFile(file, record_str + "******")
