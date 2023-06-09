import time
import requests
# importing the unquote module since we'll use the url encoding from Trivia API
# unquote will make the output requests human-readable
from urllib.parse import unquote
import random


def greet_user(greetings_state):
    delay = 0.01
    print("")
    for i in greetings_state:
        print(i, end="")
        time.sleep(delay)

    print(
        "\n\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Code in Place Grand Geography "
        "Quiz>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


def user_qstn_set():
    question_num = input("\nPlease choose the number of quiz questions, from 1 to 50, you want to be be asked: ")
    question_diff = input("\nPlease your preffered difficulty level(choose one of: hard, medium, easy, or random.) "
                          "\n\t Your choice:  ")
    return question_num, question_diff.lower()


def streak_list(num_of_qstns, result):
    global streak
    tick = "✔️"
    cross = "❌"
    if result == "correct":
        state = tick
    else:
        state = cross

    for i in range(len(streak)):
        if streak[i] == " __ ":
            streak[i] = state
            break
    print("Your streak: ", end="")
    for x in streak:
        print(x, end=" ")

    print("")


name = input("Please enter your name: ")

while len(name) == 0:
    print("You did not enter a name. Re-running the program....")
    name = input("Please enter your name: ")

greeting = f"Hello, {name}! Welcome to the Code in Place Grand Geography Quiz🧠"

greet_user(greeting)
user_set = user_qstn_set()

question_num = int(user_set[0])
count = 0
difficulty = user_set[1]

while question_num <= 0 or question_num > 275:
    print("Please choose a number in the range of 1 to 20")
    question_num = input("Please choose the number of questions, from 1 to 20, you want to be be asked: ")
    question_num = int(question_num.strip())

count = question_num
print(f"\nAlright. Let the games begin. All the best, {name}!")
print()

# initializing the url with number of questions added in
if difficulty == "random":
    url = f"https://opentdb.com/api.php?amount={question_num}&category=22&type=multiple&encode=url3986"
else:
    url = f"https://opentdb.com/api.php?amount={question_num}&category=22&type=multiple&difficulty={difficulty}&encode=url3986"

# obtaining results from the api call
r = requests.get(url)
status_code = r.status_code

# converting results to python dictionary
response_dict = r.json()

response_code = response_dict["response_code"]

if status_code != 200 and response_code != 0:
    print("The game encountered an error. Please contact Lyton, the game developer.")
    exit()

results_list = response_dict['results']

correct = 0
qstn_number = 0
streak = []
for j in range(question_num):
    streak.append(" __ ")

for i in results_list:
    qstn_number += 1
    question = unquote(i['question'])
    print(f"\n\nQuestion number {qstn_number} is: {question}\n")
    choices = [unquote(i['incorrect_answers'][0]), unquote(i['incorrect_answers'][1]),
               unquote(i['incorrect_answers'][2]), unquote(i['correct_answer'])]
    random.shuffle(choices)
    print(f"\tA: {choices[0]}")
    print(f"\tB: {choices[1]}")
    print(f"\tC: {choices[2]}")
    print(f"\tD: {choices[3]}")

    correct_choice = unquote(i['correct_answer'])
    # print(unquote(correct_choice))

    options = ['a', 'b', 'c', 'd']
    a, b, c, d = choices[0], choices[1], choices[2], choices[3]

    user_choice = input("\n\tPlease choose a letter(A, B, C, or D) that best represents your answer: ")
    user_choice = user_choice.strip().lower()

    while user_choice not in options:
        print(f"Hey {name}, you chose an invalid option. Please choose either A, B, C, or D ")
        user_choice = input("\nPlease choose a letter(A, B, C, or D) that best represents your answer: ")
        user_choice = user_choice.strip().lower()

    if user_choice == 'a':
        user_choice = choices[0]
    elif user_choice == 'b':
        user_choice = choices[1]
    elif user_choice == 'c':
        user_choice = choices[2]
    else:
        user_choice = choices[3]

    count -= 1

    if user_choice == correct_choice:
        print(f"\n****Congratulations for getting that right. {correct_choice} is the right answer!****\n")
        correct += 1
        streak_list(question_num, "correct")

    else:
        print(f"\nResult: Oops, wrong choice....... The correct answer is {correct_choice}.\n")
        streak_list(question_num, "incorrect")
    # print(count)
    if count != 0:
        print(f"\nNext question in..", end="")
        for i in range(1, 4):
            i = 4 - i
            print(f"{i}", end="...")
            time.sleep(1)

print("\n#################################################################################################################################")
if correct >= question_num:
    print(f"\nWell done, {name}. You got {correct} out of {question_num} questions correct!")
else:
    print(f"\nLooks like you couldn't do you best today, {name}. You got {correct} out of {question_num} questions correct. \
Better luck next time buddy...")
