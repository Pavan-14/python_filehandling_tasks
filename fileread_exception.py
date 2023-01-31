'''the goal is to read text file into upper cases'''
# trying to open the file
# the user enters the path. it trys to open the file in read text file mode.
# if the file not available, exception gives a error message
def file_read(filepath:str):
    try:
       with open(filepath,"rt") as file:
            print(file.read().upper())
    except FileNotFoundError as e:
        print(e)

path = input("enter your file path with the extension: \n")
file_read(path)