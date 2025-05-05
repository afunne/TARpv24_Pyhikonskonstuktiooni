from imfixingsomethingiesagain import *

participants = {}
questions = load_questions()

while True:
        print("\n=== PEAMENÜÜ ===")
        print("1. Alusta küsimustikku")
        print("2. Lisa uus küsimus")
        print("3. Välju")

        choice = input("Vali tegevus (1-3): ").strip()

        if choice == "1":
            if not questions:
                print("Hoiatus: Küsimusi ei ole. Palun lisa küsimusi enne küsimustiku alustamist.")
                continue

            num_participants = int(input("Mitu inimest soovid küsitleda? "))
            num_questions = int(input("Mitu küsimust igale inimesele esitada? "))

            if num_questions > len(questions):
                print(f"Hoiatus: Failis on ainult {len(questions)} küsimust. Kasutan kõiki.")
                num_questions = len(questions)

            for _ in range(num_participants):
                conduct_quiz(questions, num_questions, participants)

            if participants:
                save_results(participants)
                notify_participants(participants)
                notify_admin(participants)
                display_results(participants)

        elif choice == "2":
            add_new_question()
            questions = load_questions()

        elif choice == "3":
            print("Programm lõpetab töö.")
            break

        else:
            print("Vigane valik. Palun proovi uuesti.")
