# i have mdox-short.txt file and the file contains the email sender and reciever informations along with email data
def email_sender(file_name):
    # output_file = open(r"E:\Pavan Learnings\Braineest\week_03\sender.txt","wt")
    output_file_path = r"E:\Pavan Learnings\Braineest\week_03\sender.txt"
    try:
        with open(file_name,"rt") as file:
            with open(output_file_path,"wt") as output_file:
                for line in file:
                    if line.startswith('From '):
                        line = line.rstrip().split()
                        output_file.writelines("Sender: " +line[1]+"\n")
    except:
        print("The file not existed in a specified path")

    # finally:
         # output_file.close()

file_path = r"E:\Pavan Learnings\Braineest\week_03\mbox-short.txt"
email_sender(file_path)