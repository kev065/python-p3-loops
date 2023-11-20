#!/usr/bin/env python3

def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -=1
        print("Happy New Year!")



def square_integers(int_list):
    squared_list = []
    for num in int_list:
        squared = num * num
        squared_list.append(squared)
    return squared_list



def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0: # starts a for loop that iterates over the numbers from 1 to 100
            print("FizzBuzz") 
        elif number % 3 == 0:
            print("Fizz") 
        elif number % 5 == 0:
            print("Buzz") 
        else:
            print(number) 
