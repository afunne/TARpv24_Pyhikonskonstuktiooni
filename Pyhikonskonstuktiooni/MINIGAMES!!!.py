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
                if LETSGOGAMBALING not in itemlist:
                    continue
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




# Mäng mängijaga
    if tase == 1:
        print("Mängija, kas te kasutate kivi, käädrid või paber?")
        LETSGOGAMBALING=input("Kasutan... : ")
        print("Teine mängija, kas te kasutate kivi, käädrid või paber?")
        LETSGOGAMBALING2=input("Kasutan... : ")
        print(f"Te kasuate {LETSGOGAMBALING}...")
        time.sleep(3)
        itemlist = ["kivi", "käädrid", "paber"]

        if LETSGOGAMBALING or LETSGOGAMBALING2 not in itemlist:
                print("Nuh uh, proovi uueesti!")
                LETSGOGAMBALING=input("Kasutan... : ")
                LETSGOGAMBALING2=input("Kasutan... : ")
                if LETSGOGAMBALING or LETSGOGAMBALING2 not in itemlist:
                    continue
        else: 
            print("Yuh uh, tuli!")


        if LETSGOGAMBALING == LETSGOGAMBALING2:
            print("Välisid sama")
            DoYouWantToCont= int(input("Kas te tahate mängida paljum? [1-ja, 0-ei]: "))
            if DoYouWantToCont==1:
                continue
            elif DoYouWantToCont==0:
                break
        elif LETSGOGAMBALING == "kivi" and LETSGOGAMBALING2 == "paper":
            print("Robot võidab!")
            DoYouWantToCont= int(input("Kas te tahate mängida paljum? [1-ja, 0-ei]: "))
            if DoYouWantToCont==1:
                continue
            elif DoYouWantToCont==0:
                break
        elif LETSGOGAMBALING == "kivi" and LETSGOGAMBALING2 == "käädrid":
            print("Sa võidsid!")
            DoYouWantToCont= int(input("Kas te tahate mängida paljum? [1-ja, 0-ei]: "))
            if DoYouWantToCont==1:
                continue
            elif DoYouWantToCont==0:
                break
        elif LETSGOGAMBALING == "käädrid" and LETSGOGAMBALING2 == "kivi":
            print("Robot võidab!")
            DoYouWantToCont= int(input("Kas te tahate mängida paljum? [1-ja, 0-ei]: "))
            if DoYouWantToCont==1:
                continue
            elif DoYouWantToCont==0:
                break
        elif LETSGOGAMBALING == "käädrid" and LETSGOGAMBALING2 == "paber":
            print("Sa võidsid!")
            DoYouWantToCont= int(input("Kas te tahate mängida paljum? [1-ja, 0-ei]: "))
            if DoYouWantToCont==1:
                continue
            elif DoYouWantToCont==0:
                break
        elif LETSGOGAMBALING == "paber" and LETSGOGAMBALING2 == "kivi":
            print("Sa võidsid!")
            DoYouWantToCont= int(input("Kas te tahate mängida paljum? [1-ja, 0-ei]: "))
            if DoYouWantToCont==1:
                continue
            elif DoYouWantToCont==0:
                break
        elif LETSGOGAMBALING == "paber" and LETSGOGAMBALING2 == "käädrid":
            print("Robot võidab!")
            DoYouWantToCont= int(input("Kas te tahate mängida paljum? [1-ja, 0-ei]: "))
            if DoYouWantToCont==1:
                continue
            elif DoYouWantToCont==0:
                break
