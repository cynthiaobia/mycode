#!/usr/bin/env python 3

userInput = input("pick a number ") # prompt for number
i = 1 # initialize

while (i <= int(userInput)):
    if ((i%3 == 0) and (i%5 == 0)):
        print("FizzBuzz")
    elif (i%3 == 0):
        print("Fizz")
    elif (i%5 == 0):
        print("Buzz")
    else:
        print(userInput)
    i += 1

