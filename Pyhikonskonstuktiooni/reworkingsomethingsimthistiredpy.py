from MODULEduh import *

users_list = []  # it safes everything here (kasutajanimi, parool)

while True:
    print("\n--- Kasutajate Haldus ---") # wow, something that looks like GUI???
    print("1. Registreeri uus kasutaja")
    print("2. Logi sisse")
    print("3. Muuda kasutajanime või parooli")
    print("4. Lähtesta parool")
    print("0. Lõpeta programm")

    valik = input("Vali tegevus: ").strip() # sometimes I wrote things too fast I somehow added spaces around

    if valik == "1":
        users_list = registreerimine(users_list)
    elif valik == "2":
        autoriseerimine(users_list)
    elif valik == "3":
        users_list = muuda_kasutajat(users_list)
    elif valik == "4":
        users_list = unu_par_tast(users_list)
    elif valik == "0":
        lõpetamine()
        break  # just for safety
    else: # it could be try and except but it is more simpler in my opinion
        print("Vigane valik, proovi uuesti!")
        continue
