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

sonastik={}

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
    
    print("\nTestime eesti-vene suunal:")
    for est, rus in sonastik.items():
        answer = input(f"Kuidas tõlgitakse '{est}' vene keelde? ").lower()
        if answer == rus:
            print("Õige!")
            correct += 1
        else:
            print(f"Vale! Õige vastus on '{rus}'")
        total += 1
    
    print("\nTestime vene-eesti suunal:")
    for est, rus in sonastik.items():
        answer = input(f"Kuidas tõlgitakse '{rus}' eesti keelde? ").lower()
        if answer == est:
            print("Õige!")
            correct += 1
        else:
            print(f"Vale! Õige vastus on '{est}'")
        total += 1


    result = (correct / total) * 100
    if total > 0:
        print(f"\nTest läbitud! Õigete vastuste protsent: {result:.2f}%")
    else:
        print("Sõnastik on tühi, ei saa testida.")

