# import sys
# import numpy as np

# def Linnad() -> tuple:
#     """
#     linnad ja kui palju inimesi seal elab
#     """
    
#     # INT_max_population = sys.maxsize  
#     # INT_MIN = -sys.maxsize-1

#     # max_city = ''
#     # min_city =''

#     # max_population = INT_MIN
#     # min_population = INT_max_population
#     city = []
#     population = []

#     n = int(input("Kui palju adnmed pannad?: "))

#     for i in range(n):
#         name = input("Sisesta linna nimi: ")
#         city.append(name)
#         howmany = int(input("Sisesta elanikkond: "))
#         population.append(howmany)

#         # city = input("Sisesta linna nimi: ")
#         # list.city[i] = [city]
#         # population = int(input("Sisesta elanikkond: "))
#         # list.population[i] = [population]
#         # print(f"{city} - {population}")

#     # if max_population < population:
#     #     max_population = population
#     #     max_city = city

#     # if min_population>population:
#     #     min_population = population
#     #     min_city = city
#     # city_pop = city.index == population.index
#     common = np.intersect1d(city, max(population))
#     print(common)

#     common2 = np.intersect1d(city, min(population))
#     print(common2)

    
#     # for i in city:
#     #     print(f"{city.index(i)+1}: {i}")

#     #     choice = input("Which game you wanna play with me??")

#     # print(List_Of_Games[choice])


#     print(f"Max elanikkond: {tuple(common)}") # .format(max_population, max_city))
#     print(f"Min elanikkond: {tuple(common2)}") # .format(min_population, min_city))


#     # questionfor1mil= input("Kirjuta linna nimi, mille te tahate kutsuta: ")
#     # print(name in questionfor1mil)
#     # if True:
#     #     print(questionfor1mil, population[questionfor1mil])
#     # elif False:
#     #     print("Huh")


#     common = np.intersect1d(city, max(population))
#     print(common)

#     common2 = np.intersect1d(city, min(population))
#     print(common2)

#     # for i in city:
#     #     print(f"{city.index(i)+1}: {i}")
#     #     print(f"{population.index(i)+1}: {i}")
#     #     choice = input("Kirjuta linna nimi, mille te tahate kutsuta: ")
#     # print(city[choice], population[choice])

#     for i in city:
#         print(f"{city.index(i)+1}: {i}")
#         choice = input("Kirjuta linna nimi, mille te tahate kutsuta: ")
#     print(city[choice], population(index = choice))


import sys

def Linnad() -> tuple:
    """
    Kogub linnade nimed ja rahvaarvud, seejärel leiab linna, mille rahvaarv on maksimaalne ja minimaalne.
    """
    cities = []
    populations = []

    n = int(input("Kui palju andmeid sisestad?: "))

    for i in range(n):
        name = input("Sisesta linna nimi: ")
        cities.append(name)
        howmany = int(input("Sisesta elanikkond: "))
        populations.append(howmany)

    # Find max and min population with their cities
    max_pop = max(populations)
    min_pop = min(populations)
    
    max_cities = [city for city, pop in zip(cities, populations) if pop == max_pop]
    min_cities = [city for city, pop in zip(cities, populations) if pop == min_pop]

    print("\nTulemused:")
    print(f"Maksimaalne elanikkond: {max_pop} ({', '.join(max_cities)})")
    print(f"Minimaalne elanikkond: {min_pop} ({', '.join(min_cities)})")

    # Additional feature to look up specific city
    while True:
        print(
            """
1 - kui palju
2 - Kuvatakse linnade loetelu ja elanike arv tähestikulises järjekorras
3 - Sisestage elanike arv ja kuvage lähima ligikaudse elanike arvuga linna nimi 
4 - Leia vähem kui n elanikuga linnad
            """)
        choice = int(input("Sisesta sinu valik"))
        if choice == 3:
            city_data = list(zip(cities, populations))
            # index = cities.index(choice)
            # print(f"{choice}: {populations[index]} elanikku")
        # else:
        #     print("Sellist linna nimekirjas ei ole.")
            H=sorted(city_data, key=H)
            for city, pop in H:
                print(f"{city}: {pop} elanikud")
        elif choice==4:
            # n = int(input("Sisestage elanike arv: "))
            # for city, pop in city_data:
            #     if pop < n:
            #         print(f"{city}: {pop} elanikud")
            target_pop = int(input("Sisestage elanike arv: "))

            population_difference = abs(populations[1] - target_pop)
            closest_city = min(city_data, key=population_difference)
            print(f"Lähim linn: {closest_city[0]} ({closest_city[1]} elanikud)")
            # for city, pop in city_data:
            #     if pop == target_pop:
            #         print(city)

        elif choice==5:
            n = int(input("Sisestage elanike arv: "))
            for city, pop in city_data:
                if pop < n:
                    print(f"{city}: {pop} elanikud")

        elif choice==0:
            break
    return (max_cities, min_cities)