import re
from random import *
# def registreerimine(username:str,paroolXD:str,tehe:int)->any:
#     """
#     See funktsion teeb või küsis kasutajanimist ja parolist
#     """
#     while True:
#         if tehe in [1, 2]:
#             pass
#         else:
#             print("*insert cat exploding gif*")
#         if username is None:
#             print("Nuh uh")
#             continue
#         else: pass

#         if username.isalpha:
#             pass
#         else:
#             print("Nuh uh")
#             continue

#         if username.isdigit:
#             pass
#         else:
#             print("Nuh uh")
#             continue
#         regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')  
#         if(regex.search(registreerimine) == None):
#             break
#         else:
#             print("Nuh uh")
#             continue
#     return username, paroolXD, tehe

def registreerimine(tehe:int, username:str, password:str) ->any:
    """
    See funktsion teeb või küsis kasutajanimist ja parolist
    """
    while True:
        username = input("Sisesta sinu kasutajanimi: ")
        if username == None:
            print("Nuh uh")
            continue
        else: pass

        tehe= int(input("Kas te tahate looda sinu parol iseseisvalt või AI-ga [1, 2]: "))
        if tehe ==1:
            password = input("Sisesta sinu parool: ")
            if password == None:
                print("Nuh uh")
                continue
            elif password.isalpha:
                pass
            elif password.isdigit:
                pass
            regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
            if (regex.search(password) == None):
                continue
            else:
                print("Yuh uh")
                break
        elif tehe==2:
            i=input("Sisesta täht => ")
            if(i.isupper()):
                print("See on suur täht", i)
            a=input("Sisesta arv => ")
            if (a.isdigit()):
                print("See on täisarv ", a)
        else:
            print("XD")
            continue
    return tehe, username, password
