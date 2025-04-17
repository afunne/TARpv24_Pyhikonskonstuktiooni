import smtplib
from email.message import EmailMessage
import ssl
from tkinter import filedialog

def saada_kiri():
    kellele = input("Kellele saata: ")
    teema = input("Sisu: ")
    smtp_server='smtp.gmail.com'
    smtp_port=587
    kellelt="tahmazovhussejn@gmail.com"
    salasõna=input("Salasõna: ") #"kjfmeofgenjfdejooefojkwongrowoorwo"
    msg=EmailMessage()
    sisu="""
        <!DOCTYPE html>
        <head>
        </head>
            <body>
                <h1>Sending an HTML email from Python</h1>
                <p>Hello there,</p>
                <a href="https://inspirezone.tech/">Here's a link to an awesome dev
                    community!</a>
        </body>
    </html>
"""
    msg=EmailMessage()
    msg['Subject']=teema
    msg['From']=kellelt
    msg['To']=kellele
    msg.set_content(sisu,subtype='html')
    fail = filedialog.askopenfilename(title="Vali fail", filetypes=[("All files", "*.*")])
    with open(fail,'rb') as f:
        faili_sisu=f.read()
        faili_nimi=fail.split("/")[-1]
        msg.add_attachment(faili_sisu,maintype="application",subtype="octetstream",filename=faili_nimi)

    try:
        with smtplib.SMTP(smtp_server,smtp_port) as server:
            server.ehlo()
            server.starttls(context=ssl.create_default_context())
            server.login(kellelt,salasõna)
            server.send_message(msg)
            print("Kiri saadetud!")
    except Exception as e:
        print("viga:",e)