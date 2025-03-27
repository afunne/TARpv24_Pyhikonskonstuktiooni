from mOdThisIsJustAtestDoc import *

try:
    choice = int(input("valida number: "))
except:
    print("nuh uh")

if choice == 3:
        try:
            username="lol"
            password=1234
            user = [(username, password)]
            user = muuda_kasutajat(user)
            print(user) 

            print("Uuendatud kasutajad:", user)
        except:
            print("Teil pole kasutajanimi")