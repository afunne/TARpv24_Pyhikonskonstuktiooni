from MODULEfunctionspracticetasklol import *

# # 1
# while True:
#     print("Mis võimalik te tahate tegi?")
#     print("""
#     teil on võilikud:
#     1 - registreerimine
#     2 - autoriseerimine
#     3 - nime või parooli muutmine
#     4 - unustanud parooli taastamine
#     """)

#     try:
#         choice = int(input("valida number: "))
#     except:
#         print("nuh uh")
#         continue


#     # it is just faster that way

#     # wantdola = int(input("Kas te tahate jätkata? 1-ja  0-ei"))
#     # if wantdola == 1:
#     #     continue
#     # elif wantdola == 0:
#     #     lõpetamine()
#     #     break

#     if choice < 0 or choice > 5:
#         print("HUH??? n/ nuh uh n/ Praegu, vali õige võimalikud!")
#         continue

#     if choice == 1:
#         tehe, username, password = registreerimine()
#         print(f"Kasutajanimi: {username}, Parool: {password}")

#         wantdola = int(input("Kas te tahate jätkata? 1-ja  0-ei"))
#         if wantdola == 1:
#             continue
#         elif wantdola == 0:
#             lõpetamine()
#             break
        

#     # 2
#     # https://www.w3schools.com/python/python_dictionaries.asp
#     # usersstore = {username: password}

#     # print("\n Tere Tulemast! Loggi sisse")
#     # checking = autoriseerimine(usersstore)

#     # if checking:
#     #     print("Tere tulemast!")
#     # else:
#     #     print("Proovi uuesti.")


#     elif choice == 2:
#         try:
#             user = [(username, password)]
#             autoriseerimine(user)

#             wantdola = int(input("Kas te tahate jätkata? 1-ja  0-ei"))
#             if wantdola == 1:
#                 continue
#             elif wantdola == 0:
#                 lõpetamine()
#                 break
#         except:
#             print("Teil pole kasutajanimi")
#             continue

#     # 3
#     # old info
#     elif choice == 3:
#         try:
#             user = [(username, password)]
#             user = muuda_kasutajat(user)
#             print(user) 

#             print("Uuendatud kasutajad:", user)

#             wantdola = int(input("Kas te tahate jätkata? 1-ja  0-ei"))
#             if wantdola == 1:
#                 continue
#             elif wantdola == 0:
#                 lõpetamine()
#                 break
#         except:
#             print("Teil pole kasutajanimi")
#             continue

#     # 4
#     # usersstore = {username: password}
#     # usersstore = unu_par_tast(usersstore)
#     # print("Uus kasutaja:", usersstore)
#     elif choice == 4:
#         try:
#             user = [(username, password)]
#             user = unu_par_tast(user)
#             print(user)

#             wantdola = int(input("Kas te tahate jätkata? 1-ja  0-ei"))
#             if wantdola == 1:
#                 continue
#             elif wantdola == 0:
#                 lõpetamine()
#                 break
#         except:
#             print("Teil pole kasutajanimi")
#             continue

#     # 5
#     # elif choice == 0:
#     #     lõpetamine()

#     # is it ironic that 5 is almost everywhere?

users_list = []

while True:
    print("\nVali tegevus:")
    print("1 - registreerimine")
    print("2 - autoriseerimine")
    print("3 - nime või parooli muutmine")
    print("4 - unustanud parooli taastamine")
    print("0 - lõpetamine")

    try:
        choice = int(input("Sisesta valik: "))
    except:
        print("Palun sisesta number!")
        continue

    if choice == 1:
        tehe, username, password = registreerimine()
        users_list.append((username, password))
        print("Registreerimine õnnestus!")
        
    elif choice == 2:
        if not users_list:
            print("Pole ühtegi registreeritud kasutajat!")
            continue
        autoriseerimine(users_list)
        
    elif choice == 3:
        if not users_list:
            print("Pole ühtegi registreeritud kasutajat!")
            continue
        users_list = muuda_kasutajat(users_list)
        
    elif choice == 4:
        if not users_list:
            print("Pole ühtegi registreeritud kasutajat!")
            continue
        users_list = unu_par_tast(users_list)
        
    elif choice == 0:
        lõpetamine()
    else:
        print("Vale valik! Proovi uuesti.")


