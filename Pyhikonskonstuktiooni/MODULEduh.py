import re
import secrets
import string
import os

def registreerimine(users_list: list) -> list:
    """
    Registreerib uue kasutaja ja lisab selle loendisse.
    """
    while True:
        username = input("Sisesta kasutajanimi: ").strip()
        if not username:
            print("Kasutajanimi ei saa olla tühi!")
            continue

        for user, _ in users_list:
            if user == username:
                print("See kasutajanimi on juba võetud! Proovi teist.")
                continue

        try:
            tehe = int(input("Kas tahad parooli luua iseseisvalt (1) või AI-ga (2)? "))
        except ValueError:
            print("Palun sisesta number 1 või 2!")
            continue

        if tehe == 1:
            while True:
                password = input("Sisesta parool: ")
                if not password:
                    print("Parool ei saa olla tühi!")
                    continue
                
                has_letter = False
                has_digit = False
                has_special = False

                for c in password:
                    if c.isalpha():
                        has_letter = True
                    elif c.isdigit():
                        has_digit = True
                    elif re.search(r'[@_!#$%^&*()<>?/\|}{~:]', c):
                        has_special = True  


                if not (has_letter and has_digit and has_special):
                    print("Parool peab sisaldama tähti, numbreid ja erimärke!")
                    continue
                break

        elif tehe == 2:
            # Define the pool of characters (letters, digits, and punctuation)
            letters = string.ascii_letters  # a-z, A-Z
            digits = string.digits          # 0-9
            punctuation = string.punctuation # Special characters (!, @, #, etc.)

            # Combine all possible characters into one string
            characters = letters + digits + punctuation

            # Initialize an empty string to store the password
            password = ""

            # Loop 10 times to pick 10 random characters from the pool
            for i in range(10):
                # Randomly choose a character from the pool of characters
                random_char = secrets.choice(characters)
    
                # Append the chosen character to the password string
                password += random_char

            # Print the generated password
            print(f"Sinu genereeritud parool: {password}")


        users_list.append((username, password))
        print("Registreerimine õnnestus!")
        return users_list


def autoriseerimine(users_list: list) -> bool:
    """
    Kontrollib, kas kasutaja sisestas õige kasutajanime ja parooli.
    """
    username = input("Sisesta kasutajanimi: ").strip()
    password = input("Sisesta parool: ").strip()

    for user, pwd in users_list:
        if user == username and pwd == password:
            print("Sisselogimine õnnestus!")
            return True

    print("Vale kasutajanimi või parool!")
    return False


def muuda_kasutajat(users_list: list) -> list:
    """
    Lubab kasutajal muuta oma kasutajanime või parooli.
    """
    username = input("Sisesta praegune kasutajanimi: ").strip()
    password = input("Sisesta praegune parool: ").strip()

    for i, (user, pwd) in enumerate(users_list):
    # Check if the username and password match
        if user == username and pwd == password:
        
            # Ask the user for a new username and password
            uus_nimi = input("Sisesta uus kasutajanimi: ").strip()
            uus_parool = input("Sisesta uus parool: ").strip()

            # Check if the new password contains letters, digits, and special characters
            has_letter = False
            has_digit = False
            has_special = False
        
            # Loop through each character in the new password to check conditions
            for c in uus_parool:
                if c.isalpha():
                    has_letter = True
                elif c.isdigit():
                    has_digit = True
                elif re.search(r'[@_!#$%^&*()<>?/\|}{~:]', c):
                    has_special = True

        # Check if all required conditions are met for the new password
        if has_letter and has_digit and has_special:
            print("Parool on sobiv.")
        else:
            print("Parool peab sisaldama tähti, numbreid ja erimärke.")

            if not (has_letter and has_digit and has_special):
                print("Parool peab sisaldama tähti, numbreid ja erimärke!")
                continue

            users_list[i] = (uus_nimi, uus_parool)
            print("Kasutaja andmed uuendatud!")
            return users_list

    print("Vale kasutajanimi või parool!")
    return users_list


def unu_par_tast(users_list: list) -> list:
    """
    Lähtestab kasutaja parooli.
    """
    username = input("Sisesta kasutajanimi: ").strip()

    for i, (user, _) in enumerate(users_list):
    # Check if the current user matches the entered username
        if user == username:
        # Generate a new password with 8 characters (letters and digits)
            new_password = ""
            for _ in range(8):
                random_char = secrets.choice(string.ascii_letters + string.digits)
                new_password += random_char
        
            # Update the user's password in the list
            users_list[i] = (user, new_password)
        
            # Print the new password for the user
            print(f"Sinu uus parool: {new_password}")
        
            # Return the updated list
            return users_list

    print("Kasutajat ei leitud!")
    return users_list


def lõpetamine():
    """Väljub programmist."""
    print("Programm lõpetatud.")
    exit()