import re
def muuda_kasutajat(users_list: list) -> list:
    """
    Lubab kasutajal muuta oma kasutajanime või parooli.
    Kasutajate andmed on listis kujul [(kasutajanimi1, parool1)...]
    """
    while True:
        print("Kas te tahate midagi muuta?")
        tries = 4

        # Autentimine enne muutmist, duh
        print("Nuh uh, ma pean provima!")
        username = input("Kasutajanimi: ")
        password = input("Parool: ")
        
        users_list = [(username, password)]
        
        # Kui kasutajat pole või parool on vale
        while users_list[0] or users_list[1] is not users_list:
            print("Vale kasutajanimi või parool!")
            tries -= 1
            if tries == 0:
                print("Proovide arv on otsas.")
                return users_list


        print("1. Muuda kasutajanimi ja parool")
        print("0. Ei taha")
        valik = int(input("Sisesta valik: "))
    
        if valik == 0:
            uus_nimi = input("Sisesta uus kasutajanimi: ")
            if uus_nimi in users_list:
                print("See kasutajanimi on juba kasutusel!")
            else:
                users_list[uus_nimi] = users_list.pop(index)
                print("Kasutajanimi muudetud edukalt!")

            uus_parool = input("Sisesta uus parool: ")
            if not uus_parool: # == None
                    print("Parool ei saa olla tühi!")
                    continue
                
                # If it finds out you didn't follow anything pwend Sword Fight on the Heights IV
            has_letter = any(uus_parool.isalpha() in uus_parool)
            has_digit = any(uus_parool.isdigit() in uus_parool)
            has_special = bool(re.search('[@_!#$%^&*()<>?/\|}{~:]', uus_parool))
                
            if not (has_letter and has_digit and has_special): # if not all requirements are met, you get pwend in SOHF
                print("Parool peab sisaldama nii tähti, numbreid kui ka erimärke")
                continue
            else:
                 pass
        
            users_list[username] = uus_parool
            print("Parool muudetud edukalt!")
    
        elif valik == 0:
            break
        return users_list
