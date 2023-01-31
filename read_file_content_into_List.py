'''read the file then put into a list''' 
def file_read(filepath:str):
    try:
       with open(filepath,"rt") as file:
            print(file.read().split())
    except FileNotFoundError as e:
        print(e)

path = input("enter your file path with the extension: \n")
file_read(path)