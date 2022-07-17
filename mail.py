#Reasons
from curses.ascii import isalpha
import email


mail = input("Email : ")
if len (mail)>=6:
    if mail[0].isalpha( ):
        if ("@" in mail) and (mail.count("@")==1):
            pass           
            
        else:
            print('Invalid Email : Either the "@" is missing or it has been repeated more than once in the Mail provided')
    else:
        print('Invalid Email : The E-Mail provided is starting with a number')
else:
    print(f'Invalid Email : The E-Mail provided is less than 6 characters')
