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
    """
    max_p = max(p)
    # min_p = min(p)

    max_i = [i for i, pop in zip(i, p) if pop == max_p]
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
    med_p = statistics.median(p)

    print("\nAndme:")
    print(f"Keskel palk: {med_p})")

    question=int(input("Yada, yada 1 - ja, 0 - ei: "))

    if question == 1:
        # median_DEL= p < med_p # len(complete[0]) < 30
        k=i.count(i)
        for i in k:
            if i < med_p:
                ind=i.index(k)
                i.pop=(ind)
                p.pop=(ind)
                print(f"Andmed on kustutatud")
                print(f"/n {i} /n {p}")
    elif question == 0:
        pass

def Väiksem_palk(p:list, i:list):
    """
    """
    min_p = min(p)
    min_i = [i for i, pop in zip(i, p) if pop == min_p]

    print("\nAndme:")
    print(f"Minimaalne palk: {min_p} ({', '.join(min_i)})")




