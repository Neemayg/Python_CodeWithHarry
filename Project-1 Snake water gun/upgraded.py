import random

# --- 1. A better way to store our choices ---
# This makes it easier to read and print.
CHOICES = {
    's': {'name': 'Snake', 'value': -1},
    'w': {'name': 'Water', 'value': 1},
    'g': {'name': 'Gun', 'value': 0}
}
# We also need a way to look up the name by its value
REVERSE_CHOICES = {-1: 'Snake', 1: 'Water', 0: 'Gun'}


def get_user_choice():
    """
    Keeps asking the user for input until they give a valid one.
    Returns the numeric value for their choice.
    """
    while True:
        # --- 2. Handle case-insensitivity and invalid input ---
        youstr = input("Enter your choice ('s' for Snake, 'w' for Water, 'g' for Gun): ").lower()
        
        if youstr in CHOICES:
            # Get the numeric value (e.g., -1)
            return CHOICES[youstr]['value']
        else:
            print("Invalid choice. Please only enter 's', 'w', or 'g'.")


def get_computer_choice():
    """
    Returns a random numeric value for the computer.
    """
    return random.choice([-1, 1, 0])


def determine_winner(user_val, computer_val):
    """
    Compares the two choices and returns the winner.
    Returns: 'user', 'computer', or 'tie'
    """
    if user_val == computer_val:
        return "tie"

    # Your original logic, just cleaner inside a function
    if (computer_val == -1 and user_val == 1):    # Snake vs Water
        return "computer"
    elif (computer_val == -1 and user_val == 0):  # Snake vs Gun
        return "user"
    elif (computer_val == 1 and user_val == -1):  # Water vs Snake
        return "user"
    elif (computer_val == 1 and user_val == 0):   # Water vs Gun
        return "computer"
    elif (computer_val == 0 and user_val == 1):   # Gun vs Water
        return "user"
    elif (computer_val == 0 and user_val == -1):  # Gun vs Snake
        return "computer"


def play_game():
    """
    The main game loop.
    """
    print("----------------------------------------------------------------")
    print("Welcome to Snake, Water, Gun! Let's play!")
    print("----------------------------------------------------------------")

    # --- 3. Scorekeeping variables ---
    user_score = 0
    computer_score = 0

    while True:
        # --- 4. Calling our clean functions ---
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        # Show the choices
        print(f"\n> You chose:     {REVERSE_CHOICES[user_choice]}")
        print(f"> Computer chose: {REVERSE_CHOICES[computer_choice]}")

        # Determine the winner
        winner = determine_winner(user_choice, computer_choice)

        # --- 5. Print results and update score ---
        if winner == "tie":
            print("It's a TIE!")
        elif winner == "user":
            print("You WIN this round!")
            user_score += 1
        else:
            print("You LOSE this round!")
            computer_score += 1
        
        # Print the current score
        print(f"\n--- Score ---")
        print(f"You: {user_score} | Computer: {computer_score}")
        print("--------------------------------")

        # --- 6. Ask to play again ---
        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            break  # Exit the 'while True' loop

    # --- 7. Final "Game Over" message ---
    print("\nThanks for playing!")
    if user_score > computer_score:
        print(f"Congratulations! You won the game with a final score of {user_score} to {computer_score}!")
    elif computer_score > user_score:
        print(f"Better luck next time! The computer won with a final score of {computer_score} to {user_score}.")
    else:
        print(f"It's a draw! The final score was {user_score} to {user_score}.")


# --- 8. Standard Python way to run the main function ---
if __name__ == "__main__":
    play_game()