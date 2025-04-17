
import smtplib
from email.message import EmailMessage
import ssl
from tkinter import filedialog

def saada_kiri():
    kellele = input("Kellele saata: ")
    teema = input("Sisu: ")
    sisu=input("Sisu: ")
    smtp_server='smtp.gmail.com'
    smtp_port=587
    kellelt="tahmazovhussejn@gmail.com"
    salasõna=input("Salasõna: ") #"kjfmeofgenjfdejooefojkwongrowoorwo"
    msg=EmailMessage()
    msg['Subject']=teema
    msg['From']=kellelt
    msg['To']=kellele
    msg.set_content(sisu)
    fail=filedialog.askopenfilename(title="Vali fail",filetypes=[("All files", "*.*")])

    with open(fail,'rb') as f:
        faili_sisu=f.read()
        faili_nimi=fail.split("/")[-1]
        msg.add_attachment(faili_sisu,maintype="application",subtype="octetstream",filename=faili_nimi)

        with smtplib.SMTP(smtp_server,smtp_port) as server:
            server.ehlo()
            server.starttls(context=ssl.create_default_context())
            server.login(kellelt,salasõna)
            server.send_message(msg)
            print("Kiri saadetud!")

