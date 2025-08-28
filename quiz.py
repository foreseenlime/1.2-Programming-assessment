# function imports
import random
import os
import sys
import time


# set the right clear command for the platform
if sys.platform in ("linux", "darwin"):
    CLEAR = "clear"
elif sys.platform == "win32":
    CLEAR = 'cls'
else:
    exit(1)

# clear the terminal
def clear_terminal() -> None:
    os.system(CLEAR)

clear_terminal()

# DICTIONARY IMPORTANT:::
# identify what language feature is being shown!!!!!
# e.g:
# What language feature is this:
# “The car’s tires screeched as she slammed on the brakes.”
# (answer = onomatapoea)
# correct!!!!

# Choose subject function
# take 'subject' as a argument
# return the neccesary list depending on what subject was chosen
# e.g. if subject was english, return list for english questions and answers

def pick_subject(subject:str):

    if subject == "english":

        return [
            "The car's tires screeched as she slammed on the brakes.",
            "This is a pivotal time to produce policy to protect our planet.",
            "What is the most important thing in the world? It is people, it is people, it is people.",
            "He took my pride and my dignity and my hope and my money. He needed to be punished.",
            "The wind whispered through the lonely house.",
            "He was her lighthouse in the storm.",
            "Her hair was like silk.",
            "The shirt was handed down \nTo me by my brother",
            "The scent of pine was carried on the wind; the trees moved from side to side beneath the warm sun.",
            "He felt so guilty; he took a shower hot enough to burn his skin off.",
            "Before you judge me, think — what would you have done in that situation?"
        ], [
            "onomatopoeia",
            "alliteration",
            "repetition",
            "listing",
            "personification",
            "metaphor",
            "simile",
            "enjambment",
            "sensorylanguage",
            "hyperbole",
            "rhetoricalquestion"
        ]

    # this return message is just so that it doesn't get errors when calling this
    return [],[]


# maybe have dictionary with question and answer in key and entry??
# no i think it will be easier to just have a seperate answer and question key

def calc_score(time:float, points:int) -> int:
    # divide time by points
    # this rewards higher points and lower time with a higher overral score
    # points is multiplied by 1000 to make a better looking score instead of just 0.4 or something
    # time has +1 so it doesnt divide by 0
    score = (points * 1000) / (time + 1)
    score = round(score)
    return score


# main game function
# this is where the user will be prompted with a question and needs to answer
# create a new list with randomized order
# print(questions[x])
# if answers[x] == answer:
# print(YES!!!)
# else: 
# print(no....)
# print(correct answer)

def quiz(questions, answers):

    # loop list for however many items are in it at the beginning
    for i in range(0, len(questions)):

        # get a random element in the current list
        number = random.randint(0, (len(questions) - 1))
        print(questions[number])
        
        answer = input(">>> ")

        # remove whitespace and uppercase letters before checking
        answer = answer.lower()
        answer = answer.strip()
        
        # if input matches the question, correct
        if answer == answers[number]:
            print("\nCorrect\n")

        # if not, incorrect
        else:
            print(f"\nIncorrect, the answer was {answers[number]}\n")

        # remove that element from the list so it doesn't get repeated
        questions.remove(questions[number])
        answers.remove(answers[number])

        # this will loop till all of the questions in the list have been asked


quiz(["q1", "q2", "q3", "q4", "q5"], ["a1", "a2", "a3", "a4", "a5"])

# start menu function
# ask what name is (this probably will be useless though)
# what subject will you do the quiz for
# call choose subject function for the right list of questions and answers
# call main quiz function with question and answers as argument

# after game is finished, call calculate score function and return it to main loop

# choose difficulty for timed run ???


# main loop/end menu
# have score variable set to call start menu function since it will return score once finished
# print the player's score back to them 
# ask the player if they want to play again


# TESTING AREA---------------------------------------------------------------
# LEAVE THIS AT THE BOTTOM

# listlist = [
#     "question1",
#     "question2",
#     "question3",
#     "question4",
#     "question5"
# ]

# removed = 1

# looplist = []

# create new changable list

# for i in range(0, len(listlist)):
#     looplist.append(listlist[i])


# print random item in list + remove it so it doesnt get repeated
# this goes for the entire length of the list, so everything gets 
# printed in a random order

# this is how it will print a random order of questions in the main quiz
# it needs to do this instead of just using list.shuffle() because this will
# have the questions and answers in the same order, instead of both being random
# this is important because none of the questions will line up with the answers
# if we just shuffled both


# for i in range(0, len(listlist)):
#     length = (len(listlist) - removed)

#     number = random.randint(0, length)

#     print(looplist[number])

#     looplist.remove(looplist[number])

#     removed += 1


# clear terminal at end so terminal is kept tidy
clear_terminal()