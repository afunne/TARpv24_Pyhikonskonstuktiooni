import sys

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
    print(f"Max elanikkond: {str(max(population))}") # .format(max_population, max_city))
    print(f"Min elanikkond: {str(min(population))}") # .format(min_population, min_city))

    questionfor1mil= input("Kirjuta linna nimi, mille te tahate kutsuta: ")

