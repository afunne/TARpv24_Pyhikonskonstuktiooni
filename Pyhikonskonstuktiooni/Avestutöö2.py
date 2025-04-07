from Module_Arvestutöö2 import *

palgad=[2500,2500,750,395,1200]
inimesed=["A","B","C","D","E"]

while True:
    # try:
        choice=int(input("Mida te tahate teha? "))

        if choice==1:
            #yada yada yada
            print()
            mitu=int(input("Mitu andmed te pannate? "))
            for i in range (mitu):
                Lisa_andmed(palgad, inimesed)

        elif choice==2:
            #yada yada yada
            print()
            Kutsuta_andmed(palgad, inimesed)
        
        elif choice==3:
            #yada yada yada
            print()
            Suurim_palk(palgad, inimesed)
            continue
        elif choice==4:
            #yada yada yada
            print()
        
        elif choice==5:
            #yada yada yada
            print()
            sorteerimine(palgad, inimesed)
        
        elif choice==6:
            #yada yada yada
            print()
            Võrdsed_palgad(palgad, inimesed)

        elif choice==7:
            #yada yada yada
            print()
            Keskel_palk(palgad, inimesed)
        
        elif choice==8:
            #yada yada yada
            print()
            Väiksem_palk(palgad, inimesed)
        
        elif choice==9:
            #yada yada yada
            print()
            otsima_palkjanimi(palgad, inimesed)
        
        elif choice==1:
            #yada yada yada
            print()
        
        elif choice==1:
            #yada yada yada
            print()
        elif choice==0:
            print("Bye, bye! :3")
            break
        else:
            print("Bruh, are you fr rn?")
    # except:
    #     print("kys")