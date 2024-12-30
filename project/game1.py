import random

def game():
    user_choice = input("Выберите: камень, ножницы или бумага? ").lower()
    actions = ["камень", "ножницы", "бумага"]
    computer_choice = random.choice(actions)

    print(f"\nВы выбрали {user_choice}, компьютер выбрал {computer_choice}.\n")

    if user_choice == computer_choice:
        print("Ничья!")
    elif user_choice == "камень":
        if computer_choice == "ножницы":
            print("Вы выиграли!")
        else:
            print("Компьютер выиграл!")
    elif user_choice == "ножницы":
        if computer_choice == "бумага":
            print("Вы выиграли!")
        else:
            print("Компьютер выиграл!")
    elif user_choice == "бумага":
        if computer_choice == "камень":
            print("Вы выиграли!")
        else:
            print("Компьютер выиграл!")

print("Добро пожаловать в игру 'Камень, ножницы, бумага'!")

while True:
    game()
    play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
    if play_again != "да":
        break

print("Спасибо за игру!")