# plokkskeem töö
#minu V4 vastus pole mind
vastus=0
p=int(input("Mitu korda kordame?"))
while True:
    arv=float(input("Sisesta arv: "))
    arv2=float(input("Sisesta arv: "))
    if arv<0:
        vastus+=arv
    p-=1
    if p==0: break
print("Summa on: ", vastus)


#M variant (I like this one more tbh)
vastus=0
try:
    p=int(input("Mitu korda kordame?"))
    for i in range(p):
        arv=float(input("Sisesta arv: "))
        if arv<0: vastus+=arv
    print("Summa on: ", vastus)
except:
    print("Nuh uh")




# for i in range(20)








#V5
for õ in range(20):
    print(f"Soritab eksamit {õ+1}. õpilane")
    for e in range(3):
        print(f"{e+1}. eksam")


#V1
kokku=100
panni_maht=6
aeg=1

import time
kutletArv=int(input("mitu kotlet te tahate?: "))
Vabakoht=int(input("Panni maht: "))
aeg=1
lahenemine=kutletArv//Vabakoht
jaak=kutletArv%Vabakoht
if jaak>0: lahenemine +=1
print(f"Praeme. Tuleb {lahenemine} lahenemist.")
for l in range(lahenemine):
    if jaak>0 and l ==lahenemine-1:
        print(f"Panni peal on {jaak} kotlet.")
    else:
        print(f"Panni peal on {kutletArv} kotlet.")
    print(f"{l+1}. Lahnemine. Praeme esimene pool.")
    time.sleep(aeg)
    print("Ümberpöörame")
    print(f"{l+1}. lahenemine. Praeme teine pool")
    time.sleep(aeg)
    print(f"Valmis!")
print("Kõik kotletid on praetud!")



#minu v4
while True:
    try:
        a = float(input("a: "))
        b = float(input("b: "))
        if a == b: print("Väle! Proovi uuesti!")
        elif a != b:
            print("Õige")
            if a>b:
                print(f"V= {a} suurem kui {b}")
                break
            elif a<b:
                print(f"V= {b} suurem kui {a}")
                break
    except:
        print("Nuh uh")

# lõpilne ;p
print("3 sõprat tulevad  restorani jurresse ja sealpeal on roboot.")
tuli = 0
try:
    sõber1 = float(input("Kui vannad ta on?: "))
    if sõber1 >= 16:
        print("Tuli!")
        tuli += 1 # dude im suprsied I somehow though of that mgl
    else:
        print("ära tuli!")
except:
    print("DANG, ma küsisin astaa mitte nimi...")

try:
    sõber2 = float(input("Kui vannad ta on?: "))
    if sõber2 >= 16:
        print("Tuli!")
        tuli += 1
    else:
        print("ära tuli!")
except:
    print("DANG, ma küsisin astaa mitte nimi...")

try:
    sõber3 = float(input("Kui vannad ta on?: "))
    if sõber3 >= 16:
        print("Tuli!")
        tuli += 1
    else:
        print("ära tuli!")
except:
    print("DANG, ma küsisin astaa mitte nimi...")

if tuli == 3:
    print("Kõik tulevad! yay! :D")
elif tuli == 2:
    print("Kaks sõbrad tulevad... :<")
elif tuli == 1:
    print("Minu arust see on väga ebahuvitav... :_<")
elif tuli == 0:
    print("Mitte keegi tulenud. :|")