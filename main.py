import random

# Possible moves
moves = ["rock", "paper", "scissors"]

# Get player move
def get_player_move():
    while True:
        player_move = input("Enter rock, paper, or scissors: ").strip().lower()

        if player_move in moves:
            return player_move
        else:
            print("Invalid move. Please enter rock, paper, or scissors.")

# AI selects a move using frequency analysis
def get_ai_move(player_history):
    if len(player_history) < 3:
        return random.choice(moves)

    # Count the player's move history
    rock_count = player_history.count("rock")
    paper_count = player_history.count("paper")
    scissors_count = player_history.count("scissors")

    # Predict the player's most frequent move
    most_frequent = max(
        moves,
        key=lambda move: player_history.count(move)
    )

    # Choose the move that beats the predicted move
    counter_moves = {
        "rock": "paper",
        "paper": "scissors",
        "scissors": "rock"
    }

    return counter_moves[most_frequent]

# Determine the winner
def determine_winner(player_move, ai_move):
    if player_move == ai_move:
        return "tie"

    winning_combinations = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock"
    }

    if winning_combinations[player_move] == ai_move:
        return "player"
    else:
        return "ai"

# Main game
def play_game():
    player_score = 0
    ai_score = 0
    player_history = []

    print("Welcome to Rock Paper Scissors with AI!")

    while True:
        player_move = get_player_move()
        ai_move_choice = get_ai_move(player_history)

        print(f"You chose: {player_move}")
        print(f"AI chose: {ai_move_choice}")

        result = determine_winner(player_move, ai_move_choice)

        if result == "player":
            print("You win this round!")
            player_score += 1
        elif result == "ai":
            print("AI wins this round!")
            ai_score += 1
        else:
            print("This round is a tie!")

        # Store the player's move
        player_history.append(player_move)

        print(f"Score: Player {player_score} - AI {ai_score}")

        play_again = input("Play another round? (yes/no): ").strip().lower()

        if play_again != "yes":
            break

    print("\nFinal Score:")
    print(f"Player: {player_score}")
    print(f"AI: {ai_score}")
    print("Thank you for playing!")

if __name__ == "__main__":
    play_game()
