import random
import time

# Define quiz questions and answers
questions = {
    "What is the capital of France?": ["A. Paris", "B. Rome", "C. Berlin", "D. Madrid", "A"],
    "Which planet is known as the Red Planet?": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn", "B"],
    "What is the largest mammal in the world?": ["A. Elephant", "B. Blue Whale", "C. Giraffe", "D. Lion", "B"],
    # Add more questions as needed
}

def display_question(question, options):
    print(question)
    for option in options:
        print(option)
    user_answer = input("Your choice (A, B, C, or D): ").upper()
    return user_answer

def run_quiz():
    score = 0
    questions_list = list(questions.items())
    random.shuffle(questions_list)

    for question, options in questions_list:
        start_time = time.time()

        user_answer = display_question(question, options)
        
        end_time = time.time()
        elapsed_time = end_time - start_time

        # Check user's answer and update the score
        correct_answer = options[-1]
        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {correct_answer}\n")

        # Display elapsed time for answering the question
        print(f"Time taken: {elapsed_time:.2f} seconds\n")

    print("Quiz completed!")
    print(f"Your final score: {score} out of {len(questions)}")

if __name__ == "__main__":
    print("Welcome to the Python Quiz!")
    print("You will be asked multiple-choice questions from various categories.")
    print("Choose the correct option (A, B, C, or D). Let's get started!\n")

    run_quiz()
