import statistics

p=[]
i=[]
def Lisa_andmed(p:list, i:list):
    """
    Lisada mitu inimest ja nende palgad
    """
    while True:
        try:
            nimi=input("Sisesta töötaja nimi: ")
            if nimi.isalpha():
                try:
                    dola=float(input("Sisesta tema palk: "))
                except:
                    print("Hell nah, what did the bro write?")

        except:
            print("Hell nah, what did the bro write?")
    p.append(dola)
    i.append(nimi)

def Kutsuta_andmed(p:list, i:list):
    """
    Isiku ja tema palga kustutada(nimi sisestab kasutaja)
    """
    while True:
        try:
            nimi=input("Sisesta töötaja nimi: ")
            if nimi.isalpha():
                k=i.count(nimi)
                if k>0:
                    for i in range (k):
                        ind=i.index(nimi)
                        i.pop=(ind)
                        p.pop=(ind)
                    print(f"Andmed: {nimi} on kustutatud")
                    break
                else:
                    print("Nuh uh. it doesnt exist. KYS")
                    continue
        except:
            print("Bruh. try again idk idc")
            continue

def Suurim_palk(p:list, i:list):
    """
    Näita kõige suurim palk listist
    """
    max_p = max(p)
    max_i = []

    for nimi, palk in zip(i, p):
        if palk == max_p:
            max_i.append(nimi)
    # min_i = [i for i, pop in zip(i, p) if pop == min_p]

    print("\nAndme:")
    print(f"Maksimaalne palk: {max_p} ({', '.join(max_i)})")
    # print(f"Minimaalne elanikkond: {min_p} ({', '.join(min_i)})")

    # suurim=max(p)
    # print(f"Suurim palk on {suurim}")
    # k=p.index(suurim)
    # for i in range (k):
    #     ind=p.index(suurim,ind)
    #     print(f"Saab kätte {i[ind]}")
    #     ind+=1

def sorteerimine(p:list, i:list):
    """
    Järjestada palgad kasvavas ja kahanevas järjekorras koos nimedega
    """
    v=input("Vali märk: > (kasvav) või < (kahanev): ")
    for n in range(0,len(i)):
        for m in range(n,len(i)):
            if eval(str(p[n])+v+str(p[m])):
                p[n],p[m]=p[m],p[n]
                i[n],i[m]=i[m],i[n]
    print(p)
    print(i)

def Võrdsed_palgad(p:list,i:list):
    """
    Teada saada, kes saavad võrdset palka, leida, kui palju neid on ja kuvada nende andmed ekraanile
    """
    hulk=set(p)
    print(hulk)
    for palk in hulk:
        k=p.count(palk)
        if k>1:
            print(f"Palk {palk}")
            ind=p.index(palk)
            for j in range(k):
                ind=p.index(palk,ind)
                print(f"Saab kätte {i[ind]}")
                ind+=1

def Keskel_palk(p:list,i:list):
    """
    Näita keskel palk
    """
    med_p = statistics.median(p)

    print("\nAndme:")
    print(f"Keskel palk: {med_p})")

    question=int(input("Yada, yada 1 - ja, 0 - ei: "))

    if question == 1:
        for x in range(len(p)):
            if p[x] < med_p:
                p.pop(x)
                i.pop(x)
        print("Andmed on kustutatud")
        print(f"\n{i}\n{p}")
    elif question == 0:
        pass

def Väiksem_palk(p:list, i:list):
    """
    Näita kõige minimaalsem palk
    """
    min_p = min(p)
    min_i = []

    for nimi, palk in zip(i, p):
        if palk == min_p:
            min_i.append(nimi)

    print("\nAndme:")
    print(f"Minimaalne palk: {min_p} ({', '.join(min_i)})")


def otsima_palkjanimi(p:list, i:list):
    """
    Otsib palga(d) nime järgi. Arvestab, et nimi võib esineda mitu korda
    """
    while True:
        sisse_nimi = input("Sisesta töötaja nimi: ")
        if not sisse_nimi or sisse_nimi not in i:
            print("Sellist nime ei leitud.")
            continue
        else:
            seotud_palgad = []
            for nimi, palk in zip(i, p):
                if nimi == sisse_nimi:
                    seotud_palgad.append(palk)
                    break


def tulevane_palk(p: list, i: list):
    """
    Tulevik palk
    """
    while True:
        nimi = input("Sisesta töötaja nimi: ")
        try:
            T = int(input("Mitu aastat edasi vaadata: "))
        except:
            print("Palun sisesta korrektne arv.")
            continue

        if nimi not in i:
            print("Sellist nime ei leitud.")
            continue

        print(f"\n{nimi} praegused palgad ja tulevased palgad {T} aasta pärast (+5% aastas):")
        for nim, palk in zip(i, p):
            if nim == nimi:
                tulev_palk = round(palk * (0.05 ** T), 2)
                print(f"Palk {palk} -> {tulev_palk} eurot")
                break
        # max_p = max(p)
        # max_i = [i for i, pop in zip(i, p) if pop == max_p]


    # hewo_p = p
    # hewo_i = [i for i, pop in zip(i, p) if pop == hewo_p]

    # print("\nAndme:")
    # print(f"Minimaalne palk: {hewo_p} ({', '.join(hewo_i)})")    