# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 00:28:08 2020

@author: Mudassir Kidwai
"""
#FACTORIAL
def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)
    
a = factorial(3)
#print("factorial: ", a)

#PRIME NUMBERS
lower=11
upper=25
for num in range(lower, upper + 1):
    # all prime numbers are greater than 1
    if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           num

#FABONACCI
def fabonacci(n):
    if n<=1:
        return n
    else:
        return (fabonacci(n-1) + fabonacci(n-2))
    
for i in range(10):
    print(fabonacci(i))
    
#Palindrome String 
x = "CIVIC"
w = "" 
for i in x: 
    w = i + w 
    if (x==w): 
        print("YES") 