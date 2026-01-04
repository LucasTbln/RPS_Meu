import random
from enum import IntEnum
from collections import Counter, deque


class GameAction(IntEnum): #Xogadas posibles
    Rock = 0
    Paper = 1
    Scissors = 2
    Lizard = 3
    Spock = 4


class GameResult(IntEnum):
    Victory = 1
    Defeat = -1
    Tie = 0


last_user_actions = deque(maxlen=5)
all_user_actions = []
last_results = deque(maxlen=5)


def assess_game(user_action, computer_action):

    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")
        result = GameResult.Tie

    elif user_action == GameAction.Rock:
        if computer_action in (GameAction.Scissors, GameAction.Lizard):
            print("Rock crushes scissors/lizard. You won!")
            result = GameResult.Defeat
        else:
            print("Paper or Spock beats rock. You lost!")
            result = GameResult.Victory

    elif user_action == GameAction.Paper:
        if computer_action in (GameAction.Rock, GameAction.Spock):
            print("Paper covers rock or disproves Spock. You won!")
            result = GameResult.Defeat
        else:
            print("Scissors or lizard beats paper. You lost!")
            result = GameResult.Victory

    elif user_action == GameAction.Scissors:
        if computer_action in (GameAction.Paper, GameAction.Lizard):
            print("Scissors cuts paper or decapitates lizard. You won!")
            result = GameResult.Defeat
        else:
            print("Rock or Spock beats scissors. You lost!")
            result = GameResult.Victory

    elif user_action == GameAction.Lizard:
        if computer_action in (GameAction.Spock, GameAction.Paper):
            print("Lizard poisons Spock or eats paper. You won!")
            result = GameResult.Defeat
        else:
            print("Rock or scissors beats lizard. You lost!")
            result = GameResult.Victory

    elif user_action == GameAction.Spock:
        if computer_action in (GameAction.Scissors, GameAction.Rock):
            print("Spock smashes scissors or vaporizes rock. You won!")
            result = GameResult.Defeat
        else:
            print("Paper or lizard beats Spock. You lost!")
            result = GameResult.Victory

    last_user_actions.append(user_action)
    all_user_actions.append(user_action)
    last_results.append(result)

    return result


def counter_action(action):

    counters = { #A que lle gaá cada xogada
        GameAction.Rock: [GameAction.Paper, GameAction.Spock],
        GameAction.Paper: [GameAction.Scissors, GameAction.Lizard],
        GameAction.Scissors: [GameAction.Rock, GameAction.Spock],
        GameAction.Lizard: [GameAction.Rock, GameAction.Scissors],
        GameAction.Spock: [GameAction.Paper, GameAction.Lizard]
    }

    return random.choice(counters[action])


def get_computer_action():

    if random.random() < 0.25:
        action = GameAction(random.randint(0, len(GameAction) - 1))
        print(f"Computer picked {action.name} (random).")
        return action

    if len(last_results) == 5:
        defeats = last_results.count(GameResult.Defeat)
        victories = last_results.count(GameResult.Victory)
        ties = last_results.count(GameResult.Tie)

        if defeats > victories + ties:
            common_action = Counter(all_user_actions).most_common(1)[0][0]
            action = counter_action(common_action)
            print(f"Computer picked {action.name} (counter-most-used).")
            return action

    if len(last_user_actions) >= 2:
        if last_user_actions[-1] == last_user_actions[-2]:
            action = counter_action(last_user_actions[-1])
            print(f"Computer picked {action.name} (anti-repeat).")
            return action

    if last_user_actions:
        common_action = Counter(last_user_actions).most_common(1)[0][0]
        action = counter_action(common_action)
        print(f"Computer picked {action.name} (strategy).")
        return action

    action = GameAction(random.randint(0, len(GameAction) - 1))
    print(f"Computer picked {action.name}.")
    return action
