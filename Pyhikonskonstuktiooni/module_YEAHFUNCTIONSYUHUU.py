from datetime import datetime


def arithmetic(arv1:float,arv2:float,tehe:str)->any:
    """Lihtne kalkulaator
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    :param float arv1: Sisend kasutajalt, minge ujukomaarv
    :param float arv1: Sisend kasutajalt, minge ujukomaarv
    :param str tehe: aritmeetiline tehe, mis valib kasutaja
    :rtype: var Määrata tüüp(float või str)
    """
    if tehe in ["+", "-", "*", "/"]:
        if arv2==0 and tehe=="/":
            vastus="DIV/0"
        else:
            vastus=eval(str(arv1+ tehe +str(arv2)))
    else:
        vastus="Tundmatu tehe"
    return vastus

def is_year_leap(aasta:int)->bool:
    """Liigaasta leidmine
    Tagastab True, kui liigaasra ja False kui on tavaline aasta
    :param int aasta: aasta number
    :rtype: bool tagastab tõecäärsuses formaadis tulemus
    """
    if aasta%4==0:
        v=True
    else:
        v=False
    return v

def square_list(külg:float)->list:
    """WELCOME TO THE UNDERGROUND!
    Panna midagi ja vaata mis juhtub!
    """
    S=külg**2
    P=külg*4
    d=(2)**(1/2)*külg
    s_list=[S,P,d]
    return s_list

def season(kuu:int)->str:
    """Panna midage te tahate siis, ma pole märatsa
    I gotta finish it at home nvm tbh
    """
    if kuu in [12,1,2]:
        return "talv"
    elif kuu in [3,4,5]:
        return "Kevadine"
    elif kuu in [6,7,8]:
        return "Suvi"
    elif kuu in [9,10,11]:
        return "sügis"
    else:
        return kuu

# (4) 2
def season(kuu:int)->str:
    """Panna midage te tahate siis, ma pole märatsa
    I gotta finish it at home nvm tbh
    """
    while True:
        if kuu in range(1, 13):
            break
        else:
            kuu = season(int(input("Panna number ya näita mis astaaeg see on: ")))
    return season(kuu)

# 5
def bank(aeur:float, years:int)->float:
    for i in range(years):
        aeur = aeur * 1.10
        return round (aeur, 2)

# def is_prime(arg:float)->bool:
#     areyouprime=arg/arg
#     areyouprimeas=arg%1
#     if areyouprime == 1 and areyouprimeas==0:
#         v="True"
#     else:
#         v="False"
#         return v

# 6
def is_prime(arg:int)->bool:
    if 0 <= arg < 1001:
        for i in range(2,arg):
            if arg % i == 0:
                return False
            else:
                return True
    else:
        if arg in [0,1]:
            pass

# 7 TS helped me a little bit here
def is_valid_date(day, month, year):
    try:
        datetime(year=year, month=month, day=day)
        return True
    except:
        return False

# 8 
# https://stackoverflow.com/questions/20557999/xor-python-text-encryption-decryption
# okay look ik I am maybe little lazy on this one but where the hell do you think I would get an exsample of this?
# okay after 50 tries it works
def XOR_cipher(text, key):
    encrypted_text = ""
    for char in text:
        encrypted_text += chr(ord(char) ^ key) # this part was suggested by TS
    return encrypted_text

def XOR_uncipher(encrypted_text, key):
    return XOR_cipher(encrypted_text, key)


