#
# Create a function called save_emails. This function takes no
# arguments but asks the user to input email, and it saves the
# emails in a CSV file. The user can input as many emails as they
# want. Once they hit ‘done’ the function saves the emails and
# closes the file. Create another function called open_emails.
# This function opens and reads the content of the CSV file. Each
# email must be in its line. Here is an example of how the emails
# must be saved:
# jj@gmail.com
# kate@yahoo.com
# and not like this:
# jj@gmail.comkate@yahoo.com

#import csv

def save_emails():
    while True:
        email= input("Enter the emails you want to save / enter done when you finish: ")

        if email.lower() == "done":
            #emails_file.close()
            break
        else:
            with open('day_44_emails.csv', 'a') as emails_file:
                emails_file.write(email)
                emails_file.write('\n')


def read_emails():
    with open('day_44_emails.csv', 'r') as emails_file:
        return emails_file.read()







