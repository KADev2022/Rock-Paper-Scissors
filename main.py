import random

l = ['Rock', 'Paper', 'Scissors']
player = False

# While player is false, continue the loop
while player == False:
    computer = random.choice(l)

    print("\nChoose anything from here")
    ply = input('Rock Paper Scissors -> ')
    print("Player chose:", ply)
    print("Computer chose:", computer)

    # If the computer AI is same as player then the match is drawn
    if computer == ply:
        print("Match is draw.......")
    # Else do you want to continue or not if player or computer won the match
    else:
        if computer == 'Rock':
            # If computer AI chooses rock and player chooses paper, then player won the match
            if ply == 'Paper':
                print("Player won the match")
            # If computer AI chooses rock and player chooses scissors, then computer won the match
            else:
                print("Computer won the match")
        elif computer == 'Paper':
            # If computer AI chooses paper and player chooses scissors, then player won the match
            if ply == 'Scissors':
                print("Player won the match")
            # If computer AI chooses paper and player chooses rock, then computer won the match
            else:
                print("Computer won the match")
        elif computer == 'Scissors':
            # If computer AI chooses scissors and player chooses paper, then computer won the match
            if ply == 'Paper':
                print("Computer won the match")
            # If computer AI chooses scissors and player chooses rock, then player won the match
            else:
                print("Player won the match")

    # This will prompt the user to choose y (Yes) or n (No) if they want to continue the game or not
    # If user chooses 'y', then the game continue or if user choose 'n', then game stops
    ch = input("Do you want to continue or not? y/n")
    if ch == 'n':
        player = True
