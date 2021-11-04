import random

print("---Game--- | 1 - Rock | 2 - Scissors | 3 - Paper")

while True:
    apponent = random.randint(1, 3)
    if apponent == 1:
        choice = "Rock"
    elif apponent == 2:
        choice = "Scissors"
    else:
        choice = "Paper"

    try:
        number = input("Enter a number or 'q' to exit: ")
        if number == "q":
            print("End of the program.")
            break

        number = int(number)
        if number == 1:
            print("Your choice: Rock")
            print(f"Opponent choice: {choice}")
            if apponent == 1:
                print("Draw.")
            elif apponent == 2:
                print("You win!")
            else:
                print("Opponent win!")
        elif number == 2:
            print("Your choice: Scissors")
            print(f"Opponent choice: {choice}")
            if apponent == 1:
                print("Opponent win!")
            elif apponent == 2:
                print("Draw.")
            else:
                print("You win!")
        else:
            print("Your choice: Paper")
            print(f"Opponent choice: {choice}")
            if apponent == 1:
                print("You win!")
            elif apponent == 2:
                print("Opponent win!")
            else:
                print("Draw.")
    except ValueError:
        print("Error!")
