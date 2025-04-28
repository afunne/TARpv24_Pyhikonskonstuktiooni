import random
import smtplib
from email.message import EmailMessage

def load_questions():
    """Load questions from the questions file"""
    questions = {}
    try:
        with open("kusimused_vastused.txt", 'r', encoding='utf-8') as file:
            for line in file:
                if ':' in line:
                    question, answer = line.strip().split(':', 1)
                    questions[question.strip()] = answer.strip()
    except FileNotFoundError:
        print("Error: Could not find questions file!")
    return questions

def add_question():
    """Add a new question to the questions file"""
    print("\n--- Add New Question ---")
    question = input("Enter the new question: ").strip()
    answer = input("Enter the correct answer: ").strip()
    
    with open("kusimused_vastused.txt", 'a', encoding='utf-8') as file:
        file.write(f"{question}:{answer}\n")
    print("Question added successfully!")

def generate_email(name):
    """Generate an email address from the participant's name"""
    name_parts = name.lower().split()
    if len(name_parts) >= 2:
        return f"{name_parts[0]}.{name_parts[1]}@example.com"
    return f"{name_parts[0]}@example.com"

def get_participant_score(participant):
    """Helper function to get score for sorting"""
    return int(participant[1])

def run_quiz():
    """Run the quiz and save results"""
    questions = load_questions()
    if not questions:
        print("No questions available!")
        return
    
    participant_name = input("\nEnter your name: ").strip()
    participant_email = generate_email(participant_name)
    
    # Prepare and shuffle questions
    question_list = list(questions.items())
    random.shuffle(question_list)
    questions_to_ask = min(5, len(question_list))
    
    correct_answers = 0
    for question_number, (question, correct_answer) in enumerate(question_list[:questions_to_ask], 1):
        user_answer = input(f"\n{participant_name}, question {question_number}: {question} ").strip().lower()
        
        if user_answer == correct_answer.lower():
            correct_answers += 1
            print("Correct!")
        else:
            print(f"Incorrect! The right answer is: {correct_answer}")
    
    # Save results to files
    result_line = f"{participant_name} – {correct_answers} correct\n"
    passing_threshold = questions_to_ask / 2
    
    if correct_answers > passing_threshold:
        with open("oiged.txt", 'a', encoding='utf-8') as file:
            file.write(result_line)
    else:
        with open("valed.txt", 'a', encoding='utf-8') as file:
            file.write(result_line)
    
    # Save to all participants file
    with open("koik.txt", 'a', encoding='utf-8') as file:
        file.write(f"{participant_name}, {correct_answers}, {participant_email}\n")
    
    # Send results email
    send_results_email(participant_name, participant_email, correct_answers, questions_to_ask)

def send_results_email(name, email, correct_count, total_questions):
    """Send quiz results to participant"""
    email_message = EmailMessage()
    email_message['Subject'] = "Your Quiz Results"
    email_message['From'] = "quiz@example.com"
    email_message['To'] = email
    
    passed = correct_count > total_questions / 2
    email_body = f"""Hello {name}!

Your results:
- Correct answers: {correct_count} out of {total_questions}
- Status: {"PASSED" if passed else "FAILED"}

Thank you for participating!"""
    
    email_message.set_content(email_body)
    
    try:
        with smtplib.SMTP("smtp.example.com", 587) as server:
            server.starttls()
            server.login("your_email@example.com", "your_password")
            server.send_message(email_message)
        print(f"Results sent to {email}")
    except Exception as error:
        print(f"Failed to send email: {error}")

def send_summary_report():
    """Send summary report to employer"""
    try:
        with open("koik.txt", 'r', encoding='utf-8') as file:
            participants = [line.strip().split(', ') for line in file if line.strip()]
    except FileNotFoundError:
        print("No participants yet!")
        return
    
    if not participants:
        print("No participants yet!")
        return
    
    # Sort participants by score (descending)
    participants.sort(key=get_participant_score, reverse=True)
    
    report_message = EmailMessage()
    report_message['Subject'] = "Quiz Summary Report"
    report_message['From'] = "quiz@example.com"
    report_message['To'] = "employer@company.ee"
    
    report_content = "Hello!\n\nToday's quiz results:\n\n"
    
    # Generate report lines for each participant
    for position, participant_data in enumerate(participants, start=1):
        name, score, email = participant_data
        
        passing_score = 3  # More than half correct (assuming 5 questions)
        status = "PASSED" if int(score) >= passing_score else "FAILED"
        
        report_line = (
            f"{position}. {name} – {score} correct – "
            f"{email} – {status}\n"
        )
        report_content += report_line
    
    # Add best participant and closing
    best_participant = participants[0]
    report_content += (
        f"\nBest participant: {best_participant[0]} "
        f"({best_participant[1]} correct)\n\n"
        "Regards,\n"
        "Quiz Automatic System"
    )
    
    report_message.set_content(report_content)
    
    try:
        with smtplib.SMTP("smtp.example.com", 587) as server:
            server.starttls()
            server.login("your_email@example.com", "your_password")
            server.send_message(report_message)
        print("Summary report sent to employer@company.ee")
    except Exception as error:
        print(f"Failed to send report: {error}")

def show_results():
    """Show participants who passed"""
    try:
        with open("oiged.txt", 'r', encoding='utf-8') as file:
            passed_participants = file.readlines()
    except FileNotFoundError:
        passed_participants = []
    
    print("\n=== PARTICIPANTS WHO PASSED ===")
    for participant in passed_participants:
        print(participant.strip())
    print("\nResults have been sent to all email addresses.")

def initialize_files():
    """Create necessary files if they don't exist"""
    for filename in ["kusimused_vastused.txt", "oiged.txt", "valed.txt", "koik.txt"]:
        try:
            open(filename, 'x', encoding='utf-8').close()
        except FileExistsError:
            pass
    
    # Add sample questions if questions file is empty
    try:
        with open("kusimused_vastused.txt", 'r+', encoding='utf-8') as file:
            if not file.read(1):
                file.write("What is Python?:programming language\n")
                file.write("What color is snow?:white\n")
                file.write("Capital of Estonia?:Tallinn\n")
    except FileNotFoundError:
        pass

def main_menu():
    """Display and handle main menu"""
    while True:
        print("\n=== QUIZ SYSTEM ===")
        print("1. Take the Quiz")
        print("2. Add New Question")
        print("3. View Results")
        print("4. Send Summary Report")
        print("5. Exit")
        
        choice = input("Select option (1-5): ").strip()
        
        if choice == '1':
            run_quiz()
        elif choice == '2':
            add_question()
        elif choice == '3':
            show_results()
        elif choice == '4':
            send_summary_report()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    initialize_files()
    main_menu()
