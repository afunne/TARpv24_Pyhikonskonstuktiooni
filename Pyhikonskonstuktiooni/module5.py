# from random import *
# #näidis 1
# arv=randint(0,10)
# print(arv)
# if arv>5:
#     print("***********************")
#     print(f"arv {arv} suurem kui 5")
#     print("***********************")
# if arv>5: print(f"arv {arv} suurem kui 5")
# if arv<5:
#     print("***********************")
#     print(f"arv {arv} väikem kui 5")
#     print("***********************")
# if arv<5:print(f"arv {arv} väikem kui 5")
# if arv==5:
#     print("***********************")
#     print(f"arv {arv} on 5, LMAO")
#     print("***********************")
# if arv==5:print(f"arv {arv} on 5, LMAO")

# #Näidis
# arv=randint(-10,10)
# if arv>0:
#     print("Poaitiivne")
# else:
#     print("Negatiivne") #viga

# if arv>0:
#     print("Poaitiivne")
# elif arv==0:
#     print("0")
# else:
#     print("Negatiivne")


# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isascii()	Returns True if all characters in the string are ascii characters
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle() 	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case

from random import Random


NameKey=input("Mis on sinu nimi? ")
pilet=print()
if NameKey.isupper() and NameKey.lower()=="juku":
    print("Lahme kinno")
    try:
        vanus=int(input("Kui vana sa oled? "))
        if vanus<0 or vanus>100:
            pilet="!!!"
            print(pilet)
        if vanus<6:
            pilet="Tasuta"
            print(pilet)
        elif vanus<=14:
            pilet="lastepilet"
            print(pilet)
        elif vanus<=65:
            pilet="täospilet"
            print(pilet)
        elif vanus<=100:
            pilet="Sooduspilet"
            print(pilet)
    except Exception as e:
        print("Tekkis viga: ", e)
else:
    print(":| Kes see on?")

#ülasane 2
from random import *

MrNimi1 = input("Arva, kes on minu esimene pindinabrid: ")
MrNimi2 = input("Arva, kes on minu teine pindinabrid: ")

arv = random.randint(0,1)


if (MrNimi1 == "Maksim" and MrNimi2 == "Nikita") or (MrNimi1 == "Nikita" and MrNimi2 == "Maksim"):
    print("Õige")
else:
    print("Vale")

# ülisane 3
print("Answer with Yes [Y], No [N]")
try:
    küsimus = input("Kas te tahete remondi tegemise soov? ")
    Price_M2 = float(input("Panna kui palju maksab: "))
    if küsimus == "Y":
        tallnes = float(input("Palun, panna pikkus meetris: "))
        wide = float(input("Palun, panna laius meetris: "))
        P = tallnes * wide
        print(f"Pindala on {round(P,2)} meetris^2.")
        koos_hind = P * Price_M2
        print(f"Koos on {round(koos_hind,2)} eurot.")

    if küsimus == "N":
        print(":<")
    else:
        print("BRUUUH")
except Exception as e:
    print("Tekkis viga: ",e)

# ülisane 4
try:
    if koos_hind >= 700:
        PriceWith_DIS =  koos_hind * 0.30
        print(f"Praegu maksab {round(PriceWith_DIS),2} eurot.")
    else:
        print("Bro, idk")
except Exception as e:
    print("Tekkis viga: ",e)

# ülisane 5
try:
    AnswerFor1MDollas = int(input("Mis temperatuur praegu on? "))
    if AnswerFor1MDollas >= 18:
        print("soovitav toasoojus talvel")
    elif AnswerFor1MDollas < 18:
        print("pannan toasoojus talvel")
    elif AnswerFor1MDollas < -100:
        print("Bro, return back from Antartica :skull emoji:")
    else:
        print("How?")
except Exception as e:
    print("Tekkis viga: ",e)

# ülisane 6
try:
    height = float(input("Kui pikk sa oled santimeetris? "))
    if height <= 130:
        print("vaike")
    elif height >= 150:
        print("keskeline")
    elif height >= 190:
        print("suur")
except Exception as e:
    print("Tekkis viga: ",e)

# ülisane 7
try:
    gender = input("Kas te olete naine voi mees? ")
    height2 = float(input("Kui pikk sa oled santimeetris? "))
    if gender == "mees":
         if height <= 130:
            print("vaike")
         elif height >= 150:
            print("keskeline")
         elif height >= 190:
            print("suur")
    if gender == "naine":
         if height <= 120:
          print("vaike")
         elif height >= 140:
          print("keskeline")
         elif height >= 180:
          print
except Exception as e:
    print("Tekkis viga: ",e)

# ülisane 8
try:
    bread = int(input("Kui palju leiva te tahate? "))
    milk = int(input("Kui palju piima te tahate? "))
    Bakery_thingy = int(input("Kui palju saia te tahate? "))
    Price_B = 1.00
    Price_M = 1.56
    Price_BT = 0.79
    inflation1 = bread * Price_B
    inflation2 = milk * Price_M
    inflation3 = Bakery_thingy * Price_BT
    print(f"leib maksab {round(inflation1,3)}, piim maksab {round(inflation2,3)} ja saiad maksab {round(inflation3,3)}")
except Exception as e:
    print("Tekkis viga: ",e)

# ülisane 9
try:
    side1 = float(input("Kui pikk see ruudu? "))
    side2 = float(input("Kui pikk see ruudu? "))
    side3 = float(input("Kui pikk see ruudu? "))
    side4 = float(input("Kui pikk see ruudu? "))
    if (side1 >0 and side2 >0 and side3 >0 and side4 >0):
        print("ruut on oige")
    else:
        print("ruut on vale")
except Exception as e:
    print("Tekkis viga: ",e)

# ülisane 10
try:
    a = float(input("Panna esimene number: "))
    b = float(input("Panna teine number: "))
    question = input("Mida arvutimine te tahate? ")
    if question == "+":
        answer1 = a + b
        print(f"vastus on {round(answer1,2)}.")
    if question == "-":
        answer2 = a - b
        print(f"vastus on {round(answer2,2)}.")
    if question == "*":
        answer3 = a * b
        print(f"vastus on {round(answer3,2)}.")
    if question == "/":
        answer4 = a / b
        print(f"vastus on {round(answer4,2)}.")
except Exception as e:
    print("Tekkis viga: ",e)

# ülisane 11

# from datetime import datetime

# sunnipaev = int(input("Sisesta oma sünnipaev: "))

# now_aeg = datetime.now().year
# vastus = now_aeg - sunnipaev
# print(vastus)

import datetime

praegu = datetime.date.today()
date_entry = input('Panna andmed YYYY-MM-DD formatis')
until = praegu - date_entry

year, month, day = map(int, date_entry.split('-'))
date1 = datetime.date(year, month, day)
print(f"Sinu sunnipaev tuleb {until.days}. ")

# ülisane 12
Panimine = float(input("Panna hind (euros): "))
if Panimine == 10:
    allahind = Panimine % 0.10
    print("hind on "+allahind)
if Panimine > 10:
    allahind = Panimine % 0.20
    print("hind on "+allahind)
# ülisane 13
try:
    genderagainlol = input("Kas te olete naine voi mees? ")
    if genderagainlol == "mees":
        age = int(input("Kui vana sa oled?"))
        if age >= 16:
            print("Tere tulemast meeskonda!")
        elif age < 16:
            print("Vabadust, aga te ei saate tulla")
    if genderagainlol == "naine":
        print("GET OUT!")
except Exception as e:
    print("Tekkis viga: ",e)

# ülisane 14
# look my imagination was at limit :|
