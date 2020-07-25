import random

username = input("Enter your name: ")
print(f"Hello, {username}")

score = 0

with open("rating.txt", "r") as f:
    lines = f.readlines()
    for l in lines:
        if str(username) in l:
            score = int(str([int(i) for i in str(l).split() if i.isdigit()]).strip("[]"))

print("Okay, let's start")

default_options = ["rock", "paper", "scissors"]
options = input().split(",")

if options == [""]:
     options = default_options

while True:
    user = input()
    computer = random.choice(options)

    lost_msg = f"Sorry, but computer chose {computer}"
    won_msg = f"Well done. Computer chose {computer} and failed"
    draw_msg = f"There is a draw ({computer})"

    if user in options:
        list_without = (options[options.index(user) + 1:]) + (options[:options.index(user)])
        loser_list = list_without[:(len(list_without) // 2)]
        winner_list = list_without[(len(list_without) // 2):]

        if computer == user:
            print(draw_msg)
            score += 50
        elif computer in loser_list:
            print(lost_msg)
        elif computer in winner_list:
            print(won_msg)
            score += 100

    else:
        if user == "!rating":
            print(f"Your rating: {score}")
        elif user == "!exit":
            with open("rating.txt", "a+") as f:
                tofile = f"{username} {score}\n"
                f.write(tofile)
                f.close()
            print("Bye!")
            exit()
        else:
            print("Invalid input")
