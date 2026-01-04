import random
from enum import IntEnum


class GameAction(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4


class GameResult(IntEnum):
    Victory = 1   # Computadora gana
    Defeat = -1   # Computadora pierde
    Tie = 0       # Empate


# Diccionario con regras de a que lle gana cada xogada
WIN_RULES = {
    GameAction.Rock: [GameAction.Scissors, GameAction.Lizard],
    GameAction.Paper: [GameAction.Rock, GameAction.Spock],
    GameAction.Scissors: [GameAction.Paper, GameAction.Lizard],
    GameAction.Lizard: [GameAction.Spock, GameAction.Paper],
    GameAction.Spock: [GameAction.Scissors, GameAction.Rock],
}


def assess_game(user_action, computer_action):

    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")
        return GameResult.Tie

    elif computer_action in WIN_RULES[user_action]: #Comproba se está nas regras de victoria
        print(f"{user_action.name} beats {computer_action.name}. You won!")
        return GameResult.Defeat  # Computadora perde

    else:
        print(f"{computer_action.name} beats {user_action.name}. You lost!")
        return GameResult.Victory  # Computadora gana


def get_computer_action():
    computer_selection = random.randint(0, len(GameAction) - 1)
    computer_action = GameAction(computer_selection)
    print(f"Computer picked {computer_action.name}.")
    return computer_action


def get_user_action():
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    while True:
        try:
            user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
            return GameAction(user_selection)
        except (ValueError, IndexError):
            print(f"Invalid selection. Pick a number between 0 and {len(GameAction)-1}!")


def play_another_round():
    another_round = input("\nAnother round? (y/n): ")
    return another_round.lower() == 'y'


def main():
    while True:
        user_action = get_user_action()
        computer_action = get_computer_action()
        assess_game(user_action, computer_action)

        if not play_another_round():
            break


if __name__ == "__main__":
    main()
