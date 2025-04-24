from PraktilineTöö import *



participants = {}
questions = load_questions()
N = min(5, len(questions)) # Number of questions per participant    
M = 2 # Number of participants



while True:
    print("- - - :3 MOEW MENU :3 - - -")
    print("  1. Alustage küsimustikku")
    print("  2. Lisa uus küsimus")
    print("  3. Lõppus")
    choice = input("Choose an option: ")
    if choice == "1":
        first = input("Sisesesta oma nimi: ")
        second = input("Sisesesta oma perenimi: ")
        if first and second in participants:
            print("Te olete juba osalenud.")
            continue
        email = generate_email(first, second)
        correct_answers = ask_questions(first, second, questions, N)
        participants[first] = correct_answers
        if correct_answers >= N // 2:
            result = f"{first} - {correct_answers} õigesti"
            send_email(email, "Test kokkuvõite", f"Tere {first},\nSa vastanud {correct_answers} küsimudele õigesti - SOBIS")
        else:
            result = f"{first} - {correct_answers} õigesti - EI SOBINUD"
            send_email(email, "Testitulemus“, f“Tere {nimi},\nSina vastasid {vale_vastused} küsimustele õigesti. Kahjuks ei läbinud te testi.")
        # Save results
        passed = sorted([f"{first} - {score}" for first, score in participants.items()
        if score >= N // 2], key=lambda x: -int(x.split('-')[1]))
        failed = sorted([f"{name}" for name, score in participants.items() if score < N // 2])
        all_results = [f"{first}, {score}, {generate_email(first)}" for first, score in participants.items()]
        save_results('oiged.txt', passed)
        save_results('valed.txt', failed)
        save_results('koik.txt', all_results)

        #Send summary to employer
        summary = "\n".join([f"{name} - {score} - {generate_email(name)} - {'PASSED' if score >= N // 2 else 'FAILED'}" for name, score in participants.items()])
        best_participant = max(participants.items(), key=lambda x: x[1])
        send_email("tootaja@firma.ee", "Daily Test Summary", f"Today's results:\n\n{summary}\n\nBest participant: {best_participant[0]} ({best_participant[1]} correct answers)")
        print("Results sent to participants and employer.")
        break
    elif choice == "2":
        new_question = input("Enter the new question: ").strip()
        new_answer = input("Enter the correct answer: ").strip()
        with open('kusimused_vastused.txt', 'a') as file:
            file.write(f"{new_question}:{new_answer}\n")
            print("New question added.")
    elif choice == "3":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")











