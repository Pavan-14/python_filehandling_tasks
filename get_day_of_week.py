# to extract the number of email in paticualr day of week
def email_sender(file_name:str):
    weekday = dict()
    try:
        with open(file_name,"rt") as file:

            for line in file:
                if line.startswith('From '):
                    line = line.rstrip().split()
                    if line[2] not in weekday:
                        weekday[line[2]] = 1
                    else:
                        weekday[line[2]] += 1 
            print(weekday)
                        
    except:
        print("The file not existed in a specified path")

file_path = "E:\\Pavan Learnings\\Braineest\\week_03\\mbox-short.txt"
email_sender(file_path)