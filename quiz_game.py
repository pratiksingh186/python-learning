import random

score = 0

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Delhi", "B. Mumbai", "C. Chennai", "D. Kolkata"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"],
        "answer": "B"
    },
    {
        "question": "Who developed Python?",
        "options": ["A. James Gosling", "B. Dennis Ritchie", "C. Guido van Rossum", "D. Elon Musk"],
        "answer": "C"
    },
    {
        "question": "How many days are there in a week?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "question": "What is 10 + 15?",
        "options": ["A. 20", "B. 25", "C. 30", "D. 35"],
        "answer": "B"
    }
]

random.shuffle(questions)

print("===== PYTHON QUIZ GAME =====")

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Correct answer is {q['answer']}")

total_questions = len(questions)
percentage = (score / total_questions) * 100

print("\n===== QUIZ RESULT =====")
print(f"Score: {score}/{total_questions}")
print(f"Percentage: {percentage:.2f}%")

if percentage >= 80:
    print("Grade: A")
    print("Excellent Performance!")
elif percentage >= 60:
    print("Grade: B")
    print("Good Job!")
elif percentage >= 40:
    print("Grade: C")
    print("Needs Improvement")
else:
    print("Grade: F")
    print("Keep Practicing!")








# ==========================================
# PROJECT: ADVANCED QUIZ GAME
# ==========================================

# Features:
# 1. Multiple-choice questions
# 2. Random question order
# 3. Score tracking
# 4. Percentage calculation
# 5. Grade system

# Concepts Used:
# - Lists
# - Dictionaries
# - Loops
# - Conditions
# - User Input
# - Random Module

# random.shuffle() randomizes the order
# of questions each time the program runs.

# score variable keeps track of
# correct answers.

# percentage is calculated using:
# (score / total_questions) * 100

# Grades:
# A = 80% and above
# B = 60% to 79%
# C = 40% to 59%
# F = Below 40%




