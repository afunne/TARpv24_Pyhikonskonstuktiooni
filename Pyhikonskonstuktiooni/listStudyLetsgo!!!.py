# len() - find how much is the leigth in the list
# isalpha - checks if input is letters
# isnumeric - checks if input is numbers

# from random import *
# sõne="Programmeerimine"
# print(sõne)
# # read by letters
# sõne_list=list(sõne)
# print(sõne_list)
# # reverses
# sõne_list.reverse()
# print(sõne_list)
# # finds input letters
# print(sõne_list.index("P"))
# # how many in a list
# print(len(sõne_list))
# # How many in a word
# print(len(sõne))
# # counts letters in m
# kogus_m=sõne_list.count("m")
# # deletes in m range letters "m"
# for m in range(kogus_m):
#     sõne_list.remove("m")
# # we are inserting numeric in the end of the list
# tähed=randint(1, 6)
# for i in range(tähed):
#     while 1:
#         try:
#             t=input("Sisesta täht: ")
#             if t.isalpha(): break
#         except:
#             print("On vaja täht!")
#     sõne_list.append(input(t))
# print(sõne_list)


# tähed=randint(1, 6)
# for i in range(tähed):
#     while 1:
#         try:
#             t=input("Sisesta täht: ")
#             if t.isalpha(): break
#         except:
#             print("On vaja täht!")
#     while 1:
#         try:
#             ind=input("Sisesta index: ")
#             if ind.isnumeric() & int(ind)<len(sõne_list): break
#         except:
#             print("On vaja index!")
#     sõne_list.insert(int(ind), t)
# print(sõne_list)
# def function(e):
#     return len(e)
# # sorts the list by the function
# sõne_list.sort(reverse=True, key=function)
# print(sõne_list)

# # work that I have to finish at home
# # just a test
# word = "andestav"
# word_list = list(word)
# print(word_list)
# # first
# word_list.title()
# print(word_list)
# # second
# word_list.capitalize()
# print(word_list)
# # third
# if word_list.isnumeric():
#     print("YAY!")
# else:
#     print("See on kõik, MA plahvatan!")
# # fourth
# word_list.capitalize()
# print(word_list)
# # fifth
# word_list.swapcase()
# print(word_list)
# # sixth
# word_list.rjust(7, fillchar="scatman")
# print(word_list)
# # seventh
# word_list.ljust(7, fillchar="scatman")
# print(word_list)
# # eight
# word_list.center(20)
# print(word_list)
# # ninth
# word_list.zfill(10)
# print(word_list)
# # tenth
# if word_list.isspace():
#     print("YAY!")
# else:
#     print("See on kõik, MA plahvatan!")


print("1. title")
print("2. capitalize")
print("3. isnumeric")
print("4. len")
print("5. swapcase")
print("6. rjust")
print("7. ljust")
print("8. center")
print("9. zfill")
print("10. isspace")
print()

try:
    question_func=int(input("Sisesta milline funktion te tahate?: "))
    if question_func > 10 & question_func <= 0:
        print("Vale! Provi uuesti")
    else:
        print("Väga hea!")
except:
    print(">:/")

while True:
            if question_func==1:
                worduser=input("Sisesta sinu sõna: ")
                print(worduser)
                worduser_list = list(worduser)
                worduser_list.title()
                print(worduser_list)
                IWANTMOOORE=input("Kas te tahate parem?: (ja või ei)")
                if IWANTMOOORE == "ja":
                    print("1. title")
                    print("2. capitalize")
                    print("3. isnumeric")
                    print("4. len")
                    print("5. swapcase")
                    print("6. rjust")
                    print("7. ljust")
                    print("8. center")
                    print("9. zfill")
                    print("10. isspace")
                    print()
                    try:
                        question_func=int(input("Sisesta milline funktion te tahate?: "))
                        if question_func > 10 & question_func <= 0:
                            print("Vale! Provi uuesti")
                        else:
                            print("Väga hea!")
                    except:
                        print(">:/")
                elif IWANTMOOORE == "ei":
                    break

            elif question_func==2:
                worduser=input("Sisesta sinu sõna: ")
                print(worduser)
                worduser_list = list(worduser)
                worduser_list.capitalize()
                print(worduser_list)
                IWANTMOOORE=input("Kas te tahate parem?: (ja või ei)")
                if IWANTMOOORE == "ja":
                    print("1. title")
                    print("2. capitalize")
                    print("3. isnumeric")
                    print("4. len")
                    print("5. swapcase")
                    print("6. rjust")
                    print("7. ljust")
                    print("8. center")
                    print("9. zfill")
                    print("10. isspace")
                    print()
                    try:
                        question_func=int(input("Sisesta milline funktion te tahate?: "))
                        if question_func > 10 & question_func <= 0:
                            print("Vale! Provi uuesti")
                        else:
                            print("Väga hea!")
                    except:
                        print(">:/")
                elif IWANTMOOORE == "ei":
                    break

            elif question_func==3:
                worduser=input("Sisesta sinu sõna (proovi kirjutamine numberidega ja numprideta): ")
                print(worduser)
                worduser_list = list(worduser)
                if worduser_list.isnumeric():
                    print("YAY!")
                else:
                    print("See on kõik, MA plahvatan!")
                print(worduser_list)
                IWANTMOOORE=input("Kas te tahate parem?: (ja või ei)")
                if IWANTMOOORE == "ja":
                    print("1. title")
                    print("2. capitalize")
                    print("3. isnumeric")
                    print("4. len")
                    print("5. swapcase")
                    print("6. rjust")
                    print("7. ljust")
                    print("8. center")
                    print("9. zfill")
                    print("10. isspace")
                    print()
                    try:
                        question_func=int(input("Sisesta milline funktion te tahate?: "))
                        if question_func > 10 & question_func <= 0:
                            print("Vale! Provi uuesti")
                        else:
                            print("Väga hea!")
                    except:
                        print(">:/")
                elif IWANTMOOORE == "ei":
                    break

            elif question_func==4:
                worduser=input("Sisesta sinu sõna: ")
                print(worduser)
                worduser_list = list(worduser)
                len(worduser_list)
                print(worduser_list)
                IWANTMOOORE=input("Kas te tahate parem?: (ja või ei)")
                if IWANTMOOORE == "ja":
                    print("1. title")
                    print("2. capitalize")
                    print("3. isnumeric")
                    print("4. len")
                    print("5. swapcase")
                    print("6. rjust")
                    print("7. ljust")
                    print("8. center")
                    print("9. zfill")
                    print("10. isspace")
                    print()
                    try:
                        question_func=int(input("Sisesta milline funktion te tahate?: "))
                        if question_func > 10 & question_func <= 0:
                            print("Vale! Provi uuesti")
                        else:
                            print("Väga hea!")
                    except:
                        print(">:/")
                elif IWANTMOOORE == "ei":
                    break

            elif question_func==5:
                worduser=input("Sisesta sinu sõna: ")
                print(worduser)
                worduser_list = list(worduser)
                worduser_list.swapcase()
                print(worduser_list)
                IWANTMOOORE=input("Kas te tahate parem?: (ja või ei)")
                if IWANTMOOORE == "ja":
                    print("1. title")
                    print("2. capitalize")
                    print("3. isnumeric")
                    print("4. len")
                    print("5. swapcase")
                    print("6. rjust")
                    print("7. ljust")
                    print("8. center")
                    print("9. zfill")
                    print("10. isspace")
                    print()
                    try:
                        question_func=int(input("Sisesta milline funktion te tahate?: "))
                        if question_func > 10 & question_func <= 0:
                            print("Vale! Provi uuesti")
                        else:
                            print("Väga hea!")
                    except:
                        print(">:/")
                elif IWANTMOOORE == "ei":
                    break
        
            elif question_func==6:
                worduser=input("Sisesta sinu sõna: ")
                print(worduser)
                worduser_list = list(worduser)
                putwhateveryouwantidc=input("Sisesta sinu fillchar: ")
                worduser_list.rjust(100, fillchar=putwhateveryouwantidc)
                print(worduser_list)
                IWANTMOOORE=input("Kas te tahate parem?: (ja või ei)")
                if IWANTMOOORE == "ja":
                    print("1. title")
                    print("2. capitalize")
                    print("3. isnumeric")
                    print("4. len")
                    print("5. swapcase")
                    print("6. rjust")
                    print("7. ljust")
                    print("8. center")
                    print("9. zfill")
                    print("10. isspace")
                    print()
                    try:
                        question_func=int(input("Sisesta milline funktion te tahate?: "))
                        if question_func > 10 & question_func <= 0:
                            print("Vale! Provi uuesti")
                        else:
                            print("Väga hea!")
                    except:
                        print(">:/")
                elif IWANTMOOORE == "ei":
                    break

            elif question_func==7:
                worduser=input("Sisesta sinu sõna: ")
                print(worduser)
                worduser_list = list(worduser)
                putwhateveryouwantidc=input("Sisesta sinu fillchar: ")
                worduser_list.ljust(100, fillchar=putwhateveryouwantidc)
                print(worduser_list)
                IWANTMOOORE=input("Kas te tahate parem?: (ja või ei)")
                if IWANTMOOORE == "ja":
                    print("1. title")
                    print("2. capitalize")
                    print("3. isnumeric")
                    print("4. len")
                    print("5. swapcase")
                    print("6. rjust")
                    print("7. ljust")
                    print("8. center")
                    print("9. zfill")
                    print("10. isspace")
                    print()
                    try:
                        question_func=int(input("Sisesta milline funktion te tahate?: "))
                        if question_func > 10 & question_func <= 0:
                            print("Vale! Provi uuesti")
                        else:
                            print("Väga hea!")
                    except:
                        print(">:/")
                elif IWANTMOOORE == "ei":
                    break
                elif IWANTMOOORE == "ei":
                    break

            elif question_func==8:
                worduser=input("Sisesta sinu sõna: ")
                print(worduser)
                worduser_list = list(worduser)
                putwhatevernumberyouwantidc=input(int("Sisesta sinu fillchar: "))
                worduser_list.center(putwhatevernumberyouwantidc)
                print(worduser_list)
                IWANTMOOORE=input("Kas te tahate parem?: (ja või ei)")
                if IWANTMOOORE == "ja":
                    print("1. title")
                    print("2. capitalize")
                    print("3. isnumeric")
                    print("4. len")
                    print("5. swapcase")
                    print("6. rjust")
                    print("7. ljust")
                    print("8. center")
                    print("9. zfill")
                    print("10. isspace")
                    print()
                    try:
                        question_func=int(input("Sisesta milline funktion te tahate?: "))
                        if question_func > 10 & question_func <= 0:
                            print("Vale! Provi uuesti")
                        else:
                            print("Väga hea!")
                    except:
                        print(">:/")
                elif IWANTMOOORE == "ei":
                    break

            elif question_func==9:
                worduser=input("Sisesta sinu sõna: ")
                print(worduser)
                worduser_list = list(worduser)
                putwhatevernumberyouwantidc=input(int("Sisesta sinu fillchar: "))
                worduser_list.zfill(putwhatevernumberyouwantidc)
                print(worduser_list)
                IWANTMOOORE=input("Kas te tahate parem?: (ja või ei)")
                if IWANTMOOORE == "ja":
                    print("1. title")
                    print("2. capitalize")
                    print("3. isnumeric")
                    print("4. len")
                    print("5. swapcase")
                    print("6. rjust")
                    print("7. ljust")
                    print("8. center")
                    print("9. zfill")
                    print("10. isspace")
                    print()
                    question_func=int(input("Sisesta milline funktion te tahate?: "))
                    if question_func > 10 & question_func <= 0:
                        print("Vale! Provi uuesti")
                elif IWANTMOOORE == "ei":
                    break

            elif question_func==10:
                worduser=input("Sisesta sinu sõna (Proovi ja sisesta tühidega ja tühideta): ")
                print(worduser)
                if worduser_list.isspace():
                    print("YAY!")
                else:
                    print("See on kõik, MA plahvatan!")
                print(worduser_list)
                IWANTMOOORE=input("Kas te tahate parem?: (ja või ei)")
                if IWANTMOOORE == "ja":
                    print("1. title")
                    print("2. capitalize")
                    print("3. isnumeric")
                    print("4. len")
                    print("5. swapcase")
                    print("6. rjust")
                    print("7. ljust")
                    print("8. center")
                    print("9. zfill")
                    print("10. isspace")
                    print()
                    try:
                        question_func=int(input("Sisesta milline funktion te tahate?: "))
                        if question_func > 10 & question_func <= 0:
                            print("Vale! Provi uuesti")
                        else:
                            print("Väga hea!")
                    except:
                        print(">:/")
                elif IWANTMOOORE == "ei":
                    break

