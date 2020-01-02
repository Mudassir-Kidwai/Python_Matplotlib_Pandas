# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 23:43:41 2019

@author: Mudassir Kidwai
"""
from nltk.corpus import words

string = "arabicwordthisis"
tokens = []
lowercaseCorpus = [x.lower() for x in words.words()]
i = 0

while i < len(string):
    maxWord = ""
    for j in range(i, len(string)):
        tempWord = string[i:j+1]
        if tempWord in lowercaseCorpus and len(tempWord) > len(maxWord):
            maxWord = tempWord
    i = i+len(maxWord)
    tokens.append(maxWord)

print(tokens)