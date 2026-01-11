import random
from enum import IntEnum
from collections import Counter, deque


class GameAction(IntEnum): #Acción posibles
    Rock = 0
    Paper = 1
    Scissors = 2


class GameResult(IntEnum):
    Victory = 1   # Computadora gana
    Defeat = -1   # Computadora perde
    Tie = 0       # Empate


# Memoria da partida
last_user_actions = deque(maxlen=5)   # últimas 5 xogadas do usuario
all_user_actions = []                 # tódalas xogadas do usuario
last_results = deque(maxlen=5)        # últimos 5 resultados


#Lóxica do xogo. Dependendo do que saque o usuario e a computadora, perde, gaña ou empata

def assess_game(user_action, computer_action):

    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")
        result = GameResult.Tie #Máquina empata

    elif user_action == GameAction.Rock:
        if computer_action == GameAction.Scissors:
            print("Rock smashes scissors. You won!")
            result = GameResult.Defeat #Máquina perde
        else:
            print("Paper covers rock. You lost!")
            result = GameResult.Victory #Máquina gaña

    elif user_action == GameAction.Paper:
        if computer_action == GameAction.Rock:
            print("Paper covers rock. You won!")
            result = GameResult.Defeat
        else:
            print("Scissors cuts paper. You lost!")
            result = GameResult.Victory

    elif user_action == GameAction.Scissors:
        if computer_action == GameAction.Rock:
            print("Rock smashes scissors. You lost!")
            result = GameResult.Victory
        else:
            print("Scissors cuts paper. You won!")
            result = GameResult.Defeat

    # Garda memoria
    last_user_actions.append(user_action) #Engade á lista de accións total
    all_user_actions.append(user_action) #Engade á lista de 5 últimas accións
    last_results.append(result) #Engade á lista dos 5 últimos resultados

    return result #Devolta o resultado da xogada


def counter_action(action):
    #Devolta a acción que lle gana á dada
    if action == GameAction.Rock:
        return GameAction.Paper
    if action == GameAction.Paper:
        return GameAction.Scissors
    return GameAction.Rock


def get_computer_action():

    if random.random() < 0.25: #25% de probabilidades de que xogue algo aleatorio en vez do planeado
        action = GameAction(random.randint(0, len(GameAction) - 1))
        print(f"Computer picked {action.name} (random).")
        return action

    if len(last_results) == 5: #Se xa hai 5 resultados que sacar
        defeats = last_results.count(GameResult.Defeat)
        victories = last_results.count(GameResult.Victory)
        ties = last_results.count(GameResult.Tie)

        if defeats > victories + ties: #Se nas últimas 5 xogadas perde máis do que empata e gaña
            common_action = Counter(all_user_actions).most_common(1)[0][0] #Garda a xogada máis usada do usuario
            action = counter_action(common_action) #Xoga a contra da acción máis usada
            print(f"Computer picked {action.name} (counter-most-used).")
            return action

    if len(last_user_actions) >= 2: 
        if last_user_actions[-1] == last_user_actions[-2]:# Se o usuario xogou o mesmo dúas veces
            action = counter_action(last_user_actions[-1])
            print(f"Computer picked {action.name} (anti-repeat).") # Xoga a contra desa xogada
            return action

    if last_user_actions: 
        common_action = Counter(last_user_actions).most_common(1)[0][0] # Xogada máis usada das últimas 5 xogadas
        action = counter_action(common_action) #Usa a contra
        print(f"Computer picked {action.name}.")
        return action

    action = GameAction(random.randint(0, len(GameAction) - 1))
    print(f"Computer picked {action.name}.")
    return action #Devolta a xogada feita

def get_user_action():
    game_choices = [f"{g.name}[{g.value}]" for g in GameAction]
    choice_str = ", ".join(game_choices)
    user_selection = int(input(f"\nPick a choice ({choice_str}): "))
    return GameAction(user_selection)


def play_another_round():
    return input("\nAnother round? (y/n): ").lower() == 'y'


def main():
    while True:
        try:
            user_action = get_user_action()
        except ValueError:
            print(f"Invalid selection. Pick a choice in range [0, {len(GameAction) - 1}]!")
            continue

        computer_action = get_computer_action()
        assess_game(user_action, computer_action)

        if not play_another_round():
            break


if __name__ == "__main__":
    main()
