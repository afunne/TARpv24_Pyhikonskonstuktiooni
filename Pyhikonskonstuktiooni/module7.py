# for i in range(10):
#     print(i, end=", ")
# print()
# for i in range(2, 12):
#     print(i, end="; ")
# print()
# for i in range(2, 12, 3):
#     print(i, end=" ")
# print()
# for i in range(12, 2, -2):
#     print(i, end=" ")
# print()

# # exsample
# for i in range(5):
#     if i == 3:
#         break
# #     print(i)


# It's time for tasks yo
täisarvud=0
for i in range(15):
        while True:
            try:
                arv = float(input(f"Palun, panna {i+1} arv: "))
                break
            except:
                print("*insert mad goku gif here*")
    # Check if they are full, now!
        if arv == int(arv):
            täisarvud+=1
        print(f"täisarvude kogus: {täisarvud}")

# ülisane 2
summa=0
while True:
    try:
        A=int(input("Sisesata A:"))
        if A>1:
            for i in range(1,A+1):
                summa+=i
            print(f"Arvude summa vahemikus 1 kuni {A}: {summa}")
            break
        else:
            print("Arv A peabe olla rohkem kui 1")
    except:
        print("Vale fromaat")

# ülasane 3
count=0
while True:
    try:
        for i in range(0,8):
            print(i)
        num = float(input(f"Palun, panna {i+1} arv: "))
        if num>0:
            count+=num
            print(f"Summa võrdub {count}-ga")
            break
        else:
            print("balls")
    except:
        print("Vale fromaat")

# ülisane 4
for i in range(10,20):
    print(i)

# ülasane 5
while True:
    try:
        N=int(input("Sisesata N:"))
        if N>1:
            for i in range(1,N+1):
                arv=float(input(f"Sisesta {i}. arv"))
                if arv<0:
                    summa+=arv
            print(f"Summa võrdub {summa}-ga")
            break
        else:
            print("Arv N peab olema rohkem kui 1")
    except:
        print("Vale formaat")

# ülisane 6
# N=float(input("Panna N: "))
# if N<0:

N = int(input("Panna number: "))
negative_count = 0
positive_count = 0
zero_count = 0

while True:
    try:
        N = int(input("Panna number: "))
        negative_count = 0
        positive_count = 0
        zero_count = 0
        for i in range(1,N+1):
            arv=float(input(f"Sisesta {i}. arv"))
            if arv < 0:
               negative_count += 1
               print(f"Negativne: {negative_count}")
               
            elif arv > 0:
               positive_count += 1
               print(f"Positive: {positive_count}")
               
            elif arv == 0:
               zero_count += 1
               print(f"0: {zero_count}")
        break
    except:
        print("Vale formaat")

# ülisane 7




# ülisane 10
for J in range(10):
    a1=float(input("Esimene arv: "))
    a2=float(input("Teine arv: "))
    if a1>a2:
        print(f"Suurem on {a1}")
    elif a2>a1:
        print(f"Suurem on {a2}")
print()




# ülisane 15
for j in range(10):
    for i in range(10):
        print(i, end=" ")
    print()
print()
