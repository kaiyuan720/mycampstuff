#!/usr/bin/env python3

"""
File: dice.py
Name:

Rolls a dice and outputs the result
Concepts covered: Random, printing
"""

import random

def main():
        randNum = random.randint(1,6)
        roll = input("Press any key and then enter to roll a dice. ")
        print("You rolled",randNum)

if __name__ == "__main__":
    main()
