import random

pc_num = random.randint(1, 100)

user_num = ""

while user_num != "correct":
    try:
        choice = int(input("Guess the number: "))
        if choice > 100:
            print("Number too high - please enter a number in range 1-100")
        elif choice < 1:
            print("Number too low - please enter a number in range 1-100")
        elif choice > pc_num:
            print("Too big!")
        elif choice < pc_num:
            print("Too small!")
        elif choice == pc_num:
            print("You win!")
            user_num = "correct"
    except Exception:
        print("ValueError - please enter a number in range 1-100")


