# print("Tere maailm!")
# nimi=input("Mis sinu nimi on?: ")
# aastat=int(input("kui vana sa oled?: "))
# pikkus=int(input("kui pikk sa oled?: "))
# vastus="Tere, maailm!", nimi
# vastus2="Sa oled", aastat, "aastat vana"
# vastus3="Sa oled", pikkus, "pikkus"
# print(vastus, vastus2, vastus3)
#check
# aastat = 18
# eesnimi = "Jaak"
# pikkus = 16.5
# kas_käib_koolis = True
# #types
# print(type(vastus))
# print(type(vastus2))
# print(type(vastus3))
# print(kas_käib_koolis, type (kas_käib_koolis))

# if kas_käib_koolis:
#     print(nimi, kas_käib_koolis)
# else:
#     print(nimi, "ei käi")

# #kommid
# kommid=int(input("kui kommid" " " + nimi + " " "pannab?: "))
# vastus="laual on", kommid
# if kommid >= 40:
#     print("._.   mitter palju?")
# else:
#     print(vastus)
# -- all of this is my first try, idk



# -- this is my second try
# #first
# print("Tere maailm!")
# nimi=input("Mis sinu nimi on?: ").capitalize()
# print(f"Tere maailm!, Tervitan sind {nimi}")
# aastat=int(input("kui vana sa oled?: "))
# print(f"Tere maailm!, Tervistan sind {nimi}! Sa oled {aastat} aastat vana")

#this is the second one (who could have guessed?)
aastat = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True
#types
print(type(f"Muutaja {aastat} on {type(aastat)}"))
print(type(f"Muutaja {eesnimi} on {type(eesnimi)}"))
print(type(f"Muutaja {pikkus} on {type(pikkus)}"))
print(type(f"Muutaja {kas_käib_koolis} on {type(kas_käib_koolis)}"))

#third one
 #kommid
from random import * 

kommide_arv=randint(10,100)
print(f"Laua peal on {kommide_arv}")
mitu=int(input("Mitu tahad süüja"))
print(f"Laual peal on jäänud {kommide_arv-mitu}")

# 4th one
import math
puu=float(input("mis on puu diametr?: "))
print("vastus on", puu*math.pi)

#5th one
N=float(input("mis on N?: "))
M=float(input("mis on M?: "))
print("vastus on", N*M)

#6th one
aeg = int(input("Mitu tundi kulus sõiduks (sekundid)? "))
teepikkus = int(input("Mitu kilomeetrit sõitsid (meetrit)? "))
print(f"sinu kiirus on: {teepikkus/aeg}")

#7th one
esimene_number=float(input("mis on esimene number?: "))
teine_number=float(input("mis on teine number?: "))
kolmas_number=float(input("mis on kolmas number?: "))
neljas_number=float(input("mis on neljas number?: "))
vies_number=float(input("mis on vies number?: "))
print(f"sinu kiirus on: {esimene_number+teine_number+kolmas_number+neljas_number+vies_number}")

#8th one
print("  @..@")
print(" (----)")
print("( \__/ )")
print('^^ "" ^^')

#9th one
a=float(input("mis on a?: "))
b=float(input("mis on b?: "))
c=float(input("mis on c?: "))
print(f"P on: {a+b+c}")

#10th one
hind=12.90
tip=hind+0.10
summa=hind+tip
from random import * 
sõbra=randint(2,4)
print(f"Laual juures on {sõbra}")
print(f"Nad ostavad {round(summa/sõbra,2)}")