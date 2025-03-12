import random
import time

#at home I will finish this
print("Tere tulemast! See mäng on... kivi, käärid, paber. Te teate mida te peate tegema.")
print()

# Mäng robotiga
while True:
    tase=int(input("Kas te tahate mängida roboti või mängijaga? [0-robot, 1-mängija]: "))
    print("Mängija, kas te kasutate kivi, käädrid või paber?")
    if tase == 0:
        LETSGOGAMBALING=input("Kasutan... : ")
        print(f"Te kasuate {LETSGOGAMBALING}...")
        time.sleep(3)
        itemlist = ["kivi", "käädrid", "paber"]
        cmonworkpls = random.choice(itemlist)

        if LETSGOGAMBALING not in itemlist:
                print("Nuh uh, proovi uueesti!")
                LETSGOGAMBALING=input("Kasutan... : ")
        else: 
            print("Yuh uh, tuli!")

        print(f"Robot kasutab {cmonworkpls}...")
        if LETSGOGAMBALING == cmonworkpls:
            print("Välisid sama")
            DoYouWantToCont= int(input("Kas te tahate mängida paljum? [1-ja, 0-ei]: "))
            if DoYouWantToCont==1:
                continue
            elif DoYouWantToCont==0:
                break
        elif LETSGOGAMBALING == "kivi" and cmonworkpls == "paper":
            print("Robot võidab!")
            DoYouWantToCont= int(input("Kas te tahate mängida paljum? [1-ja, 0-ei]: "))
            if DoYouWantToCont==1:
                continue
            elif DoYouWantToCont==0:
                break
        elif LETSGOGAMBALING == "kivi" and cmonworkpls == "käädrid":
            print("Sa võidsid!")
            DoYouWantToCont= int(input("Kas te tahate mängida paljum? [1-ja, 0-ei]: "))
            if DoYouWantToCont==1:
                continue
            elif DoYouWantToCont==0:
                break
        elif LETSGOGAMBALING == "käädrid" and cmonworkpls == "kivi":
            print("Robot võidab!")
            DoYouWantToCont= int(input("Kas te tahate mängida paljum? [1-ja, 0-ei]: "))
            if DoYouWantToCont==1:
                continue
            elif DoYouWantToCont==0:
                break
        elif LETSGOGAMBALING == "käädrid" and cmonworkpls == "paber":
            print("Sa võidsid!")
            DoYouWantToCont= int(input("Kas te tahate mängida paljum? [1-ja, 0-ei]: "))
            if DoYouWantToCont==1:
                continue
            elif DoYouWantToCont==0:
                break
        elif LETSGOGAMBALING == "paber" and cmonworkpls == "kivi":
            print("Sa võidsid!")
            DoYouWantToCont= int(input("Kas te tahate mängida paljum? [1-ja, 0-ei]: "))
            if DoYouWantToCont==1:
                continue
            elif DoYouWantToCont==0:
                break
        elif LETSGOGAMBALING == "paber" and cmonworkpls == "käädrid":
            print("Robot võidab!")
            DoYouWantToCont= int(input("Kas te tahate mängida paljum? [1-ja, 0-ei]: "))
            if DoYouWantToCont==1:
                continue
            elif DoYouWantToCont==0:
                break
