from MODULEduh import *

users_list = []  # Loend kasutajatest (kasutajanimi, parool)

while True:
    print("\n--- Kasutajate Haldus ---")
    print("1. Registreeri uus kasutaja")
    print("2. Logi sisse")
    print("3. Muuda kasutajanime või parooli")
    print("4. Lähtesta parool")
    print("5. Lõpeta programm")

    valik = input("Vali tegevus: ").strip()

    if valik == "1":
        users_list = registreerimine(users_list)
    elif valik == "2":
        autoriseerimine(users_list)
    elif valik == "3":
        users_list = muuda_kasutajat(users_list)
    elif valik == "4":
        users_list = unu_par_tast(users_list)
    elif valik == "5":
        lõpetamine()
        break  # Oluline! Lõpetab while-tsükli
    else:
        print("Vigane valik, proovi uuesti!")
