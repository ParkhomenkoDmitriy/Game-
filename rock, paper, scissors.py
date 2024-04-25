import random

options = ["камень", "ножницы", "бумага"]

player_wins = 0
computer_wins = 0
draw = 0


def determine_winner(player, computer):
    if player == computer:
        return "ничья"
    elif (player == "камень" and computer == "ножницы") or \
            (player == "ножницы" and computer == "бумага") or \
            (player == "бумага" and computer == "камень"):
        return "игрок"
    else:
        return "компьютер"


while True:
    player_choice = input("Выберите камень, ножницы или бумага (или 'выход', чтобы закончить): ").lower()

    if player_choice == "выход":
        break

    if player_choice not in options:
        print("Неверный выбор. Попробуйте снова.")
        continue

    computer_choice = random.choice(options)

    winner = determine_winner(player_choice, computer_choice)

    if winner == "ничья":
        draw += 1
        print(f"Ничья! Вы оба выбрали {player_choice}.")
    elif winner == "игрок":
        player_wins += 1
        print(f"Вы выиграли! Вы выбрали {player_choice}, а компьютер выбрал {computer_choice}.")
    else:
        computer_wins += 1
        print(f"Компьютер выиграл! Вы выбрали {player_choice}, а компьютер выбрал {computer_choice}.")

print(f"Игра окончена. Счет: Игрок - {player_wins}, Компьютер - {computer_wins}, Ничья - {draw}")
