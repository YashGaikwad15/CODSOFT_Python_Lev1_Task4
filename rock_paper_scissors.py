import random

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "scissors" and computer == "paper") or
        (user == "paper" and computer == "rock")
    ):
        return "user"
    else:
        return "computer"

def main():
    choices = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    round_no = 1

    print("🎮 Rock Paper Scissors Game")

    while True:
        print(f"\n--- Round {round_no} ---")
        user_choice = input("Choose rock, paper, or scissors (or 'quit'): ").lower()

        if user_choice == "quit":
            print("\nFinal Score")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break

        if user_choice not in choices:
            print("❌ Invalid choice! Try again.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        result = get_winner(user_choice, computer_choice)

        if result == "tie":
            print("🤝 It's a tie!")
        elif result == "user":
            print("🎉 You win this round!")
            user_score += 1
        else:
            print("💻 Computer wins this round!")
            computer_score += 1

        print(f"Score → You: {user_score} | Computer: {computer_score}")
        round_no += 1

if __name__ == "__main__":
    main()
