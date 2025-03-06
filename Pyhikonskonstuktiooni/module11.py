
# its porpuse just to be a refernce

# n = 9
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         if j == i:
#             print(i, end=' ')
#         else:
#             print(0, end=' ')
#     print()



#ul 1
try:
    SkvorecProV=int(input("Panna koju number: "))

    for i in range(SkvorecProV):
        print(" ----- ")
        print("|  O  |")
        print("!  -  !")
        print(" ----- ")
except:
    print("Nuh uh")

#ul 2
try:
    n = int(input("Panna n: "))
    stepen = int(input("Panna **"))

    while True:
        koos=n**stepen
        if koos > n**3:
            print("Proovi uuesti!")
            n = int(input("Panna n: "))
            stepen = int(input("Panna **"))
        else:
            print("Täname!")
            print(koos)
            break
except:
    print("Nuh uh")

# #ul 3

from random import *
from math import *
totalsum = 0
õpilased=randrange(25, 36)
# grades = randrange(2, 6)
for i in range(õpilased):
     grades = randrange(2, 6)
     print(grades, end=" ")
     totalsum += grades
average_grade =totalsum/õpilased
print(f"keske hind on: {average_grade:.2f}")
# for i in range(õpilased):
# grades = [randrange(2, 6) for i in range(õpilased)] # this only one problem which I have been having with this uhhhhhhh
# for i in range(õpilased):
#         print(str(õpilased)+ str("grades"), end=", ")
# for i in range(õpilased):

print(f"õpilased on: {õpilased}")
print(f"keske hind on: {average_grade:.2f}") # I found out in forums that adding :.2f is just like rounding, yay :D

#ul 4
# I took some examples from the channel called "Bro Code"
print() # prints here dont do anything they just space out tasks because they looked out of place in my opinion
print()
print("Minu rikas onu kinkis mulle esimeseks sünnipäevaks ühe dollari. Igal sünnipäeval suurendas ta oma kingitust ja lisas sellele nii palju dollareid, kui ma sain ühe aasta vanuseks.")
aasta = 1
dolas = 1 # Reminder that it starts with one dolla dolla (can be 0 idk, I didn't undertsand task)

while dolas <= 100:
    print(f"Sunnipaev: {aasta}, Kingi: {dolas}$")
    aasta += 1
    dolas += aasta # I did these two with tutorials because I got confused what to put here exsacly

print(f"Arvane lopitab {aasta} sunnipaevale ja kingi on: {dolas}$")

#ul 5
# look I just searched in browser I couldn't find this
# theme in moodle, some lines of code were taken from this website:
# https://sky.pro/wiki/python/algoritm-fibonachchi-na-python-poshagovoe-rukovodstvo/
a, b = 0, 1

n = 9 # I was literally guessing here until I got what I needed to do the whole time

# GO, GO MY LOOP!
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b










