import random
import time

# Define the quiz questions and answers
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Paris", "C. London", "D. Rome"],
        "correct_answer": "B"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Mars", "B. Venus", "C. Jupiter", "D. Saturn"],
        "correct_answer": "A"
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["A. Elephant", "B. Giraffe", "C. Blue Whale", "D. Dolphin"],
        "correct_answer": "C"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Mark Twain"],
        "correct_answer": "B"
    },
    {
        "question": "Which programming language is often used for data analysis?",
        "options": ["A. Java", "B. Python", "C. C++", "D. Ruby"],
        "correct_answer": "B"
    },
    {
        "question": "What is the capital of Japan?",
        "options": ["A. Seoul", "B. Beijing", "C. Tokyo", "D. Bangkok"],
        "correct_answer": "C"
    },
    {
        "question": "In which year did World War II end?",
        "options": ["A. 1945", "B. 1939", "C. 1941", "D. 1943"],
        "correct_answer": "A"
    },
    {
        "question": "What is the powerhouse of the cell?",
        "options": ["A. Nucleus", "B. Mitochondria", "C. Ribosome", "D. Endoplasmic Reticulum"],
        "correct_answer": "B"
    },
    {
        "question": "Which famous scientist developed the theory of relativity?",
        "options": ["A. Isaac Newton", "B. Albert Einstein", "C. Galileo Galilei", "D. Nikola Tesla"],
        "correct_answer": "B"
    },
    {
        "question": "What is the currency of India?",
        "options": ["A. Yen", "B. Rupee", "C. Euro", "D. Dollar"],
        "correct_answer": "B"
    },
]

def run_quiz():
    score = 0
    random.shuffle(quiz_questions)  # Shuffle the questions for variety

    for question_data in quiz_questions:
        print("\n" + question_data["question"])
        for option in question_data["options"]:
            print(option)

        user_answer = input("Your answer (Enter A, B, C, or D): ").upper()

        if user_answer == question_data["correct_answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question_data['correct_answer']}.\n")

    print(f"Quiz completed! Your score is {score}/{len(quiz_questions)}.")

if __name__ == "__main__":
    print("Welcome to the Console Quiz!\n")
    input("Press Enter to start the quiz...")

    start_time = time.time()  # Record the start time
    run_quiz()
    end_time = time.time()  # Record the end time

    elapsed_time = round(end_time - start_time, 2)
    print(f"Total time taken: {elapsed_time} seconds.")
