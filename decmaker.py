import random

def main():
        randNum = random.randint(1,6)
        you = input("Welcome to Kaiyuan's Decision maker, feel free to ask Kaiyuan Yes or No Questions!: ")
        while (True):
                randNum = random.randint(1,6)
                if randNum == 1:
                        print("Kaiyuan has thought it over and Kaiyuan says Yes!")
                elif randNum == 2:
                        print("Kaiyuan dissaproves and therfore Kaiyuan says No!")
                elif randNum == 3:
                        print("Absolutely Yes!")
                elif randNum == 4:
                        print("Kaiyuan is not so sure, Kaiyuan thinks maybe?")
                elif randNum == 5:
                        print("Kaiyuan thinks the best advice for this question would be from a friend, ask a friend!")
                elif randNum == 6:
                        print("Kaiyuan says pay me and your question will matter no more!")
                again = input("Do you want to ask again? y/n ")
                if again == "y":
                        You = input("Welcome to Kaiyuan's Decision maker, feel free to ask Kaiyuan Yes or No Questions!: ")
                
                else:
                        break
                

if __name__ == "__main__":
        main()