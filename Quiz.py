questions = [
    "What is the capital of France?",
    "What is the largest planet in our solar system?",
    "What is the chemical symbol for gold?",
    "Who wrote 'Romeo and Juliet'?",
]

options = [
    ["1. Paris", "2. London", "3. Berlin", "4. Madrid"],
    ["1. Earth", "2. Mars", "3. Jupiter", "4. Saturn"],
    ["1. Au", "2. Ag", "3. Fe", "4. Pb"],
    ["1. William Shakespeare", "2. Charles Dickens", "3. Mark Twain", "4. Jane Austen"],
]

answers = [1, 3, 1, 1]  # 1-based indices

def start_quiz():
    score = 0
    total_guesses = 0

    for i in range(len(questions)):
        print("\n" + questions[i])
        for option in options[i]:
            print(option)

        try:
            guess = int(input("Enter your answer (1-4): "))
            if guess < 1 or guess > 4:
                print("Invalid option. Please enter a number between 1 and 4.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        total_guesses += 1
        if guess == answers[i]:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer was option {answers[i]}.")

    print(f"\nQuiz completed! Your score is {score}/{len(questions)}.")
    print(f"Total valid guesses made: {total_guesses}")

if __name__ == "__main__":
    start_quiz()
