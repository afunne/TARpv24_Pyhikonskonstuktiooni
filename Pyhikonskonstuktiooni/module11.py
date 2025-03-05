# n = 9
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if j == i:
#             print(i, end=' ')
#         else:
#             print(0, end=' ')
#     print()

#ul 1
# try:
#     SkvorecProV=int(input("Panna koju number: "))

#     for i in range(SkvorecProV):
#         print(" ----- ")
#         print("|  O  |")
#         print("!  -  !")
#         print(" ----- ")
# except:
#     print("Nuh uh")

# #ul 2
# try:
#     n = int(input("Panna n: "))
#     stepen = int(input("Panna **"))

#     while True:
#         koos=n**stepen
#         if koos > n**3:
#             print("Proovi uuesti!")
#             n = int(input("Panna n: "))
#             stepen = int(input("Panna **"))
#         else:
#             print("Täname!")
#             break
# except:
#     print("Nuh uh")

#ul 3

from random import *
LookImcheesingthis = 0
for õpilased in randrange(25, 36):
    print(f"Klassis on {õpilased} inimest.")
grades = [1, 2, 3, 4, 5]
while True:
    for marks in range(õpilased):
        print(f"See õpilase hind on {grades}.")
        LookImcheesingthis+=1
        if LookImcheesingthis == marks:
            break











