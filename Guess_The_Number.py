# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 01:14:09 2019

@author: Mudassir Kidwai
"""

import random

print("GUESS THE NUMBER")

#Initialization the guess numvber
guess = 0

#using random number
hiddenNumber = random.randrange(1, 10)
print("Select number between 1-10")
#print(hiddenNumber)

#while the guess does not hit do this
while (hiddenNumber != guess):
    guess = int(input("Please enter your guess: "))

    if guess == hiddenNumber:
        print("Hit!")
    elif guess < hiddenNumber:
        print("Your guess is too low")
    else:
        print("Your guess is too high")