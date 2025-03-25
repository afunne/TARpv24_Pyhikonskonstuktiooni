from MODULEfunctionspracticetasklol import *

# 1
tehe, username, password = registreerimine()
print(f"Kasutajanimi: {username}, Parool: {password}")

# 2
# https://www.w3schools.com/python/python_dictionaries.asp
usersstore = {username: password}

print("\n Tere Tulemast! Loggi sisse")
checking = autoriseerimine(usersstore)

if checking:
    print("Tere tulemast!")
else:
    print("Proovi uuesti.")

# 3
# old info
usersstore = {username: password}
usersstore = muuda_kasutajat(usersstore)

print("Uuendatud kasutajad:", usersstore)

# 4
usersstore = {username: password}
usersstore = unu_par_tast(usersstore)
print("Uus kasutaja:", usersstore)

# 5
lõpetamine()




