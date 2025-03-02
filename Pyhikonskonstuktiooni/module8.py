from random import *

TaseKüsimus=input("Panna sinu tase: ")
countertrue=0
counterfalse=0


while True:
    try:
        if TaseKüsimus == "Tase 1":
            tehed=["+","-"]
            valitud_tehe=choice(tehed)
            print(valitud_tehe)
            if valitud_tehe=="+":
                print("Oli valitud summa")
            a=randint(0,5)
            b=randint(0,5)
            print(f"Millega võrdub {a} {valitud_tehe} {b} =")
            vastus=int(input("Anna vastus: "))
            if vastus==eval(str(a)+valitud_tehe+str(b)):
                print("Tore!")
                countertrue+=1
            else:
                print("Vale!")
                counterfalse+=1
        TaseKüsimus2=input("kas soovite jätkata?: ")
        if TaseKüsimus2 == "jah":
           TaseKüsimus=input("Panna sinu tase: ")
        elif TaseKüsimus2 == "ei":
            break
    except:
        print("BRUH")



while True:
    try:
        if TaseKüsimus == "Tase 2":
            tehed=["+","-","*","/"]
            valitud_tehe=choice(tehed)
            print(valitud_tehe)
            if valitud_tehe=="+":
                print("Oli valitud summa")
            a=randint(0,5)
            b=randint(0,5)
            print(f"Millega võrdub {a} {valitud_tehe} {b} =")
            vastus=int(input("Anna vastus: "))
            if vastus==eval(str(a)+valitud_tehe+str(b)):
                print("Tore!")
                countertrue+=1
            else:
                print("Vale!")
                counterfalse+=1
        TaseKüsimus2=input("kas soovite jätkata?: ")
        if TaseKüsimus2 == "jah":
           TaseKüsimus=input("Panna sinu tase: ")
        elif TaseKüsimus2 == "ei":
            break
    except:
        print("BRUH")


while True:
    try:
        if TaseKüsimus == "Tase 3":
            tehed=["+","-","*","/", "**"]
            valitud_tehe=choice(tehed)
            print(valitud_tehe)
            if valitud_tehe=="+":
                print("Oli valitud summa")
            a=randint(0,5)
            b=randint(0,5)
            print(f"Millega võrdub {a} {valitud_tehe} {b} =")
            vastus=int(input("Anna vastus: "))
            if vastus==eval(str(a)+valitud_tehe+str(b)):
                print("Tore!")
                countertrue+=1
            else:
                print("Vale!")
                counterfalse+=1
        TaseKüsimus2=input("kas soovite jätkata?: ")
        if TaseKüsimus2 == "jah":
           TaseKüsimus=input("Panna sinu tase: ")
        elif TaseKüsimus2 == "ei":
            break

    except:
        print("BRUH")

print(f"Õige vastud = {countertrue} and vale vastud {counterfalse}.")

HindProts=round((countertrue/counterfalse) *100)
print(f"Protsent on {HindProts}%")
if HindProts < 60:
    print("Hinne 2")
elif 60 <= HindProts < 75:
    print("Hinne 3")
elif 75 <= HindProts < 90:
    print("Hinne 4")
else:
    print("Hinne 5")
