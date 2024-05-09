import random

def get_user_input():
    while True:
        try:
            user_input = int(input("Enter runs (1-6): "))
            if user_input < 1 or user_input > 6:
                print("Invalid input! Please enter a number between 1 and 6.")
                continue
            return user_input
        except ValueError:
            print("Invalid input! Please enter a number.")

def play_hand_cricket():
    user_total = 0
    comp_total = 0
    innings = 1

    print("Welcome to Hand Cricket!")
    while True:
        print(f"\nInnings {innings}: Your turn to bat.")
        while True:
            user_runs = get_user_input()
            comp_runs = random.randint(1, 6)
            print(f"Computer bowled: {comp_runs}")

            if user_runs != comp_runs:
                user_total += user_runs
                print(f"Your total: {user_total}")
            else:
                print("Out! Your innings is over.")
                break

    print(f"\nInnings {innings}: Computer's turn to bat.")
    while True:
        comp_runs = random.randint(1, 6)
        user_runs = get_user_input()
        print(f"You bowled: {user_runs}")

        if user_runs != comp_runs:
            comp_total += comp_runs
            print(f"Computer's total: {comp_total}")
        else:
            print("Out! Computer's innings is over.")
            break

    innings += 1

    if innings > 2:
        if user_total > comp_total:
            print("\nCongratulations! You win!")
        elif user_total < comp_total:
            print("\nComputer wins!")
        else:
            print("\nIt's a tie!")

if __name__ == "__main__":
    play_hand_cricket()