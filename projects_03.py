import random
emojis = {"r": "✊", "p": "✋", "s": "✌️"}
choion = ("r", "p", "s")
while True:
    nadim = input("Enter your choice (r for rock, p for paper, s for scissors : ").lower()
    if nadim not in choion:
        print("Invalid choice! Please choose r, p, or s.")
        continue

    computer = random.choice(choion)

    print(f"Computer chose: {emojis[computer]}")
    print(f"Nadim chose: {emojis[nadim]}")

    if nadim == computer:
        print("Tie!")
    elif (
        (nadim == "r" and computer == "s") or \
        (nadim == "p" and computer == "r") or \
        (nadim == "s" and computer == "p")):
        print("Nadim wins!")
    else:
        print("You lose!")

    should_play_again = input("Do you want to play again? (y/n): ").lower()
    if should_play_again == "n":
        break
    #https://youtu.be/yVl_G-F7m8c?si=wBXpR8tKLkP7mrn-
