from module_Dictonary import *

# sonastik = lae_sonastik()

while True:
    print("""
1 - Tõlgi eesti -> vene
2 - Tõlgi vene -> eesti
3 - Lisa uus sõna
4 - Paranda sõna
5 - Testi teadmisi
0 - lõppimine
(hey, future me is here. I added a bunch of options to debug many things
I hope nobody minds it)
"""
)
    try:
        valik=int(input("Tee on valik: "))
    except:
        print("h u h")
        continue

    if valik == 1:
        print()
        tolgi_est_rus()
    elif valik == 2:
        print()
        tolgi_rus_est()

    elif valik == 3:
        print()
        lisa_sona()

    elif valik == 4:
        print()
        paranda_sona()

    elif valik == 5:
        print()
        testi_teadmisi()
    elif valik == 0:
        print("Bye, bye! <3 \n*lehvitab käega*")
        break
    elif valik == 6:
        Loe_failist()
    elif valik == 7:
        Kirjuta_failisse
    elif valik == 8:
        kuva_sonastik
    else:
        print(".╭╮.")
        continue
