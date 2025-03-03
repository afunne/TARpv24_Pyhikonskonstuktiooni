#abs()
#sleep()
print("*** MÄNG ARVUTIGA ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        # you dont have to put brackets before abs
        a = abs(int(input("sisesta täisarv => ")))
        break
    except ValueError:
         print("Это не целое число")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("nuliga ei tööta")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Определяем, сколько в числе чётных и сколько нечётных цифр")
    print()
    c=b=a
    paaris = 0
    paaritu = 0
    while b > 0:
          # we use = then we are setting variables, we are using == to follow instructions 
            if b % 2 == 0:
                    paaris += 1
            else:
                    paaritu += 1
            b = b // 10
    
    # correct syntaks ( print("Чётных цифр:", paaris))
    print("Чётных цифр:", paaris) 
    print("Нечётных цифр:", paaritu)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
for i in range(50):

#b becomes useless
    print("*Переворачиваем* введённое число")
    print()
    b=0
    while a > 0:
        number = a % 10
        a = a // 10
        b = b * 10
        b += number
    print("*Перевёрнутое* число", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Проверяем гипотезу Сиракуз")
    print()

    while c != 1:
            if c % 2 == 0:
                print('{:>4}'.format(round(c))," - Paaris arv, Jagame 2.")
                c = c / 2
            else:
                print('{:>4}'.format(round(c))," - Paaritu arv. Korrutame 3, liidame 1 ja jagame 2.")
                c = (3*c + 1) / 2
    print()
    print("Гипотеза верна")