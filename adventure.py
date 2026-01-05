#this game has a potiential of growing into a larger adventure game but for now we will keep it simple and portray our python loops and nested loops skills.
answer = input("you are in a dark room with two doors. do you want to go through door 1 or door 2? type 1 or 2: ")
if answer == "1":
    print("there is a giant bear here eating a cheese cake and you are next. you lose!")
    quit()
elif answer == "2":
    answer = input("you enter a room full of fire. do you want to (1) try to run through it or (2) go back? type 1 or 2: ")
    if answer == "1":
        print("you are burned to a crisp. you lose!")
        quit()
    elif answer == "2":
        answer = input("you are back at the first room. do you want to go through door 1 or door 2? type 1 or 2: ")
        if answer == "1":
            print("there is a giant bear here eating a cheese cake and you are next. you lose!")
            quit()
        elif answer == "2":
            print("you enter a room full of fire. do you want to (1) try to run through it or (2) go back? type 1 or 2: ")
            answer = input("you are back at the first room. do you want to go through door 1 or door 2? type 1 or 2: ")
            if answer == "1":
                print("there is a giant bear here eating a cheese cake and you are next. you lose!")
                quit()
            elif answer == "2":
                print("you enter a room full of fire. do you want to (1) try to run through it or (2) go back? type 1 or 2: ")
                print("you are stuck in an endless loop of fire and bears. you lose!")
                quit()
            else:
                print("not a valid option. you lose!")
                quit()
        else:
            print("not a valid option. you lose!")
            quit()
    else:
        print("not a valid option. you lose!")
        quit()