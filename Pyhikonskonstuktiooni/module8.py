# btw main code starts at 277 line


# from random import *

# TaseKüsimus=input("Panna sinu tase: ")
# countertrue=0
# counterfalse=0

# if TaseKüsimus == "Tase 1":
#     tehed=["+","-"]
#     valitud_tehe=choice(tehed)
#     print(valitud_tehe)
#     if valitud_tehe=="+":
#         print("Oli valitud summa")
#         a=randint(0,5)
#         b=randint(0,5)
#         print(f"Millega võrdub {a} {valitud_tehe} {b} =")
#         vastus=int(input("Anna vastus: "))
#         if vastus==eval(str(a)+valitud_tehe+str(b)):
#             print("Tore!")
#             countertrue+=1
#         else:
#             print("Vale!")
#             counterfalse+=1



# while True:
#     try:
#         if TaseKüsimus == "Tase 2":
#             tehed=["+","-","*","/"]
#             valitud_tehe=choice(tehed)
#             print(valitud_tehe)
#             if valitud_tehe=="+":
#                 print("Oli valitud summa")
#             a=randint(0,5)
#             b=randint(0,5)
#             print(f"Millega võrdub {a} {valitud_tehe} {b} =")
#             vastus=int(input("Anna vastus: "))
#             if vastus==eval(str(a)+valitud_tehe+str(b)):
#                 print("Tore!")
#                 countertrue+=1
#                 break
#             else:
#                 print("Vale!")
#                 counterfalse+=1
#                 break
#     except:
#         print("BRUH")


# while True:
#     try:
#         if TaseKüsimus == "Tase 3":
#             tehed=["+","-","*","/", "**"]
#             valitud_tehe=choice(tehed)
#             print(valitud_tehe)
#             if valitud_tehe=="+":
#                 print("Oli valitud summa")
#             a=randint(0,5)
#             b=randint(0,5)
#             print(f"Millega võrdub {a} {valitud_tehe} {b} =")
#             vastus=int(input("Anna vastus: "))
#             if vastus==eval(str(a)+valitud_tehe+str(b)):
#                 print("Tore!")
#                 countertrue+=1
#                 break
#             else:
#                 print("Vale!")
#                 counterfalse+=1
#             break
#     except:
#         print("BRUH")


# print(f"Õige vastud = {countertrue} and vale vastud {counterfalse}.")

# HindProts=round((countertrue/counterfalse) *100)
# print(f"Protsent on {HindProts}%")
# if HindProts < 60:
#     print("Hinne 2")
# elif 60 <= HindProts < 75:
#     print("Hinne 3")
# elif 75 <= HindProts < 90:
#     print("Hinne 4")
# else:
#     print("Hinne 5")




# I am rewrting this whole code because this one just doesn't work.
# I borrowed some ideas from one of my classmates and from flowchart and official guides from microsoft

# from random import choice, randint

# # dictionary.png
# operators = {
#     "+": lambda a, b: a + b,
#     "-": lambda a, b: a - b,
#     "*": lambda a, b: a * b,
#     "/": lambda a, b: a / b if b != 0 else "undefined",
#     "**": lambda a, b: a ** b
# }

# # counter, GO! 
# countertrue = 0
# counterfalse = 0

# # Functions which I have copied from flowchart
# def play_game(level):
#     global countertrue, counterfalse
#     if level == "Tase 1":
#         tehed = ["+", "-"]
#     elif level == "Tase 2":
#         tehed = ["+", "-", "*", "/"]
#     elif level == "Tase 3":
#         tehed = ["+", "-", "*", "/", "**"]
#     else:
#         print("Vigane tase!")
#         return

#     valitud_tehe = choice(tehed)
#     a = randint(0, 5)
#     b = randint(0, 5)

#     # Ensure b is not 0 for division
#     if valitud_tehe == "/" and b == 0:
#         b = 1  # Avoid division by zero

#     print(f"Millega võrdub {a} {valitud_tehe} {b} =")
#     try:
#         vastus = float(input("Anna vastus: "))  # Allow float for division
#         correct_answer = operators[valitud_tehe](a, b)

#         if vastus == correct_answer:
#             print("Tore!")
#             countertrue += 1
#         else:
#             print(f"Vale! Õige vastus on {correct_answer}.")
#             counterfalse += 1
#     except ValueError:
#         print("Vigane sisend! Palun sisesta number.")

# # Main loop
# while True:
#     TaseKüsimus = input("Panna sinu tase (Tase 1, Tase 2, Tase 3): ")
#     if TaseKüsimus not in ["Tase 1", "Tase 2", "Tase 3"]:
#         print("Vigane tase! Palun vali Tase 1, Tase 2 või Tase 3.")
#         continue

#     play_game(TaseKüsimus)

#     TaseKüsimus2 = input("Kas soovite jätkata? (jah/ei): ")
#     if TaseKüsimus2.lower() != "jah":
#         break

# # Calculate and display results
# print(f"Õige vastud = {countertrue} ja vale vastud = {counterfalse}.")

# if counterfalse == 0:
#     HindProts = 100  # Avoid division by zero
# else:
#     HindProts = round((countertrue / (countertrue + counterfalse)) * 100)

# print(f"Protsent on {HindProts}%")

# if HindProts < 60:
#     print("Hinne 2")
# elif 60 <= HindProts < 75:
#     print("Hinne 3")
# elif 75 <= HindProts < 90:
#     print("Hinne 4")
# else:
#     print("Hinne 5")





# I am rewrting this whole code because this one just doesn't work.
# I borrowed some ideas from one of my classmates and from flowchart and official guides from microsoft

# I forgot we didn't pass defenitions but I will still hold these lines of codes there, sooooo...
# I am changing a code a little bit

# from random import choice, randint

# # Inspared by my classmates
# operators = {
#     "+": lambda a, b: a + b,
#     "-": lambda a, b: a - b,
#     "*": lambda a, b: a * b,
#     "/": lambda a, b: a / b if b != 0 else "undefined",
#     "**": lambda a, b: a ** b
# }

# # Initialize counters
# countertrue = 0
# counterfalse = 0

# # Main loop
# while True:
#     TaseKüsimus = input("Panna sinu tase (Tase 1, Tase 2, Tase 3): ")
#     if TaseKüsimus not in ["Tase 1", "Tase 2", "Tase 3"]:
#         print("Vigane tase! Palun vali Tase 1, Tase 2 või Tase 3.")
#         continue
#     # Determine levels
#     if TaseKüsimus == "Tase 1":
#         tehed = ["+", "-"]
#     elif TaseKüsimus == "Tase 2":
#         tehed = ["+", "-", "*", "/"]
#     elif TaseKüsimus == "Tase 3":
#         tehed = ["+", "-", "*", "/", "**"]
# TaseKüsimus2 = input("Kas soovite jätkata? (jah/ei): ")
# if TaseKüsimus2.lower() != "jah":
#     kuipalju=input(int("Mitu?"))
#     if 



#     # Doing what classmate would do
# while True:
#     valitud_tehe = choice(tehed)
#     a = randint(0, 5)
#     b = randint(0, 5)

#     # if B = 0, im going to explode in 3 seconds (without it, it doesn't work) P.S microsoft support helped me out here!
#     if valitud_tehe == "/" and b == 0:
#         b = 1  # Avoid division by zero

#     # Display the problem
#     print(f"Millega võrdub {a} {valitud_tehe} {b} =")
#     try:
#         vastus = float(input("Anna vastus: "))  # Allow float for division
#         correct_answer = operators[valitud_tehe](a, b)

#         # Check if the answer is correct
#         if vastus == correct_answer:
#             print("Tore!")
#             countertrue += 1
#         else:
#             print(f"Vale! Õige vastus on {correct_answer}.")
#             counterfalse += 1
#     except:
#         print("Vigane sisend! Palun sisesta number.")

#     # Ask if the user wants to continue
#     TaseKüsimus2 = input("Kas soovite jätkata? (jah/ei): ")
#     if TaseKüsimus2.lower() != "jah":
#         break

# # Calculation...
# print(f"Õige vastud = {countertrue} ja vale vastud = {counterfalse}.")

# if counterfalse == 0:
#     HindProts = 100  # Avoid division by zero
# else:
#     HindProts = round((countertrue / counterfalse) * 100)

# print(f"Protsent on {HindProts}%")

# if HindProts < 60:
#     print("Hinne 2")
# elif 60 <= HindProts < 75:
#     print("Hinne 3")
# elif 75 <= HindProts < 90:
#     print("Hinne 4")
# else:
#     print("Hinne 5")





from random import choice, randint

# Initialize counters
countertrue = 0
counterfalse = 0

# User puts a number of levels
while True:
    TaseKüsimus = input("Vali tase (Tase 1, Tase 2, Tase 3): ")
    if TaseKüsimus in ["Tase 1", "Tase 2", "Tase 3"]:
        break
    else:
        print("Vigane tase! Palun vali Tase 1, Tase 2 või Tase 3.")

# Ask the user how many problems they want to solve
while True:
    try:
        num_problems = int(input("Mitu ülesannet soovid lahendada? "))
        if num_problems > 0:
            break
        else:
            print("Palun sisesta positiivne arv!")
    except ValueError:
        print("Vigane sisend! Palun sisesta number.")

# Define operators for each level
if TaseKüsimus == "Tase 1":
    tehed = ["+", "-"]
elif TaseKüsimus == "Tase 2":
    tehed = ["+", "-", "*", "/"]
elif TaseKüsimus == "Tase 3":
    tehed = ["+", "-", "*", "/", "**"]

# Main loop
for i in range(num_problems):
    # Randomly select an operator and generate numbers
    valitud_tehe = choice(tehed)
    a = randint(0, 10)
    b = randint(0, 10)

    # Ensure b is not 0 for division
    if valitud_tehe == "/" and b == 0:
        b = 1  # Avoid division by zero

    # Displaying the problem
    print(f"Millega võrdub {a} {valitud_tehe} {b} =")
    while True:
        try:
            vastus = float(input("Anna vastus: "))  # Allow float for division
            break
        except ValueError:
            print("Vigane sisend! Palun sisesta number.")

    # Calculate the correct answer
    if valitud_tehe == "+":
        correct_answer = a + b
    elif valitud_tehe == "-":
        correct_answer = a - b
    elif valitud_tehe == "*":
        correct_answer = a * b
    elif valitud_tehe == "/":
        correct_answer = a / b
    elif valitud_tehe == "**":
        correct_answer = a ** b

    # Check if the answer is correct
    if vastus == correct_answer:
        print("Tore!")
        countertrue += 1
    else:
        # bro, did you fr do it wrong? nah its okay... I do mistakes as well :<
        print(f"Vale! Õige vastus on {correct_answer}.")
        counterfalse += 1

# Calculate and display results, pls
print(f"Õige vastud = {countertrue} ja vale vastud = {counterfalse}.")

if countertrue + counterfalse == 0:
    HindProts = 0  # Avoid division by zero (without it, it gives me errors for some reason)
else:
    HindProts = round(countertrue / (countertrue + counterfalse)) * 100
    # the reason why it looks like this is because it gives me mistakes *(defenition of 0, yeah?)

print(f"Protsent on {HindProts}%")

if HindProts < 60:
    print("Hinne 2")
elif 60 <= HindProts < 75:
    print("Hinne 3")
elif 75 <= HindProts < 90:
    print("Hinne 4")
else:
    print("Hinne 5")