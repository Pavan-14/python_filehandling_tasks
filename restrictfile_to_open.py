'''if the file is demofile.txt don't open the file.
    if the file doesn't exist raise an error
    if the file other than demofile.txt open the file and read'''

import os
def file_read(filepath:str):
    file_name = os.path.basename(filepath) 
    # location = os.path.dirname(filepath) 
    # print(file_name)
    # print(location)
    if file_name != 'demofile.txt':
        try:
            with open(filepath,"rt") as file:
                print(file.read())
        except FileNotFoundError as e:
            print(e)
    else:
        print("the file demofile.txt is confidential")

path = input("enter your file path with the extension: \n")
file_read(path)