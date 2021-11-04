import random


def game():
    number = random.randint(1, 100)

    userNumber = None
    count = 0
    levels = {1: 10, 2: 5, 3: 3}
    level = int(input('Выберите уровень сложности: '))
    maxCount = levels[level]
    userCount = int(input('Введите кол-во пользователей: '))
    users = []

    for i in range(userCount):
        userName = input(f'Введите имя {i}: ')
        users.append(userName)

    isWinner = False
    winnerName = None

    while not isWinner:
        count += 1
        if count > maxCount:
            print('Вы проиграли.')
            break
        print(f'Попытка № {count}')
        for user in users:
            print(f'Ход пользователя {user}')
            userNumber = int(input('Введите число: '))
            if userNumber == number:
                isWinner = True
                winnerName = user
                break
            elif number < userNumber:
                print('Ваше число больше загаданного')
            else:
                print('Ваше число меньше загаданного')
    else:
        print(f'Победитель {winnerName}')


if __name__ == '__main__':
    game()
