# import random

# d = {} # initialize empty dictionary 

# # Create and write to input.txt
# with open('kusimused_vastused.txt', 'w') as f:
#     f.write("what is the best drink on this world?: kvass\nhow much robux I have?: 300") 

# # Read and process the file into a dictionary
# with open('kusimused_vastused.txt', 'r') as file:
#     for line in file:
#         key, value = line.strip().split(':', 1)
#         d[key.strip()] = value.strip()
# print(d)

# Q = random.choice(list(d.keys()))
# print(Q)

import random
# Import smtplib for the actual sending function
import smtplib
# Import the email modules we'll need
from email.mime.text import MIMEText

d = {} # initialize empty dictionary 

# Create and write to input.txt
with open('kusimused_vastused.txt', 'w') as f:
    f.write("what is the best drink on this world?: kvass\nhow much robux I have?: 300") 

# Read and process the file into a dictionary
with open('kusimused_vastused.txt', 'r') as file:
    for line in file:
        key, value = line.strip().split(':', 1)
        d[key.strip()] = value.strip()

def load_questions():
    questions = {}
    with open('kusimused_vastused.txt', 'r') as file:
        for line in file:
            key, value = line.strip().split(':', 1)
            questions[key.strip()] = value.strip()
    return questions

def save_results(file_name, data):
    with open(file_name, 'w') as file:
        for line in data:
            file.write(line + '\n')

def generate_email(name, familyname):
    first=name
    second=familyname
    return f"{first.lower()}{second.lower()}@gmail.com"


def ask_questions(name, questions, n):
    selected_questions = random.sample(list(questions.items()), n)
    correct_answers = 0

    for question, answer in selected_questions:
        user_answer = input(f"{name}, {question} ").strip().lower()
        if user_answer == answer.lower():
            correct_answers += 1

    return correct_answers

def send_email(to_email, subject, body):
    # Dummy email function: Replace with real email logic
    print(f"E-posti saatmine aadressil {to_email}...")
    print(f"Teema: {subject}")
    print(body)



# import random

# def Theboyshungry():
#     """
#     """
#     d = {} # initialize empty dictionary 

#     # Create and write to input.txt
#     with open('kusimused_vastused.txt', 'w') as f:
#         f.write("what is the best drink on this world?: kvass\nhow much robux I have?: 300") 

#     # Read and process the file into a dictionary
#     with open('kusimused_vastused.txt', 'r') as file:
#         for line in file:
#             key, value = line.strip().split(':', 1)
#             d[key.strip()] = value.strip()
#             Q = random.choice(list(d.keys()))
#             print(Q)

#     with open('kusimused_vastused.txt', 'r') as file:
#         for line in file:
#             key, value = line.strip().split(':', 1)


