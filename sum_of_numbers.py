#!/usr/bin/env python3
# Created by: Tomi Oyediran
# Created on: Nov 1, 2022
# This program asks the user to enter a positive number
# and then uses a loop to calculate and display the sum
# of all numbers from 0 until that number.

from tkinter import Variable


def main():

    # user input Variable
    user_number = input("Enter a positive number: ")


loop_counter = 0
sum = 0
# try to cast user number as a string
try:
    user_number = int(input("Enter a positive number: "))
    print("")
    if user_number < 0:
        print("This is not a positive integer")
        exit()
except Exception:
    print("This is not a positive number")
    exit()
# calculates the sum of all numbers starting from 0
while loop_counter <= user_number:
    sum = sum + loop_counter
    print("Tracking {0} times through loop.".format(loop_counter))
    loop_counter = loop_counter + 1

    print("")
    print("The sum of the numbers from 0 to {} is: {}.".format(user_number, sum))
    exit

if __name__ == "__main__":
    main()
