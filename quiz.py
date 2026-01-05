print("Welcome to my quiz!")

answer = input("do you want to play? (yes/no): ").lower()
if answer != "yes":
    print("Maybe next time!");
    quit();
else:
    print ("let's play!");

score=0;
    
answer =input("what does the CPU stand for? ").lower()
if answer == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer =input("what does the GUI stand for? ").lower()
if answer == "graphical user interface":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer =input("what does the PSU stand for? ").lower()
if answer == "power supply":
    print("correct!")
    score += 1
else:
    print("incorrect!")

answer =input("what does the RAM stand for? ").lower()
if answer == "random access memory":
    print("correct!") 
    score += 1
else:
    print("incorrect!")
    
print("You got " +str(score) + " questions correct!")
print("You got " +str((score/4)*100) + "%.")