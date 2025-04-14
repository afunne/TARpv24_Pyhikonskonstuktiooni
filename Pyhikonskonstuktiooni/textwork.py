# def Loe_failist(fail:str)->list:
#     f=open(fail,'r',encoding="utf-8-sig")
#     jarjend=[]
#     for rida in f:
#         jarjend.append(rida.strip())
#     f.close()
#     return jarjend

# list_=Loe_failist("TextFilework.txt")
# for x in list_:
#     print(x)

# def Kirjuta_failisse(fail:str,jarjend:list):
#     f=open(fail,'w',encoding="utf-8-sig")
#     for line in jarjend:
#         f.write(line+'\n')
#     f.close()

# list_=Loe_failist("TextFilework.txt")
# for x in list_:
#     print(x)

# list_=["Ann", "Kati", "Mari"]
# Kirjuta_failisse("TextFilework.txt", list_)
# list_2=Loe_failist("TextFilework.txt")
# print(list_2)

# with open("TextFilework.txt","r",encoding="utf-8-sig") as f:
#     print(f.read())

from random import *
def failis_to_dict(f:str):
    riik_pealinn={}
    pealinn_riik={}
    riigid=[]
    file=open(f,'r',encoding="utf-8-sig")
    for line in file:
        k,v=line.strip().split('-')
        riik_pealinn[k]=v
        pealinn_riik[v]=k
        riigid.append(k)
    file.close()
    return riik_pealinn, pealinn_riik, riigid

riik_pealinn, pealinn_riik, riigid = failis_to_dict
("TextFilework.txt")

