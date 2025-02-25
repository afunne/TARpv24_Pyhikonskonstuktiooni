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
while True:
    try:
        A = int(input("Sisestage intervalli algus: "))
        B = int(input("Sisestage intervalli lõpp: "))
        if A < B:
            K = int(input("Sisestage arv K: "))
            if K > 0:
                for i in range(A, B + 1):
                    if i % K == 0:
                        print(i, end=" ")
                        print()
                break
            else:
                print("K peab olema rohkem kui 0")
        else:
            print("lõpp peab olema rohkem kui algus")
    except:
        print("Ainult numbrid")

# ülisane 8
print("Tollid | Sentimeetrit")
print("------------------")
for i in range(1, 21):
    cm = i * 2.5
    print(f"{i} | {cm}")

# ülisane 9
while True:
    try:
        S = float(input("Sisestage esialgne hoiuse summa: "))
        N = int(input("Sisesta aastate arv: "))

        for _ in range(N):
            S *= 1.03 # 3%

        print(f"Hoiuse summa pärast {N} aastat: {round(S,2)} eurot")
        break
    except:
        print("Ainult numbrid")

# ülisane 10
for J in range(10):
    a1=float(input("Esimene arv: "))
    a2=float(input("Teine arv: "))
    if a1>a2:
        print(f"Suurem on {a1}")
    elif a2>a1:
        print(f"Suurem on {a2}")
print()

# ülisane 11
import random

K = random.randint(1, 50)
print(f"Genereeritud number: {K}")

product = 1

for num in range(11, 100, 2):
    if num % K == 0:
        product *= num

if product>1:
    print(f"Kahekohaliste paaritute arvude korrutis, mis on jagatavad {K}: {product}")
else:
    print(f"Ei ole kahekohalisi paarituid numbreid, mis on jagatavad {K}.")

# ülisane 12
N = int(input("Sisestage heinategijate arv: "))
m = int(input("Sisestage esimese heinaküünla tööaeg (tundid): "))

total_hours = 0
for i in range(N):
    total_hours = m + (i * 10 / 60)

print(f"Kogu meeskond töötas {round(total_hours)} tundi.")

# ülisane 13
count = 0
total_sum = 0

for number in range(100, 1001):
    if number % 7 == 0:
        count += 1
        total_sum += number
print(f"jagatavate arvude arv: {count}")
print(f"jagatavate arvude summa: {total_sum}")

# ülisane 14
import random
N = random.randint(1, 20)
product = 1

for i in range(1, N + 1):
    product *= i

print(f"Juhuslik number N: {N}")
print(f"Numbrite 1 kuni {N}: {product}")


# ülisane 15
for j in range(10):
    for i in range(10):
        print(i, end=" ")
    print()
print()

# ülisane 16
n = 9
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j == i:
            print(i, end=' ')
        else:
            print(0, end=' ')
    print()