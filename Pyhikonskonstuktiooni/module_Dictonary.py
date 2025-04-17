# test

# from gtts import gTTS
# from playsound import playsound

# def raagi(tekst, keel='et'):
#     obj = gTTS(text=tekst, lang=keel, slow=False)
#     failinimi = "heli.mp3"
#     obj.save(failinimi)
#     playsound(failinimi)

# Dictionary to store words (Estonian: Russian)

# tolgi_est_rus(sona)

# tolgi_rus_est(sona)

# lisa_sona()

# paranda_sona()

# testi_teadmisi()
# import random

# sonastik = {
#     'koer': 'собака',
#     'kass': 'кошка',
#     'maja': 'дом',
#     'auto': 'машина',
#     'päike': 'солнце'
# }

# def tolgi_est_rus(sona):
#     """
#     Tõlge eesti keelest vene keelde
#     """
#     word = input("Sisesta eesti keelne sõna: ").lower()
#     translation = sona.get(word, "Sõna sõnastikus puudub")
#     print(f"Tõlge: {translation}")


# def tolgi_rus_est(sona):
#     """
#     Tõlge vene keelest eesti keelde
#     """
#     word = input("Sisesta vene keelne sõna: ").lower()
#     translation = "Sõna sõnastikus puudub"
#     for est, rus in sona.items():
#         if rus == word:
#             translation = est
#             break
#     print(f"Tõlge: {translation}")

# def lisa_sona():
#     """
#     Uue sõna lisamine sõnaraamatusse
#     """
#     est_sona = input("Sisesta eesti keelne sõna: ").lower()
#     rus_sona = input("Sisesta vene tõlge: ").lower()
#     sonastik[est_sona] = rus_sona
#     print(f"Sõna '{est_sona}' lisatud sõnastikku!")

# def paranda_sona():
#     """
#     Parandada sõna sõnaraamatus
#     """
#     est_sona = input("Sisesta parandatav eesti keelne sõna: ").lower()
#     if est_sona in sonastik:
#         new_rus = input(f"Sisesta uus vene tõlge sõnale '{est_sona}': ").lower()
#         sonastik[est_sona] = new_rus
#         print("Sõna parandatud!")
#     else:
#         print("Sellist sõna sõnastikus pole.")

# def testi_teadmisi():
#     """
#     Testi kasutaja sõnavara teadmisi
#     """
#     sonastik = {
#         'koer': 'собака',
#         'kass': 'кошка',
#         'maja': 'дом',
#         'puu': 'дерево',
#         'raamat': 'книга'
#     }

#     correct = 0
#     total = 0

#     confirm = int(input("Kas te tahate testida? 1 - jah, 0 - ei: "))
#     if confirm == 1:
#         while True:
#             testlvl = int(input("\nVali testitüüp: vene - 1, eesti - 2, lõpetamiseks - 0: "))
#             if testlvl == 1:
#                 est = random.choice(list(sonastik))
#                 rus = sonastik[est]
#                 print("\nTestime eesti-vene suunal:")
#                 useranswer = input(f"Kuidas tõlgitakse '{est}' vene keelde? ").lower()
#                 total += 1
#                 if useranswer == rus:
#                     print("Õige!")
#                     correct += 1
#                 else:
#                     print(f"Vale! Õige vastus on '{rus}'")

#             elif testlvl == 2:
#                 rus = random.choice(list(sonastik.values()))
#                 # get corresponding est word
#                 est = [k for k, v in sonastik.items() if v == rus][0]
#                 print("\nTestime vene-eesti suunal:")
#                 useranswer = input(f"Kuidas tõlgitakse '{rus}' eesti keelde? ").lower()
#                 total += 1
#                 if useranswer == est:
#                     print("Õige!")
#                     correct += 1
#                 else:
#                     print(f"Vale! Õige vastus on '{est}'")

#             elif testlvl == 0:
#                 if total > 0:
#                     result = (correct / total) * 100
#                     print(f"\nTest lõppenud! Õiged vastused: {correct}, valed: {total - correct}")
#                     print(f"Protsent: {result:.2f}%")
#                 else:
#                     print("Testi ei tehtud.")
#                 break
#             else:
#                 print("Vigane sisestus, proovi uuesti.")

#     else:
#         print("Selge, järgmine kord!")

import random
import os

DICTIONARY_FILE = "sonastik.txt"

def lae_sonastik():
    """
    Laeb sõnastiku failist sõnastikku (dict)
    """
    sona = {}
    if os.path.exists(DICTIONARY_FILE):
        with open(DICTIONARY_FILE, "r", encoding="utf-8") as f:
            for line in f:
                if ':' in line:
                    est, rus = line.strip().split(":", 1)
                    sona[est.strip()] = rus.strip()
    return sona

def salvesta_sonastik(sonastik):
    """
    Salvestab sõnastiku faili
    """
    with open(DICTIONARY_FILE, "w", encoding="utf-8") as f:
        for est, rus in sonastik.items():
            f.write(f"{est}:{rus}\n")

def tolgi_est_rus(sonastik):
    word = input("Sisesta eesti keelne sõna: ").lower()
    translation = sonastik.get(word, "Sõna sõnastikus puudub")
    print(f"Tõlge: {translation}")

def tolgi_rus_est(sonastik):
    word = input("Sisesta vene keelne sõna: ").lower()
    translation = "Sõna sõnastikus puudub"
    for est, rus in sonastik.items():
        if rus == word:
            translation = est
            break
    print(f"Tõlge: {translation}")

def lisa_sona(sonastik):
    est_sona = input("Sisesta eesti keelne sõna: ").lower()
    rus_sona = input("Sisesta vene tõlge: ").lower()
    sonastik[est_sona] = rus_sona
    salvesta_sonastik(sonastik)
    print(f"Sõna '{est_sona}' lisatud sõnastikku!")

def paranda_sona(sonastik):
    est_sona = input("Sisesta parandatav eesti keelne sõna: ").lower()
    if est_sona in sonastik:
        new_rus = input(f"Sisesta uus vene tõlge sõnale '{est_sona}': ").lower()
        sonastik[est_sona] = new_rus
        salvesta_sonastik(sonastik)
        print("Sõna parandatud!")
    else:
        print("Sellist sõna sõnastikus pole.")

def testi_teadmisi(sonastik):
    correct = 0
    total = 0

    confirm = int(input("Kas te tahate testida? 1 - jah, 0 - ei: "))
    if confirm == 1:
        while True:
            testlvl = int(input("\nVali testitüüp: vene - 1, eesti - 2, lõpetamiseks - 0: "))
            if testlvl == 1:
                est = random.choice(list(sonastik))
                rus = sonastik[est]
                print("\nTestime eesti-vene suunal:")
                useranswer = input(f"Kuidas tõlgitakse '{est}' vene keelde? ").lower()
                total += 1
                if useranswer == rus:
                    print("Õige!")
                    correct += 1
                else:
                    print(f"Vale! Õige vastus on '{rus}'")

            elif testlvl == 2:
                rus = random.choice(list(sonastik.values()))
                est = [k for k, v in sonastik.items() if v == rus][0]
                print("\nTestime vene-eesti suunal:")
                useranswer = input(f"Kuidas tõlgitakse '{rus}' eesti keelde? ").lower()
                total += 1
                if useranswer == est:
                    print("Õige!")
                    correct += 1
                else:
                    print(f"Vale! Õige vastus on '{est}'")

            elif testlvl == 0:
                if total > 0:
                    result = (correct / total) * 100
                    print(f"\nTest lõppenud! Õiged vastused: {correct}, valed: {total - correct}")
                    print(f"Protsent: {result:.1f}%")
                else:
                    print("Testi ei tehtud.")
                break
            else:
                print("Vigane sisestus, proovi uuesti.")
    else:
        print("Selge, järgmine kord!")
