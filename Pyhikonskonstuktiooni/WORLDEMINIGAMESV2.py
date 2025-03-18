from random import *
import colorama
colorama.just_fix_windows_console()
minisõne="viski"
minisõne_list=list(minisõne)
listnumber = ["v", "i", "s", "k", "i"]



OKGREEN = '\033[92m'
OKRED = '\033[91m'
ENDC = '\033[0m'

while True:
    try:
        tase=int(input("Valige, kas te olete laps või mees? (1-laps 2-mees): "))
        if tase <= 0 or tase >= 3:
            print("BRUH")
            continue
        else:
            break
    except:
        print(":|")
        
# my wordle
if tase==1:
    while True:
        number1 = input("Proovi, panna midagi (mitte sõna): ").lower()
        if number1 not in listnumber[0]:
            print(OKRED+"Proovi uuesti" + ENDC)
            continue
        else:
            print(OKGREEN+"Väga hästi!"+ENDC)
            break

    while True:
        number2 = input("Proovi, panna midagi (mitte sõna): ").lower()
        if number2 not in listnumber[1]:
            print(OKRED+"Proovi uuesti" + ENDC)
            continue
        else:
            print(OKGREEN+"Väga hästi!"+ENDC)
            break

    while True:
        number3 = input("Proovi, panna midagi (mitte sõna): ").lower()
        if number3 not in listnumber[2]:
            print(OKRED+"Proovi uuesti" + ENDC)
            continue
        else:
            print(OKGREEN+"Väga hästi!"+ENDC)
            break

    while True:
        number4 = input("Proovi, panna midagi (mitte sõna): ").lower()
        if number4 not in listnumber[3]:
            print(OKRED+"Proovi uuesti" + ENDC)
            continue
        else:
            print(OKGREEN+"Väga hästi!"+ENDC)
            break

    while True:
        number5 = input("Proovi, panna midagi (mitte sõna): ").lower()
        if number5 not in listnumber[4]:
            print(OKRED+"Proovi uuesti" + ENDC)
            continue
        else:
            print(OKGREEN+"Väga hästi!"+ENDC)
            break

    print(":3, siis... *viskab sulle joogi peale*")
    print("and ja, see sõna oli viski")

# their wordle idk how to call this
if tase == 2:
    gogomylist = ["viski", "leib", "riigikogu", "ligma", "coolkid"]
    randomgogolist = choice(gogomylist)
    tryanddontexplode=6
    while True:
        userdosomething=input("Panna sõna: ").lower()
        if userdosomething not in randomgogolist:
            tryanddontexplode -= 1
            if tryanddontexplode == 0:
                print(f"olete kaotanud! {OKRED}>:D{ENDC}")
                break
            print(OKRED +"nuh uh"+ENDC)
            continue
        else:
            print(OKGREEN+"Väga hästi!"+ENDC)
            break
print(f"Õige sõna oli {randomgogolist}!")