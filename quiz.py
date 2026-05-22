import random
import time
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

print(Fore.CYAN + "===== Welcome to AI Quiz Generator =====")

score = 0

# Select difficulty
print("\nChoose Difficulty Level:")
print("1. Easy")
print("2. Medium")
print("3. Hard")

difficulty_choice = input("Enter choice: ")

difficulty_map = {
    "1": "easy",
    "2": "medium",
    "3": "hard"
}

print(Fore.RED+"\nEach question has 1 minute to answer.\n")
selected_difficulty = difficulty_map.get(difficulty_choice)

if not selected_difficulty:
    print(Fore.RED + "Invalid Choice!")
    exit()

# Read questions
with open("questions.txt", "r") as file:
    all_questions = file.readlines()

# Filter questions based on difficulty
filtered_questions = []

for line in all_questions:
    data = line.strip().split("|")

    if data[0] == selected_difficulty:
        filtered_questions.append(data)

# Randomize questions
random.shuffle(filtered_questions)

# Take only 5 random questions
questions = filtered_questions[:5]

total_questions = len(questions)

# Quiz Loop
for index, q in enumerate(questions, start=1):

    difficulty, question, op1, op2, op3, op4, correct = q

    print(Fore.YELLOW + f"\nQuestion {index}:")
    print(Fore.WHITE + question)

    print(Fore.BLUE + f"1. {op1}")
    print(Fore.BLUE + f"2. {op2}")
    print(Fore.BLUE + f"3. {op3}")
    print(Fore.BLUE + f"4. {op4}")

    # Timer start
    start_time = time.time()

    answer = input(Fore.GREEN + "Enter option number: ")

    end_time = time.time()

    time_taken = end_time - start_time

    # Timer validation
    if time_taken > 60:
        print(Fore.RED + "Time Up! You exceeded 1 minute.")
        continue

    # Answer validation
    if answer == correct:
        print(Fore.GREEN + "Correct Answer!")
        score += 1
    else:
        print(Fore.RED + "Wrong Answer!")
        print(Fore.CYAN + f"Correct Option: {correct}")

# Final Result
print(Fore.MAGENTA + "\n===== Quiz Finished =====")
print(Fore.CYAN + f"Final Score: {score}/{total_questions}")

# Save score
with open("scores.txt", "a") as score_file:
    score_file.write(f"{selected_difficulty} Score: {score}/{total_questions}\n")

print(Fore.GREEN + "Score saved successfully!")