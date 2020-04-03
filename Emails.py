import imaplib
import email
import webbrowser
import Movement as m
import os
import cv2

def j1():
    while(1):
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login('swapnil13pawar22@gmail.com', 'DarkArt742')
        mail.select('inbox')
        result, data = mail.search(None, 'ALL')
        mail_ids = data[0]

        id_list = mail_ids.split()
        # first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])
        #print(latest_email_id)
        if latest_email_id > 62:
            break

    result, data = mail.fetch(str(latest_email_id), '(RFC822)')
    return data


def read_email_from_gmail():

        data = j1()
        for response_part in data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                email_subject = msg['subject']
                email_from = msg['from']
                if email_from == "TECHNOFY 7 <swapnil99pawar@gmail.com>":
                    qu = email_subject
                    print(email_subject)
                    print(email_from)

                    if 'x open youtube' in qu:
                        webbrowser.open("youtube.com")

                    elif 'x open fb' in qu:

                        webbrowser.open("facebook.com")

                    elif 'x open google' in qu:
                        webbrowser.open("google.com")

                    elif 'terminate x' in qu:
                        break

                    elif 'x open steam' in qu:
                        p = 'F:\\Steam\\Steam.exe'
                        os.startfile(p)

                    elif 'x open c3' in qu:
                        p = 'E:\\game\\Crysis 3\\Bin32\\Crysis3.exe'
                        os.startfile(p)

                    elif 'start' in qu:
                        cv2.waitKey(1000)
                        m.Move()