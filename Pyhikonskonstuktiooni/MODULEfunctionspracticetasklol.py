import re
from random import *
import secrets
import string

# def registreerimine(username:str,paroolXD:str,tehe:int)->any:
#     """
#     See funktsion teeb või küsis kasutajanimist ja parolist
#     """
#     while True:
#         if tehe in [1, 2]:
#             pass
#         else:
#             print("*insert cat exploding gif*")
#         if username is None:
#             print("Nuh uh")
#             continue
#         else: pass

#         if username.isalpha:
#             pass
#         else:
#             print("Nuh uh")
#             continue

#         if username.isdigit:
#             pass
#         else:
#             print("Nuh uh")
#             continue
#         regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')  
#         if(regex.search(registreerimine) == None):
#             break
#         else:
#             print("Nuh uh")
#             continue
#     return username, paroolXD, tehe

# def registreerimine(tehe:int, username:str, password:str) ->any:
#     """
#     See funktsion teeb või küsis kasutajanimist ja parolist
#     """
#     while True:
#         username = input("Sisesta sinu kasutajanimi: ")
#         if username == None:
#             print("Nuh uh")
#             continue
#         else: pass

#         tehe= int(input("Kas te tahate looda sinu parol iseseisvalt või AI-ga [1, 2]: "))
#         if tehe ==1:
#             password = input("Sisesta sinu parool: ")
#             if password == None:
#                 print("Nuh uh")
#                 continue
#             elif password.isalpha:
#                 pass
#             elif password.isdigit:
#                 pass
#             regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
#             if (regex.search(password) == None):
#                 continue
#             else:
#                 print("Yuh uh")
#                 break
#         elif tehe==2:
#             i=input("Sisesta täht => ")
#             if(i.isupper()):
#                 print("See on suur täht", i)
#             a=input("Sisesta arv => ")
#             if (a.isdigit()):
#                 print("See on täisarv ", a)
#         else:
#             print("XD")
#             continue
#     return tehe, username, password


def registreerimine() -> tuple:
    """
    See funktsioon küsib kasutajalt kasutajanime ja parooli.
    """
    while True:
        username = input("Sisesta sinu kasutajanimi: ")
        if not username:  # == None (ik it looks retarted, but it works)
            print("Kasutajanimi ei saa olla tühi!")
            continue

        try:
            tehe = int(input("Kas te tahate luua parooli iseseisvalt või AI-ga [1, 2]: "))
        except:
            print("Palun sisesta number 1 või 2")
            continue

        if tehe == 1:
            while True:
                password = input("Sisesta sinu parool: ")
                if not password: # == None
                    print("Parool ei saa olla tühi!")
                    continue
                
                # If it finds out you didn't follow anything pwend Sword Fight on the Heights IV
                has_letter = any(password.isalpha() in password)
                has_digit = any(password.isdigit() in password)
                has_special = bool(re.search('[@_!#$%^&*()<>?/\|}{~:]', password))
                
                if not (has_letter and has_digit and has_special): # if not all requirements are met, you get pwend in SOHF
                    print("Parool peab sisaldama nii tähti, numbreid kui ka erimärke")
                    continue
                else:
                    break
            break
        elif tehe == 2:
            # if you are asking me why I didnt use the code on the example, its because it didn't work
            # Yeah I took it from a forum and changed into my taste >:D
            # https://www.codingal.com/coding-for-kids/blog/create-random-password-generator-program-using-python/
            letters = string.ascii_letters
            digits = string.digits
            special_chars = string.punctuation
            selection_list = letters + digits + special_chars
            password = ''
            password += ''.join(secrets.choice(selection_list))
            print(password)

    return tehe, username, password

# 2
# def autoriseerimine(users_db: dict) -> bool:
#         """
#         Kontrollib, kas kasutaja sisestas õige kasutajanime ja parooli.
#         """
#         username = input("Sisesta kasutajanimi: ")
#         password = input("Sisesta parool: ")
    
#         if username in users_db and users_db[username] == password:
#             print("Sisselogimine õnnestus!")
#             return True
#         else:
#             print("Vale kasutajanimi või parool!")
#             return False

def autoriseerimine(users_list: list) -> bool:
    """
    Kontrollib, kas kasutaja sisestas õige kasutajanime ja parooli.
    Kasutajate andmed on listis kujul [(kasutajanimi1, parool1)...]
    """
    username = input("Sisesta kasutajanimi: ")
    password = input("Sisesta parool: ")
    
    if users_list[0] == username and users_list[1] == password:
        print("Sisselogimine õnnestus!")
        return True
    
    print("Vale kasutajanimi või parool!")
    return False

# 3
# def muuda_kasutajat(userstore: dict) -> dict:
#     """
#     Lubab kasutajal muuta oma kasutajanime või parooli.
#     """
#     while True:
#         # Autentimine enne muutmist
#         print("Kas te tahate mudada midagi?: ")

#         tries=4

#         print("Nuh uh, ma pean provima!")
#         username = input("Kasutajanimi: ")
#         password = input("Parool: ")
    
#         if username not in userstore or userstore[username] != password:
#             while username not in userstore or userstore[username] != password:
#                 print("Vale kasutajanimi või parool!")
#                 tries -= 1
#                 username = input("Kasutajanimi: ")
#                 password = input("Parool: ")
#                 if tries == 0:
#                     print("Proovide arv on otsas.")
#                     break

#         print("1. Muuda kasutajanimi ja parool")
#         print("0. Ei taha")
#         valik = int(input("Sisesta valik: "))
    
#         if valik == 0:
#             uus_nimi = input("Sisesta uus kasutajanimi: ")
#             if uus_nimi in userstore:
#                 print("See kasutajanimi on juba kasutusel!")
#             else:
#                 userstore[uus_nimi] = userstore.pop(username)
#                 print("Kasutajanimi muudetud edukalt!")

#             uus_parool = input("Sisesta uus parool: ")
#             if not uus_parool: # == None
#                     print("Parool ei saa olla tühi!")
#                     continue
                
#                 # If it finds out you didn't follow anything pwend Sword Fight on the Heights IV
#             has_letter = any(uus_parool.isalpha() in uus_parool)
#             has_digit = any(uus_parool.isdigit() in uus_parool)
#             has_special = bool(re.search('[@_!#$%^&*()<>?/\|}{~:]', uus_parool))
                
#             if not (has_letter and has_digit and has_special): # if not all requirements are met, you get pwend in SOHF
#                 print("Parool peab sisaldama nii tähti, numbreid kui ka erimärke")
#                 continue
#             else:
#                  pass
        
#             userstore[username] = uus_parool
#             print("Parool muudetud edukalt!")
    
#         elif valik == 0:
#             break
#         return userstore

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
    
        if valik == 1:
            uus_nimi = input("Sisesta uus kasutajanimi: ")
            if uus_nimi in users_list:
                print("See kasutajanimi on juba kasutusel!")
            else:
                users_list[uus_nimi] = users_list.pop(username)
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

# 4
# def unu_par_tast(userstore):
#     username = input("Username to reset: ")
#     if username in userstore:
#         userstore[username] = "test"  # Set a default temporary password
#         print('Password reset to "test"')
#     else:
#         print("huh")

# def unu_par_tast(usersstore: dict) -> dict:
#     """
#     I wanna kms
#     """
#     print("Kaboom, here goes your tower. Feel it crumble. Feel the power. Afunne codes this #### in 5 am")
#     while True:
#         username = input("Kasutajanimi: ")
    
#         if username not in usersstore:
#             print("NUH UH!")
#             continue
#         else:
#             pass
#         password = input("Parool: ")

#         if password not in usersstore:
#             print("NUH UH!")
#             continue
#         else:
#             pass
#         password_new = input("Parool: ")
#         has_letter = any(password_new.isalpha() in password_new)
#         has_digit = any(password_new.isdigit() in password_new)
#         has_special = bool(re.search('[@_!#$%^&*()<>?/\|}{~:]', password_new))
                
#         if not (has_letter and has_digit and has_special): # if not all requirements are met, you get pwend in SOHF
#             print("Parool peab sisaldama nii tähti, numbreid kui ka erimärke")
#             continue
#         else:
#             pass

#         usersstore[username] = password_new
    
#         print(f"Sinu uus parool: {password_new}")
#         break
#     return usersstore


def unu_par_tast(usersstore: list) -> list:
    """
    I wanna kms
    Usersstore on nüüd loend topeltest: [("user1", "pass1")]
    """
    print("Kaboom, here goes your tower. Feel it crumble. Feel the power. Afunne codes this #### in 5 am")
    while True:
        username = input("Kasutajanimi: ")
       
        if username not in usersstore:
            print("NUH UH!")
            continue
        else:
            pass
        password = input("Parool: ")

        if password not in usersstore:
            print("NUH UH!")
            continue
        else:
            pass
        password_new = input("Parool: ")
        has_letter = any(password_new.isalpha() in password_new)
        has_digit = any(password_new.isdigit() in password_new)
        has_special = bool(re.search('[@_!#$%^&*()<>?/\|}{~:]', password_new))
                
        if not (has_letter and has_digit and has_special): # if not all requirements are met, you get pwend in SOHF
            print("Parool peab sisaldama nii tähti, numbreid kui ka erimärke")
            continue
        else:
            pass
# 5
def lõpetamine():
  print("lõpetamine")

