import random

ran = random.randint(1,3)
match ran:
    case 1:
        computerChoice = "stone"
    case 2:
        computerChoice = "paper"
    case 3:
        computerChoice = "scissors"

print("1.Stone")
print("2.Paper")
print("3.Scissors")
playerChoice = int(input("Enter your choice(The No.):"))
if playerChoice == 1 and ran == 1:
    print("Tie, Computer choosed:", computerChoice)
elif playerChoice == 1 and ran == 2:
    print("You lost, lol. Computer choosed:", computerChoice)
elif playerChoice == 1 and ran == 3:
    print("You Win. Computer choosed:", computerChoice)
elif playerChoice == 2 and ran == 1:
    print("You Win. Computer choosed:", computerChoice)
elif playerChoice == 2 and ran == 2:
    print("Tie, Computer choosed:", computerChoice)
elif playerChoice == 2 and ran == 3:
    print("You lost, lol. Computer choosed:", computerChoice)
elif playerChoice == 3 and ran == 1:
    print("You lost, lol. Computer choosed:", computerChoice)
elif playerChoice == 3 and ran == 2:
    print("You Win. Computer choosed:", computerChoice)
elif playerChoice == 3 and ran == 3:
    print("Tie, Computer choosed:", computerChoice)
elif playerChoice>3:
    print("Invalid Choice")