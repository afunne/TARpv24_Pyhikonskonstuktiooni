# YUHHHUUUU FIXING MISTAKES AGAIN

# black list num = float(input("Enter a number: ")) if num < 0: print("The number is negative. ") else: print("The number is not negative.

# importing math stuff like a pro ;)
from math import *
print("Ruudu karakteristikud")

# (a > 0 and b > 0 and c > 0, r > 0):
#     print("lähe. ")
#     else:
#         print("Vale. ")


try:
    a=float(input("Sisesta ruudu külje pikkus => "))
    # checking
    if a > 0:
        S=a**2
        print("Ruudu pindala", S)
        P=4*a
        print("Ruudu ümbermõõt", P)
        di=a*sqrt(2)
        print("Ruudu diagonaal", round(di,2))
        print()
        print("Ristküliku karakteristikud")
    else:
        print("viga")
    # checking
    b=float(input("Sisesta ristküliku 1. külje pikkus => "))
    # checking
    c=float(input("Sisesta ristküliku 2. külje pikkus => "))
    if c > 0 and b > 0:
        S=b*c
        print("Ristküliku pindala", S)
        P=2*(b+c)
        print("Ristküliku ümbermõõt", P)
        di=sqrt(b**2+c**2)
        print("Ristküliku diagonaal", round(di,2))
        print()
        print("Ringi karakteristikud")
    else:
        print("viga")
# checking
    r=float(input("Sisesta ringi raadiusi pikkus => "))
    if r > 0:
        d=2+r
        print("Ringi läbimõõt", d)
        C=pi*r**2
        print("Ringjoone pikkus", round(C,2))
        S=pi*r*2
        print("Ringi pindala", round(S,2))
    else:
        print("viga")
# This  checks if the user inputs any letters
except Exception as e:
    print("vale ", e)