#!/usr/bin/env python3
"""
Final Project
Expanded on reading data mini project
Trivia question game utilizing APIs, JSON, functions, and dictionaries
"""

import random
import requests

URL = "http://opentdb.com/api.php?amount=10"

trivia_questions = requests.get(URL)
trivia_questions = trivia_questions.json()
all_questions = trivia_questions['results']

print("Let's play trivia!\n")
# display q & a, prompt for user answer, compare answers, get score
def display_question():
    # tally correct answers by user in a single game
    num_correct = 0
    # tally the total number of questions in a single game
    total_num = len(all_questions)
    # enumerate questions starting at index 1
    question_num = 1

    # form each question as a dictionary
    for question_set in all_questions:
        question = question_set['question']
        all_answers = question_set['incorrect_answers']
        all_answers += [question_set['correct_answer']]
        random.shuffle(all_answers)
        correct_answer = question_set['correct_answer']
        choices = ['a', 'b', 'c', 'd']
        let_and_ans = []
        answers = {}
        i = 0
        
        # display answers in format a. answer, b. answer, etc...
        print(f"{question_num}. {question}")
        for answer in all_answers:
            let_and_ans = [choices[i], answer]
            answers[let_and_ans[1]] = let_and_ans[0]
            print(f"{let_and_ans[0]}. {let_and_ans[1]}")
            i += 1
        # prompt user for answer
        user_answer = input()

        # compare user answer to correct answer and keep score
        if user_answer == answers[correct_answer]:
            print("Yes, that's correct!\n")
            num_correct += 1
            question_num += 1
        else:
            print(f"Sorry, the correct answer is: {correct_answer}\n")
            question_num += 1

    # end game 
    print("Game over.")
    print(f"You got {num_correct} out of {total_num} correct.")
    return num_correct

def main():
    display_question()

if __name__ == "__main__":
    main()

# edit variable names
# add comments
# define more functions
# fix characters
# bonus. keep looping for new game
# track highest score