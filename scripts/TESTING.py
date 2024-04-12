import random

colors = ["Y", "G", "B", "R", "P", "W"]
pc_answer = []
right_count = 0
exist_count = 0
lives = 8

for i in range(4):
    random_color = random.choice(colors)
    pc_answer.append(random_color)

while lives > 0:

    pc_answer_copy = pc_answer[:]

    user_input = input("Guess 4 colors: ").upper()

    list_of_guesses = list(user_input)

    # print(f"pc: {pc_answer}")
    print(f"input: {list_of_guesses}")

    list_of_guesses = list(user_input)

    for i in range(4):
        if list_of_guesses[i] == pc_answer[i]:
            right_count += 1
            pc_answer_copy.remove(list_of_guesses[i])
    
    if right_count == 4:
        print(f"you guessed it: {list_of_guesses} was the answer!")
        break

    for i in range(4):
        if list_of_guesses[i] in pc_answer_copy and list_of_guesses[i] != pc_answer[i]:
            exist_count += 1
            pc_answer_copy.remove(list_of_guesses[i])

    lives -= 1

    print(f"Right place: {right_count} | wrong place: {exist_count}")
    right_count = 0
    exist_count = 0
    print(f"Lives left : {lives}")

    if lives == 0:
        print("You Lost")
        print(f"The answer was: {pc_answer}")
