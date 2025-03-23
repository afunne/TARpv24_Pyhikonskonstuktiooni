from telnetlib import EC
from module_YEAHFUNCTIONSYUHUU import *
from datetime import datetime

a=float(input("Sisesta arv 1: "))
b=float(input("Sisesta arv 2: "))
t=input("Tehe: ")
v=arithmetic(a, b, t)
print(v)
# is_year_leap funktiooni kasutamine
aasta=int(input("Mis aasta tahad kontrollida?: "))
if aasta>0:
    v=is_year_leap(aasta)
    print(v)
    if v:
        print(f"{aasta} on liigaasta")
    else:
        print(f"{aasta} ei ole liigaasta")
# square funktsiooni kasutamine
S, P, d = square_list(float(input("Sisesta külg: ")))
print(S, P, d)

# write a number and get your
kuu = season(int(input("Panna number ya näita mis astaaeg see on: ")))
print(kuu)

while True:
    try:
        a = float(input("Sisesta summa: "))
        b = float(input("Sisesta aastate arv: "))
        v = bank(a, b)
        print(v)
        break
    except:
        ("WAAAH, WAAAAAH!")
        a = float(input("Sisesta summa: "))
        b = float(input("Sisesta aastate arv: "))

arg=int(input("Sisesta summa: "))
vastus=is_prime(arg)
print(vastus)

# 7
print(is_valid_date(31, 12, 2025))
print(is_valid_date(31, 2, 2025))

# 8 I wanna kms
text = input("Sisesta midagi: ")
key = 42

encrypted = XOR_cipher(text, key)
print("Krüptograafiline tekst:", encrypted)

decrypted = XOR_uncipher(encrypted, key)
print("Dekrüpteeritud tekst:", decrypted)

