import random
print("welcome to rock, paper,scissors!\nThe rules are simple:\nrock beats scissors,scissors beats paper,paper beats rock.end the game anytime by typing Q")

user_wins = 0;
computer_wins = 0;
options = ["rock", "paper", "scissors"]

while True:
 user_choice = input("Type rock/paper/scissors or Q to quit: ").lower()
 if user_choice == "q":
     break
 if user_choice not in options:
     print("input is not valid")
     continue
 random_number = random.randint(0,2)
 computer_choice = options[random_number]
 print("computer picked " + computer_choice + ".")
 if user_choice == computer_choice:
     print("it's a tie")
     user_wins +=1
     computer_wins +=1
 elif(user_choice == "rock" and computer_choice =="scissors" ) or (user_choice =="paper" and computer_choice =="rock") or (user_choice =="scissors" and computer_choice =="paper"):
    print("you win!")
    user_wins +=1
    continue
 else:
    print("computer wins!")
    computer_wins +=1 
    continue
print("you have " +str(user_wins) +" wins.")
print("computer has " +str(computer_wins) +" wins.")