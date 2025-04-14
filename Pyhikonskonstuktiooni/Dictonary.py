from module_Dictonary import *

while True:
    print("""
1 - Tõlgi eesti -> vene
2 - Tõlgi vene -> eesti
3 - Lisa uus sõna
4 - Paranda sõna
5 - Testi teadmisi
0 - lõppimine
"""
)
    try:
        valik=int(input("Tee on valik: "))
    except:
        print("h u h")
        continue

    if valik == 1:
        print()
        tolgi_est_rus(sonastik)
    elif valik == 2:
        print()
        tolgi_rus_est(sonastik)

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
    else:
        print(".╭╮.")
        continue
