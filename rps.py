#!/usr/bin/env python3

"""
File: rps.py
Name:

A rock-paper-scissors game against the CPU
Concepts covered: Random, IO, if/else, printing
"""

import random
import sys

def main():
    p1 = input("Rock(r), Paper(p), or Scissors(s)? ")
    if p1 == "r":
        print("You chose Rock")
    elif p1 == "p":
        print("You chose Paper")
    elif p1 == "s":
        print("You chose Scissors")
    p2 = ai_guess()
    checkWin(p1, p2)
    
def ai_guess():
    p2 = random.randint(1,3)
    if p2 == 1:
        print("CPU chose Rock")
    elif p2 == 2:
        print("CPU chose Paper")
    elif p2 == 3:
        print("CPU chose Scissors")
    return p2


def checkWin(p1, p2):
    if (p1 == "r" and p2 == 1):
        print("You chose Rock and CPU chose Rock, Tie!")
    elif (p1 == "r" and p2 == 2):
            print("You chose Rock and CPU chose Paper, You Lose!")
    elif (p1 == "r" and p2 == 3):
            print("You chose Rock and CPU chose Scissors, You Win!")
    elif (p1 == "p" and p2 == 1):
                print("You chose Paper and CPU chose Rock, You Win!")
    elif (p1 == "p" and p2 == 2):
                    print("You chose Paper and CPU chose Paper, Tie!")
    elif (p1 == "p" and p2 == 3):
                    print("You chose Paper and CPU chose Scissors, You Lose!")
    elif (p1 == "s" and p2 == 1):
                print("You chose Scissors and CPU chose Rock, You Lose!")
    elif (p1 == "s" and p2 == 2):
                    print("You chose Scissors and CPU chose Paper, You Win!")
    elif (p1 == "s" and p2 == 3):
                    print("You chose Scissors and CPU chose Scissors, CPU Wins!")    
            

if __name__ == "__main__":
    main()
