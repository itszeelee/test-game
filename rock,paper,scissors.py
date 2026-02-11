"""
Rock-Paper-Scissors: Best of Five
Simple console game: first to 3 wins (ties do not count).
"""


import random

CHOICES = {
    'r': 'rock',
    'p': 'paper',
    's': 'scissors',
    'rock': 'rock',
    'paper': 'paper',
    'scissors': 'scissors'
}

WIN_RULES = {
    ('rock', 'scissors'),
    ('scissors', 'paper'),
    ('paper', 'rock')
}


def get_player_choice() -> str | None:
    """Prompt the player and return normalized choice or None if quitting."""
    raw = input("Enter rock/paper/scissors (r/p/s) or q to quit: ").strip().lower()
    if not raw:
        return None
    if raw == 'q':
        return None
    return CHOICES.get(raw)


def get_computer_choice() -> str:
    return random.choice(['rock', 'paper', 'scissors'])


def decide_winner(p: str, c: str) -> str:
    """Return 'player', 'computer', or 'tie'."""
    if p == c:
        return 'tie'
    if (p, c) in WIN_RULES:
        return 'player'
    return 'computer'


def play_round(round_no: int) -> tuple[int, int, bool]:
    """Play a single round. Returns (player_point, computer_point, valid_round).

    valid_round is False for invalid input or quit (no points), or True if a decisive/tie round occurred.
    """
    print(f"\n--- Round {round_no} ---")
    player = get_player_choice()
    if player is None:
        print("Quitting the game.")
        return 0, 0, False
    comp = get_computer_choice()
    print(f"You played: {player}")
    print(f"Computer played: {comp}")
    result = decide_winner(player, comp)
    if result == 'tie':
        print("It's a tie. No points awarded. Try again.")
        return 0, 0, True
    elif result == 'player':
        print("You win this round! ✅")
        return 1, 0, True
    else:
        print("Computer wins this round. ❌")
        return 0, 1, True


def play_game():
    print("\nWelcome to Rock-Paper-Scissors (Best of Five)! First to 3 wins.")
    player_score = 0
    computer_score = 0
    round_no = 1

    try:
        while player_score < 3 and computer_score < 3:
            p_point, c_point, valid = play_round(round_no)
            if not valid and p_point == 0 and c_point == 0:
                # Player chose to quit or gave invalid input; stop the game
                break
            # Only increment scores when a valid round occurred (ties also count as a played round but with no points)
            # We increase round number for every attempt (including ties) so player sees progress
            round_no += 1
            player_score += p_point
            computer_score += c_point
            print(f"Score -> You: {player_score}  Computer: {computer_score}")

        if player_score > computer_score:
            print("\n You won the game! Congratulations!")
        elif computer_score > player_score:
            print("\n Computer won the game. Better luck next time!")
        else:
            print("\nGame ended before completion.")

    except KeyboardInterrupt:
        print("\nInterrupted. Goodbye!")


if __name__ == '__main__':
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != 'y':
            print("Thanks for playing — goodbye!")
            break
