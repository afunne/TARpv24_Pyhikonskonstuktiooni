#Ulasane
from datetime import *
from calendar import *
from math import *
from xml.sax import default_parser_list
tana=date.today()
print(f"Tere! Tana on {tana}")

# 27/12/2022
tana_ = tana.strftime("%d/%m/%Y")
paevadekogus=monthrange(2025,1)[1]
print(f"Jaanuaris on {paevadekogus} paeva")
paevad=tana.day
onjaanud=paevadekogus-paevad
print(f"Jaanuaris on {onjaanud} paeva")
# #1v
# aastalopuni=onjaanud+monthrange(2025,2)[1]+onjaanud+monthrange(2025,3)[1]+aastalopuni=onjaanud+monthrange(2025,4)[1]+onjaanud+monthrange(2025,5)[1]+(2025,2)[1]+onjaanud+monthrange(2025,6)[1]+aastalopuni=onjaanud+monthrange(2025,7)[1]+onjaanud+monthrange(2025,8)[1]+(2025,2)[1]+onjaanud+monthrange(2025,3)[1]+aastalopuni=onjaanud+monthrange(2025,9)[1]+onjaanud+monthrange(2025,10)[1]
# print(f"Aasta lõpuni on jaanud {aastalopuni}")

#2.V
aastalopuni=365-monthrange(2025,1)[1]+onjaanud
print(f"Aasta lõpuni on jaanud {aastalopuni}")

# print(f"Tere! Tana on {tana_}")
# # December 27, 2022
# tana_ = tana.strftime("%B %d, %Y")
# print(f"Tere! Tana on {tana_}")
# # 12/27/22
# tana_ = tana.strftime("%m/%d/%y")
# print(f"Tere! Tana on {tana_}")
# # Dec-27-2022
# tana_ = tana.strftime("%b-%d-%Y")
# print(f"Tere! Tana on {tana}")

#counting

#Ulasane 2
a=3+8/(4-2)*4

a=3+8/(2)*4

a=11/2*4

#Ulasane 3
try:
     R=float(input("R: "))
     Sruudu=round((2*R)**2,2)
     Sringi=round(pi*R**2,2)
     Pruudu=round(8*R,2)
     Pringi=round(2*pi*R,2)
     print(f"Vastus:nRuudu pindala on {Sruudu}, ruudu umbermoot on {Pruudu}, nringi pindala on {Sringi}, Ringi umbermeet on {Pringi}.")
except:
    print("Sisesta ujukomaarvud")

#Ülasane 4 (my version)
eurocoinR=0.00002575/2
maaR=6378
erinavalt=round(maaR/eurocoinR,2)
print(f"Vajab {erinavalt} 2 eurot")
#skbidi
d=2.575 # mündi d sm
maaR=6378 # maa radium sm
maaR*=100000 # maa radium sm
Pmaa=2*pi*maaR # maa ümbermõõt
kogus=Pmaa/d
print(f"Meil on vaja {int(kogus):,d} mündi")
print(f"Meil on vaja {int(kogus*2):,d} euro")

#Ülasane 5
a="kill-koll ".capitalize()
b="killadi-koll ".capitalize()
print(a*2,b,a*2,b,a*4)

#Ülasane 6
skibidi="""Rong see sõitis tsuhh tsuhh tsuhh,
piilupart oli rongijuht.
Rattad tegid rat tat taa,
rat tat taa ja tat tat taa.
Aga seal rongi peal,
kas sa tead, kes olid seal?"""
skibidi2="""Rong see sõitis tuut tuut tuut,
piilupart oli rongijuht.
Rattad tegid kill koll koll,
kill koll koll ja kill koll kill."""
print(skibidi.upper())
print()
print(skibidi2.upper())

#Ülasane 7
try:
    a=float(input("mis on a?: "))
    b=float(input("mis on b?: "))
    if a>0 and b>0:
        print("Pindala ja ümbermõõdu rvutamine: ")
        P=(a+b)*2
        S=a*b
        print(f"P on {P} ja S on {S}")
    else:
        print("Arvud peavadc suurem kui 0 olla!")
except:
    print("Nuh uh")

#Ülasane 8
liitrid=float(input("mis on liitrid?: "))
kilometrid=float(input("mis on kilometrid?: "))
vastus=liitrid/kilometrid*100
print(f"Kütusekulu arvutamine on {round(vastus,2)}")

#Ülasane 9
print("did you know that avarge speed of a skateboard is 29,9km/h? insertn nerd emoji")

try:
    kiirus=29,9 #kilometrris
    M=float(input("Kui kaugele jõuab M minutiga?: "))
    if M>0:
        print("aeg avutamine: ")
        viis=kiirus*M
        print(f"viis on {viis}")
    else:
        print("Arvud peavad suurem kui 0 olla!")
except:
    print("Nuh uh")

#Ülasane 10
try:
    aeg=float(input("Kui palju minutit te tahate arvitida: "))
    if a>0 and b>0:
        print("aeg avutamine: ")
        minutit=aeg//60 #tundid
        balling=aeg%60 #minutit
        print(f"aeg on {round(minutit,2)}:{round(balling),2}")
    else:
        print("Arvud peavad suurem kui 0 olla!")
except:
    print("Nuh uh")