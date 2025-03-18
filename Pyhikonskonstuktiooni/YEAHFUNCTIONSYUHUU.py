from module_YEAHFUNCTIONSYUHUU import *
# a=float(input("Sisesta arv 1: "))
# b=float(input("Sisesta arv 2: "))
# t=input("Tehe: ")
# v=arithmetic(a, b, t)
# print(v)
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