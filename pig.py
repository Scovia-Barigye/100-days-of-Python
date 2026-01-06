import random

def roll():
    roll = random.randint(1,6)
    return roll

while True:
    players=input("Enter the number of players(3-6):")
    if players.isdigit():
        players=int(players)
        if 3<=players<=6:
            break
        else:
            print("Must be between 3-6 players.")
    else:
        print("invalid try again.")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer", player_idx +1 , "turn has just started!\n")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("would you like to roll (y) for yes :")
            
            if should_roll != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)

            print("Your score is:", current_score)

        player_scores[player_idx] += current_score
        print("Your total score is:", player_scores[player_idx])

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1,
      "is the winner with a score of:", max_score)
