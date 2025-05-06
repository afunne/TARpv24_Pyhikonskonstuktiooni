import random
import smtplib

# Global variables for Gmail and SMTP settings
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
GMAIL_USER = 'tahmazovhussejn@gmail.com'
GMAIL_APP_PASSWORD = ''

def load_questions():
    """
    Laeb küsimused ja vastused failist kusimused_vastused.txt sõnastikku.
    """
    questions = {}
    try:
        with open("kusimused_vastused.txt", 'r', encoding='utf-8') as file:
            for line in file:
                if ':' in line:
                    question, answer = line.strip().split(':', 1)
                    questions[question.strip()] = answer.strip()
    except FileNotFoundError:
        print("Warning: kusimused_vastused.txt not found. Creating new file.")
        open("kusimused_vastused.txt", 'w', encoding='utf-8').close()
    return questions

def save_question(question, answer):
    """
    Lisab uue küsimuse ja vastuse faili kusimused_vastused.txt.
    """
    with open("kusimused_vastused.txt", 'a', encoding='utf-8') as file:
        file.write(f"{question}:{answer}\n")

def get_score(item):
    """
    Tagastab osaleja õigete vastuste arvu.
    """
    return item[1]['correct']

def load_completed_participants():
    """
    Laadige nende osalejate nimed ja e-posti aadressid, kes on viktoriini juba täitnud.
    """
    completed_names = set()
    completed_emails = set()
    try:
        with open("koik.txt", 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) >= 3:
                    name = parts[0].strip().lower()
                    email = parts[2].strip().lower()
                    completed_names.add(name)
                    completed_emails.add(email)
    except FileNotFoundError:
        pass
    return completed_names, completed_emails

def conduct_quiz(questions, num_questions, participants):
    """
    Viib läbi küsitluse ühe osaleja jaoks, esitab küsimused,
    kontrollib vastused ja salvestab tulemused.
    """
    completed_names, completed_emails = load_completed_participants()

    while True:
        name = input("Palun sisesta oma nimi: ").strip()
        if not name:
            print("Nimi ei tohi olla tühi!")
            continue

        # Check if the name has already completed the quiz
        if name.lower() in completed_names:
            print("See nimi on juba küsimustikku täitnud! Proovimine keelatud.")
            return None  # Exit if the name already exists in the list of completed participants
        break

    while True:
        email = input("Palun sisesta oma e-posti aadress: ").strip().lower()
        if not email:
            print("E-posti aadress ei tohi olla tühi!")
            continue

        # Check if the email has already been used for the quiz
        if email in completed_emails:
            print("See e-posti aadress on juba küsimustikku täitnud! Proovimine keelatud.")
            return None  # Exit if the email already exists in the list of completed participants
        break


    # Check if name or email already used
    if name.lower() in completed_names:
        print("See nimi on juba küsimustikku täitnud! Proovimine keelatud.")
        return None
    if email in completed_emails:
        print("See e-posti aadress on juba küsimustikku täitnud! Proovimine keelatud.")
        return None

    if len(questions) < num_questions:
        print(f"Hoiatus: Failis on ainult {len(questions)} küsimust. Kasutan kõiki.")
        selected_questions = list(questions.keys())
    else:
        selected_questions = random.sample(list(questions.keys()), num_questions)

    correct = 0

    print(f"\nTere, {name}!")
    print(f"Vastake järgmistele {num_questions} küsimusele:\n")

    for i, question in enumerate(selected_questions, 1):
        user_answer = input(f"{i}. {question} ").strip().lower()
        if user_answer == questions[question].lower():
            correct += 1

    passed = correct > num_questions / 2
    status = "SOBIS" if passed else "EI SOBINUD"

    participants[name] = {
        'correct': correct,
        'email': email,
        'status': status
    }

    return name

def save_results(participants):
    """
    Salvestab tulemused:
    Edukad osalejad faili oiged.txt
    Ebaõnnestunud osalejad faili valed.txt
    """
    # Sort participants by correct answers (descending)
    sorted_by_score = sorted(participants.items(), key=get_score, reverse=True)

    # Save to correct.txt
    with open("oiged.txt", 'w', encoding='utf-8') as file:
        for name, data in sorted_by_score:
            if data['status'] == "SOBIS":
                file.write(f"{name} – {data['correct']} õigesti\n")

    # Sort alphabetically
    sorted_alphabetically = sorted(participants.items())

    # Save to incorrect.txt
    with open("valed.txt", 'w', encoding='utf-8') as file:
        for name, data in sorted_alphabetically:
            if data['status'] != "SOBIS":
                file.write(f"{name}\n")

    # Save to all.txt (append mode to keep history)
    with open("koik.txt", 'a', encoding='utf-8') as file:
        for name, data in participants.items():
            file.write(f"{name}, {data['correct']}, {data['email']}\n")

def send_email(to_email, subject, body):
    """
    Saadab e-kirja määratud aadressile, kasutades Gmaili SMTP serverit.
    """
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(GMAIL_USER, GMAIL_APP_PASSWORD)

        msg = f"From: {GMAIL_USER}\nTo: {to_email}\nSubject: {subject}\n\n{body}"

        server.sendmail(GMAIL_USER, to_email, msg)
        print(f"\nSaadetud: {to_email}")
        print(body)
        server.quit()
    except Exception as e:
        print(f"Viga e-kirja saatmisel {to_email}: {e}")

def notify_participants(participants):
    """
    Saadab kõigile osalejatele isikupärastatud tulemuste e-kirjad.
    """
    for name, data in participants.items():
        email = data['email']
        correct = data['correct']
        status = data['status']

        subject = "Küsimustiku tulemused"

        if status == "SOBIS":
            body = f"Tere {name}!\n\nSinu õigete vastuste arv: {correct}.\nSa sooritasid testi edukalt."
        else:
            body = f"Tere {name}!\n\nSinu õigete vastuste arv: {correct}.\nKahjuks testi ei sooritatud edukalt."

        send_email(email, subject, body)

def notify_admin(participants):
    """
    Saadab administraatorile koondtulemused e-kirjana.
    """
    if not participants:
        return

    sorted_participants = sorted(participants.items(), key=get_score, reverse=True)

    subject = "Küsimustiku koondtulemused"
    body = "Tere!\n\nTänased küsimustiku tulemused:\n\n"

    for i, (name, data) in enumerate(sorted_participants, 1):
        body += (f"{i}. {name} – {data['correct']} õigesti – "
                f"{data['email']} – {data['status']}\n")

    best_name, best_data = sorted_participants[0]
    body += f"\nParim vastaja: {best_name} ({best_data['correct']} õigesti)\n\n"
    body += "Lugupidamisega,\nKüsimustiku Automaatprogramm"

    send_email(GMAIL_USER, subject, body)

def display_results(participants):
    """
    Kuvab küsitluse tulemused ekraanil ja toob välja edukad vastajad.
    """
    print("\nKüsimustiku tulemused:")
    print("=" * 30)

    if not participants:
        print("Küsimustikku ei osalenud keegi.")
        return

    passed = []
    for name, data in participants.items():
        if data['status'] == "SOBIS":
            passed.append((name, data))

    if passed:
        print("\nEdukad vastajad:")
        for name, data in passed:
            print(f"{name}: {data['correct']} õiget vastust")
    else:
        print("\nEdukaid vastajaid ei olnud.")

    print("\nTulemused saadetud e-posti aadressidele.")

def add_new_question():
    """
    Võimaldab administraatoril/lõppkasutajal lisada uusi küsimusi ja vastuseid.
    """
    question = input("Sisesta uus küsimus: ").strip()
    answer = input("Sisesta selle küsimuse õige vastus: ").strip()

    if not question or not answer:
        print("Viga: Küsimus ja vastus ei tohi olla tühjad!")
        return

    save_question(question, answer)
    print("Küsimus lisatud edukalt!")

def main():
    """
    Peamenüü ja juhtloogika küsitluse läbiviimiseks, küsimuste lisamiseks või programmist väljumiseks.
    """
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
            
main()
