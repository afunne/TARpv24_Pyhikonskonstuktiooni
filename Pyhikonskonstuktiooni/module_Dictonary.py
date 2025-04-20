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

# import random
# import os

# # Single file for vocabulary storage
# VOCAB_FILE = "vocabulary.txt"

# def read_vocabulary() -> dict:
#     """Read vocabulary from file into dictionary (Estonian-Russian)"""
#     vocabulary = {}
#     try:
#         with open(VOCAB_FILE, 'r', encoding='utf-8-sig') as f:
#             for line in f:
#                 if '-' in line:
#                     est, rus = line.strip().split('-')
#                     vocabulary[est] = rus
#     except FileNotFoundError:
#         print("Vocabulary file not found. Creating new one.")
#         with open(VOCAB_FILE, 'w', encoding='utf-8-sig') as f:
#             pass
#     return vocabulary

# def write_vocabulary(vocabulary: dict):
#     """Write dictionary to vocabulary file"""
#     with open(VOCAB_FILE, 'w', encoding='utf-8-sig') as f:
#         for est, rus in vocabulary.items():
#             f.write(f"{est}-{rus}\n")

# def translate_est_to_rus():
#     """Translate from Estonian to Russian"""
#     vocabulary = read_vocabulary()
#     word = input("Sisesta eesti keelne sõna: ").lower()
#     translation = vocabulary.get(word, "Sõna sõnastikus puudub")
#     print(f"Tõlge: {translation}")

# def translate_rus_to_est():
#     """Translate from Russian to Estonian"""
#     vocabulary = read_vocabulary()
#     word = input("Sisesta vene keelne sõna: ").lower()
#     # Create reverse dictionary for lookup
#     rus_est = {rus: est for est, rus in vocabulary.items()}
#     translation = rus_est.get(word, "Sõna sõnastikus puudub")
#     print(f"Tõlge: {translation}")

# def add_word():
#     """Add new word to vocabulary"""
#     est_word = input("Sisesta eesti keelne sõna: ").lower()
#     rus_word = input("Sisesta vene tõlge: ").lower()
    
#     vocabulary = read_vocabulary()
#     vocabulary[est_word] = rus_word
#     write_vocabulary(vocabulary)
    
#     print(f"Sõna '{est_word}' lisatud sõnastikku!")

# def correct_word():
#     """Correct existing word in vocabulary"""
#     vocabulary = read_vocabulary()
#     est_word = input("Sisesta parandatav eesti keelne sõna: ").lower()
    
#     if est_word in vocabulary:
#         new_rus = input(f"Sisesta uus vene tõlge sõnale '{est_word}': ").lower()
#         vocabulary[est_word] = new_rus
#         write_vocabulary(vocabulary)
#         print("Sõna parandatud!")
#     else:
#         print("Sellist sõna sõnastikus pole.")

# def test_knowledge():
#     """Test user's vocabulary knowledge"""
#     vocabulary = read_vocabulary()
#     if not vocabulary:
#         print("Sõnastik on tühi. Palun lisa esmalt sõnu.")
#         return
    
#     correct = 0
#     total = 0
    
#     confirm = input("Kas te tahate testida? (jah/ei): ").lower()
#     if confirm == 'jah':
#         while True:
#             test_type = input("\nVali testitüüp: vene - 1, eesti - 2, lõpetamiseks - 0: ")
            
#             if test_type == '1':
#                 # Test Estonian to Russian
#                 est_word = random.choice(list(vocabulary.keys()))
#                 correct_translation = vocabulary[est_word]
#                 user_answer = input(f"Kuidas tõlgitakse '{est_word}' vene keelde? ").lower()
#                 total += 1
#                 if user_answer == correct_translation:
#                     print("Õige!")
#                     correct += 1
#                 else:
#                     print(f"Vale! Õige vastus on '{correct_translation}'")
            
#             elif test_type == '2':
#                 # Test Russian to Estonian
#                 rus_word = random.choice(list(vocabulary.values()))
#                 # Find corresponding Estonian word
#                 est_word = None
#                 for est, rus in vocabulary.items():
#                     if rus == rus_word:
#                         est_word = est
#                         break
    
#                 if est_word is None:
#                     print("lol")
#                     continue
#                 user_answer = input(f"Kuidas tõlgitakse '{rus_word}' eesti keelde? ").lower()
#                 total += 1
#                 if user_answer == est_word:
#                     print("Õige!")
#                     correct += 1
#                 else:
#                     print(f"Vale! Õige vastus on '{est_word}'")
            
#             elif test_type == '0':
#                 if total > 0:
#                     percentage = (correct / total) * 100
#                     print(f"\nTest lõppenud! Õiged vastused: {correct}, valed: {total - correct}")
#                     print(f"Protsent: {percentage:.2f}%")
#                 else:
#                     print("Testi ei tehtud.")
#                 break
#             else:
#                 print("Vigane sisestus, proovi uuesti.")
#     else:
#         print("Selge, järgmine kord!")

# def display_vocabulary():
#     """Show all words in vocabulary"""
#     vocabulary = read_vocabulary()
#     if not vocabulary:
#         print("Sõnastik on tühi.")
#         return
    
#     # for debuging purposes
#     print("\n=== SÕNASTIK ===")
#     for i, (est, rus) in enumerate(vocabulary.items(), 1):
#         print(f"{i}. {est} - {rus}")


import random

def Loe_failist(fail:str)->list:
    """
    Faili lugemine ridade loeteluks
    """
    try:
        with open(fail, 'r', encoding="utf-8-sig") as f:
            return [rida.strip() for rida in f]
    except FileNotFoundError:
        print(f"Faili {fail} ei leitud!")
        return

def tolgi_est_rus():
    """
    Tõlge eesti keelest vene keelde tekstifailist
    """
    sonad = Loe_failist("sonastik.txt")
    if not sonad:
        print("Sõnastik on tühi!")
        return
    
    otsitav = input("Sisesta eesti keelne sõna: ").lower()
    leitud = False
    
    for paar in sonad:
        if '-' in paar:
            est, rus = paar.split('-')
            if est == otsitav:
                print(f"Tõlge: {rus}")
                leitud = True
                break
    
    if not leitud:
        print("Sõna ei leitud sõnastikust!")

def tolgi_rus_est():
    """
    Tõlge vene keelest eesti keelde tekstifailist
    """
    sonad = Loe_failist("sonastik.txt")
    if not sonad:
        print("Sõnastik on tühi!")
        return
    
    otsitav = input("Sisesta vene keelne sõna: ").lower()
    leitud = False
    
    for paar in sonad:
        if '-' in paar:
            est, rus = paar.split('-')
            if rus == otsitav:
                print(f"Tõlge: {est}")
                leitud = True
                break
    
    if not leitud:
        print("Sõna ei leitud sõnastikust!")

def Kirjuta_failisse(fail:str, jarjend:list):
    """
    Nimekirja kirjutamine faili
    """
    with open(fail, 'w', encoding="utf-8-sig") as f:
        f.write('\n'.join(jarjend))

def kuva_sonastik():
    """
    Kuvada kõik sõnad sõnavaras
    """
    sonad = Loe_failist("sonastik.txt")
    if not sonad:
        print("Sõnastik on tühi!")
    else:
        print("\nSõnastik:")
        for i, paar in enumerate(sonad, 1):
            print(f"{i}. {paar.replace('-', ' - ')}")

def lisa_sona():
    """
    Lisa uus sõnapaar
    """
    est = input("Eesti sõna: ").lower()
    rus = input("Vene tõlge: ").lower()
    sonad = Loe_failist("sonastik.txt")
    sonad.append(f"{est}-{rus}")
    Kirjuta_failisse("sonastik.txt", sonad)
    print(f"'{est}' lisatud!")

def paranda_sona():
    """
    Olemasoleva sõna muutmine
    """
    sonad = Loe_failist("sonastik.txt")
    kuva_sonastik()
    try:
        nr = int(input("Mitmes sõna parandada? ")) - 1
        if 0 <= nr < len(sonad):
            est, rus = sonad[nr].split('-')
            uus_rus = input(f"Uus tõlge sõnale '{est}': ")
            sonad[nr] = f"{est}-{uus_rus}"
            Kirjuta_failisse("sonastik.txt", sonad)
            print("Parandatud!")
        else:
            print("Vale number!")
    except:
        print("Viga!")

def testi_teadmisi():
    """
    Sõnavara test
    """
    sonad = Loe_failist("sonastik.txt")
    if not sonad:
        print("Sõnastik on tühi!")
        return
    
    õiged = 0
    küsimused = 0
    
    while True:
        suund = input("\nTesti suund (1-est>rus, 2-rus>est, 0-katkesta): ")
        
        if suund == '1':
            paar = random.choice(sonad)
            est, rus = paar.split('-')
            vastus = input(f"Kuidas tõlgitakse '{est}'? ").lower()
            if vastus == rus:
                print("Õige!")
                õiged += 1
            else:
                print(f"Vale! Õige: {rus}")
            küsimused += 1
            
        elif suund == '2':
            paar = random.choice(sonad)
            est, rus = paar.split('-')
            vastus = input(f"Kuidas tõlgitakse '{rus}'? ").lower()
            if vastus == est:
                print("Õige!")
                õiged += 1
            else:
                print(f"Vale! Õige: {est}")
            küsimused += 1
            
        elif suund == '0':
            if küsimused > 0:
                print(f"\nTulemus: {õiged}/{küsimused} ({(õiged/küsimused)*100:.1f}%)")
            break
        
        else:
            print("Vale valik!")