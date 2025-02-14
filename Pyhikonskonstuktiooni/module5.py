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






