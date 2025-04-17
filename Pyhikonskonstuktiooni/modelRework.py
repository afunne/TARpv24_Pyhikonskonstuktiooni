import re
import secrets
import string

# some things have been done in Discord VC. Some things are written short but it works the same

def registreerimine(users_list: list) -> list:
    """
    Registreerib uue kasutaja ja lisab selle loendisse.
    """
    while True:
        username = input("Sisesta kasutajanimi: ").strip() # sometimes it would give out errors after copying the password, it just here so no mistakes can happen
        if not username: # the saem as usernaem = "" or username is None
            print("Kasutajanimi ei saa olla t�hi!")
            continue

        # checks the username only
        for user, _ in users_list:
            if user == username:
                print("See kasutajanimi on juba v�etud! Proovi teist.")
                continue

        try:
            tehe = int(input("Kas tahad parooli luua iseseisvalt (1) v�i auto-ga (2)? "))
        except:
            print("Palun sisesta number 1 v�i 2!")
            continue

        if tehe == 1:
            while True:
                password = input("Sisesta parool: ")
                if not password:
                    print("Parool ei saa olla t�hi!")
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
                    print("Parool peab sisaldama t�hti, numbreid ja erim�rke!")
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
        print("Registreerimine �nnestus!")
        return users_list


def autoriseerimine(users_list: list) -> bool:
    """
    Kontrollib, kas kasutaja sisestas �ige kasutajanime ja parooli.
    """
    username = input("Sisesta kasutajanimi: ").strip()
    password = input("Sisesta parool: ").strip()

    for user, pwd in users_list:
        if user == username and pwd == password:
            print("Sisselogimine �nnestus!")
            return True
        else:
            print("Vale kasutajanimi v�i parool!")
            return False


def muuda_kasutajat(users_list: list) -> list:
    """
    Lubab kasutajal muuta oma kasutajanime v�i parooli.
    """
    username = input("Sisesta praegune kasutajanimi: ").strip()
    password = input("Sisesta praegune parool: ").strip()
    if username and password in users_list:
        print("Tere tagasi!")
    if not username and password in users_list:
        print("Vale kasutajanimi v�i parool!")
        tries = 4
        while tries != 0:
            username = input("Sisesta praegune kasutajanimi: ").strip()
            password = input("Sisesta praegune parool: ").strip()
            if username and password in users_list:
                print("Tere tagasi!")
                break
            if not username and password in users_list:
                print("Vale kasutajanimi v�i parool!")
                tries -= 4
                if tries == 0:
                    print("Sissetungija!")
                    exit()
                else:
                    continue
            


    # function enumerate suggested by TS

    # enumerate() function adds a counter to each item in a list or other iterable.
    # It turns the iterable into something we can loop through, where each item comes with its number (starting from 0 by default).
    # We can also turn it into a list of (number, item) pairs using list().


    for i, (user, pwd) in enumerate(users_list):
    # Check if the username and password match
        if user == username or uus_nimi and pwd == password or uus_parool:
        
            # Ask the user for a new username and password
            uus_nimi = input("Sisesta uus kasutajanimi: ").strip()
            tehe = int(input("Kas tahad parooli luua iseseisvalt (1) v�i auto-ga (2)? "))
            if tehe == 1:
                while True:
                    uus_parool = input("Sisesta parool: ")
                    if not uus_parool:
                        print("Parool ei saa olla t�hi!")
                        continue
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
                        # Thanks to TS once again
                        if has_letter and has_digit and has_special: # if they all = True
                            print("Parool on sobiv.")
                        else:
                            print("Parool peab sisaldama t�hti, numbreid ja erim�rke.")

                            if not (has_letter and has_digit and has_special): # if they aren't True
                                print("Parool peab sisaldama t�hti, numbreid ja erim�rke!")
                                continue
            if tehe ==2:
                # Define the pool of characters (letters, digits, and punctuation)
                letters = string.ascii_letters  # a-z, A-Z
                digits = string.digits          # 0-9
                punctuation = string.punctuation # Special characters (!, @, #, etc.)

                # Combine all possible characters into one string
                characters = letters + digits + punctuation

                # Initialize an empty string to store the password
                uus_parool = ""

                # Loop 10 times to pick 10 random characters from the pool
                for i in range(10):
                    # Randomly choose a character from the pool of characters
                    random_char = secrets.choice(characters)
    
                    # Append the chosen character to the password string
                    uus_parool += random_char

                # Print the generated password
                print(f"Sinu genereeritud parool: {uus_parool}")
        users_list.remove((username, password))
        username = uus_nimi
        password = uus_parool
        users_list.append((uus_nimi, uus_parool))
        print("Registreerimine �nnestus!")
        return users_list

def unu_par_tast(users_list: list) -> list:
    """
    L�htestab kasutaja parooli.
    """
    username = input("Sisesta kasutajanimi: ").strip()

    # thanks to TS helping me out here, password generator wrote time mutiple times, so this code kinda just prints the final result
    # at least it should

    # _ here is supposed to be password but it doesn't include it
    for i, (user, _) in enumerate(users_list):
    # Check if the current user matches the entered username
        if user == username:
        # Generate a new password with 8 characters (letters and digits)
            new_password = ""
            for i in range(8): # could be more, I jsut didn't want more checks to be honest :P
                random_char = secrets.choice(string.ascii_letters + string.digits)
                new_password += random_char
            # Update the user's password in the list
            users_list = (user, new_password)
            # Print the new password for the user
            print(f"Sinu uus parool: {new_password}")
            # Return the updated list
            return users_list
    print("Kasutajat ei leitud!")
    return users_list


def l�petamine():
    """V�ljub programmist."""
    print("Programm l�petatud.")
    exit()
