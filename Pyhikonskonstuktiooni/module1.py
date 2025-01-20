nimi=str(input("Mis sinu nimi on?: "))
aastat=int(input("kui vana sa oled?: "))
pikkus=int(input("kui pikk sa oled?: "))
vastus="Tere, maailm!", nimi
vastus2="Sa oled", aastat, "aastat vana"
vastus3="Sa oled", pikkus, "pikkus"
print(vastus, vastus2, vastus3)
#check
aastat = 18
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True
#types
print(type(vastus))
print(type(vastus2))
print(type(vastus3))
print(kas_käib_koolis, type (kas_käib_koolis))

if kas_käib_koolis:
    print(nimi, kas_käib_koolis)
else:
    print(nimi, "ei käi")

#kommid
kommid=int(input("kui kommid" " " + nimi + " " "pannab?: "))
vastus="laual on", kommid
if kommid >= 40:
    print("._.   mitter palju?")
else:
    print(vastus)