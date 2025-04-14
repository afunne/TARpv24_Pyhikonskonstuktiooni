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
import random

sonastik = {
    'koer': 'собака',
    'kass': 'кошка',
    'maja': 'дом',
    'auto': 'машина',
    'päike': 'солнце'
}

def tolgi_est_rus(sona):
    """
    Tõlge eesti keelest vene keelde
    """
    word = input("Sisesta eesti keelne sõna: ").lower()
    translation = sona.get(word, "Sõna sõnastikus puudub")
    print(f"Tõlge: {translation}")


def tolgi_rus_est(sona):
    """
    Tõlge vene keelest eesti keelde
    """
    word = input("Sisesta vene keelne sõna: ").lower()
    translation = "Sõna sõnastikus puudub"
    for est, rus in sona.items():
        if rus == word:
            translation = est
            break
    print(f"Tõlge: {translation}")

def lisa_sona():
    """
    Uue sõna lisamine sõnaraamatusse
    """
    est_sona = input("Sisesta eesti keelne sõna: ").lower()
    rus_sona = input("Sisesta vene tõlge: ").lower()
    sonastik[est_sona] = rus_sona
    print(f"Sõna '{est_sona}' lisatud sõnastikku!")

def paranda_sona():
    """
    Parandada sõna sõnaraamatus
    """
    est_sona = input("Sisesta parandatav eesti keelne sõna: ").lower()
    if est_sona in sonastik:
        new_rus = input(f"Sisesta uus vene tõlge sõnale '{est_sona}': ").lower()
        sonastik[est_sona] = new_rus
        print("Sõna parandatud!")
    else:
        print("Sellist sõna sõnastikus pole.")

def testi_teadmisi():
    """
    Testi kasutaja sõnavara teadmisi
    """
    correct = 0
    total = 0
    confirm=int(input("Kas te tahate? 1 - ja, 0 - ei: "))
    if confirm == 1:
        while True:
            testlvl= int(input("vene - 1, eesti - 2, mitte midagi - 0 "))
            if testlvl == 1:
                est = random.choice(list(sonastik))
                print("\nTestime eesti-vene suunal:")
                print(f"{est} translation...")
                useranswer=input('')
                    # import random
                    # d = {sonastik}
                    # # est = random.choice(list(d.values()))
                    # # answer = input(f"Kuidas tõlgitakse '{est}' vene keelde? ").lower()
                if useranswer == rus:
                    print("Õige!")
                    correct += 1
                else:
                    print(f"Vale! Õige vastus on '{rus}'")
                    total += 1

            elif testlvl == 2:
                print("\nTestime vene-eesti suunal:")
                for est, rus in sonastik.items():
                    answer = input(f"Kuidas tõlgitakse '{rus}' eesti keelde? ").lower()
                    if answer == est:
                        print("Õige!")
                        correct += 1
                    else:
                        print(f"Vale! Õige vastus on '{est}'")
                        total += 1
            elif testlvl == 0:
                if total > 0:
                    result = (correct / total) * 100
                    print(f"\nTest läbitud! Õigete vastuste protsent: {result:.2f}%")
            else:
                print(f"\nSinu result: õiged {correct} ja valed {total}, hea töö!")
                break

    elif confirm == 0:
        print("alr")
    else:
        print(":|")