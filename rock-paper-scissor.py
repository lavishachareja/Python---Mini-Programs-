import random

def userchoice():
  print("R: rock")
  print("P: paper")
  print("S: scissors")
  choice = input("Enter your choice: ")
  choice = choice.upper()
  if choice != "R" and choice != "P" and choice != "S":
    print("Invalid Choice")
    choice = userchoice()
  return choice

def computerchoice():
  choice = random.choice(["R", "P", "S"])
  print("Computer Choice:",choice)
  return choice

def game(user, userc, computer):
  if userc == computer:
    print("TIE!!!")
  if userc == "R" and computer =="P":
    print("Computer wins!!!")
  if userc == "R" and computer =="S":
    print(user,"wins!!!")
  if userc == "P" and computer == "R":
    print(user,"wins!!!")
  if userc == "P" and computer == "S":
    print("Computer wins!!!")
  if userc == "S" and computer == "P":
    print(user,"wins!!!")
  if userc == "S" and computer == "R":
    print("Computer wins!!!")

print("Player Name:")
name = input()
print("Welcome",name)
print("Time for Rock-Paper-Scissor")
uc = userchoice()
cc = computerchoice()
game(name, uc, cc)