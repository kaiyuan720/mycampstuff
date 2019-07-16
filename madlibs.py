#!/usr/bin/env python3

"""
File: madlibs.py
Name:

A madlibs adventure!
Concepts covered: Strings, IO, printing
"""

def main():
    adje = input("Please enter an adjective ")
    person = input("Please enter a name ")
    job = input("Please enter a job ex:worker,doctor,etc ")
    hir = input("Please enter his or her ")
    heshe = input("Please enter he or she ")
    print("There was once a",adje,"person named",person,",",person,"was a you guessed it,",adje,"person",",",person,"pretended to love",hir,"job, but everyone knows that",heshe,"hated being a",job)
    

if __name__ == "__main__":
    main()
