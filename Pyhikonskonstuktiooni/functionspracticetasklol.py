from symbol import parameters
from telnetlib import EC
from MODULEfunctionspracticetasklol import *
while True:
    nick=input("Panna sinu kasutajanimi: ")
    if nick is None: #Mr.Maksim näitab mind
        print("Nuh uh")
        continue
    par=input("Panna sinu parool: ")
    teh = int(input("1 - random parool generator GO! / 2 - sa, tuli... GO"))
