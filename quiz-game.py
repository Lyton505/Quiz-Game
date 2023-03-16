import requests
#importing the unquote module since we'll use the url encoding from Trivia API
#unquote will make the output requests human-readable
from urllib.parse import unquote
import random

name = input("Please enter your name: ")

while len(name) == 0:
    print("You did not enter a name. Re-running the program....")
    name = input("Please enter your name: ")

print(f"\n\tHello, {name}! Welcome to the Kibo Grand Geography Quiz🧠")

print("\n################################Kibo Grand Geography Quiz#######################################################")

question_num = input("\nPlease choose the number of quiz questions, from 1 to 275, you want to be be asked: ")

question_num = int(question_num.strip())
count = 0

while question_num <= 0 or question_num > 275:
    print("Please choose a number in the range of 1 to 20")
    question_num = input("Please choose the number of questions, from 1 to 20, you want to be be asked: ")
    question_num = int(question_num.strip())

count = question_num
print(f"Alright. Let the games begin. All the best, {name}!")
print(f"pssst....Hey {name} we won't make it too hard for you. We promise ;-)")
print()

#initializing the url with number of questions added in
url = "https://opentdb.com/api.php?amount={}&category=22&type=multiple&encode=url3986".format(question_num)

#obtaining results from the api call
r = requests.get(url)

status_code = r.status_code

#converting results to python dictionary
response_dict = r.json()

response_code = response_dict["response_code"]

if status_code != 200 and response_code != 0:
    print("The game encountered an error. Please contact Lyton, the game developer.")
    exit()


results_list = response_dict['results']

correct = 0
qstn_number = 0

#print(results_list)

for i in results_list:
    qstn_number += 1
    question = unquote(i['question'])
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    print(f"\nQuestion number {qstn_number} is: {question}\n")
    choices = [unquote(i['incorrect_answers'][0]),unquote(i['incorrect_answers'][1]), unquote(i['incorrect_answers'][2]), unquote(i['correct_answer']) ]
    random.shuffle(choices)
    print(f"\tA: {choices[0]}")
    print(f"\tB: {choices[1]}")
    print(f"\tC: {choices[2]}")
    print(f"\tD: {choices[3]}")

    correct_choice = unquote(i['correct_answer'])
    #print(unquote(correct_choice))
    
    options = ['a', 'b', 'c', 'd']
    a, b, c, d = choices[0], choices[1], choices[2], choices[3]

    user_choice = input("\nPlease choose a letter(A, B, C, or D) that best represents your answer: ")
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
    else:
        print(f"\nResult: Ooops, wrong choice....... The correct answer is {correct_choice}.\n")
    
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    

    if count != 0:
        quit_continue = input("\nPress q(followed by ENTER) to quit, or any other letter(followed by ENTER) to continue")
        if quit_continue == 'q':
            break
        else:
            continue

if correct >= question_num:
    print(f"\nWell done, {name}. You got {correct} out of {question_num} questions correct!")
else:
    print(f"\nLooks like you couldn't do you best today {name}. You got {correct} out of {question_num} questions correct. \
Better luck next time buddy...")

       