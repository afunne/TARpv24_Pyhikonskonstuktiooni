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