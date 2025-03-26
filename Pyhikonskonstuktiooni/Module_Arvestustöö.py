import sys
import numpy as np

def Linnad() -> tuple:
    """
    linnad ja kui palju inimesi seal elab
    """
    
    # INT_max_population = sys.maxsize  
    # INT_MIN = -sys.maxsize-1

    # max_city = ''
    # min_city =''

    # max_population = INT_MIN
    # min_population = INT_max_population
    city = []
    population = []

    n = int(input("Kui palju adnmed pannad?: "))

    for i in range(n):
        name = input("Sisesta linna nimi: ")
        city.append(name)
        howmany = int(input("Sisesta elanikkond: "))
        population.append(howmany)

        # city = input("Sisesta linna nimi: ")
        # list.city[i] = [city]
        # population = int(input("Sisesta elanikkond: "))
        # list.population[i] = [population]
        # print(f"{city} - {population}")

    # if max_population < population:
    #     max_population = population
    #     max_city = city

    # if min_population>population:
    #     min_population = population
    #     min_city = city
    # city_pop = city.index == population.index
    common = np.intersect1d(city, max(population))
    print(common)

    common2 = np.intersect1d(city, min(population))
    print(common2)

    
    # for i in city:
    #     print(f"{city.index(i)+1}: {i}")

    #     choice = input("Which game you wanna play with me??")

    # print(List_Of_Games[choice])


    print(f"Max elanikkond: {tuple(common)}") # .format(max_population, max_city))
    print(f"Min elanikkond: {tuple(common2)}") # .format(min_population, min_city))


    # questionfor1mil= input("Kirjuta linna nimi, mille te tahate kutsuta: ")
    # print(name in questionfor1mil)
    # if True:
    #     print(questionfor1mil, population[questionfor1mil])
    # elif False:
    #     print("Huh")


    common = np.intersect1d(city, max(population))
    print(common)

    common2 = np.intersect1d(city, min(population))
    print(common2)

    # for i in city:
    #     print(f"{city.index(i)+1}: {i}")
    #     print(f"{population.index(i)+1}: {i}")
    #     choice = input("Kirjuta linna nimi, mille te tahate kutsuta: ")
    # print(city[choice], population[choice])

    for i in city:
        print(f"{city.index(i)+1}: {i}")
        choice = input("Kirjuta linna nimi, mille te tahate kutsuta: ")
    print(city[choice], population(index = choice))
