import random

print("Ready for a game of Rock, Paper, Scissors?!")
print("Rock, Paper, Scissors, says...")
print("Rock")
print("Paper")
print("Scissors")
p1 = input("SHOOT!: ").lower()
p2 = random.choice(["Rock", "Paper", "Scissors"]).lower()

while p1 not in ["Rock", "Paper", "Scissors", "rock", "paper", "scissors"]:
    p1 = input("Your choice wasn't valid, please shoot again!: ")

print("And...the Computer shoots...", p2, "!", sep = "")

while p1 == p2:
    p1 = input("It's a tie, shoot again!: ").lower()
    p2 = random.choice(["Rock", "Paper", "Scissors"]).lower()
    
    while p1 not in ["Rock", "Paper", "Scissors", "rock", "paper", "scissors"]:
        p1 = input("Your choice wasn't valid, please shoot again!: ")
    
    print("And this time...the Computer shoots...", p2, "!", sep = "")

if p1 == "rock" and p2 == "paper":
    print("Paper beats rock, you lose!")
elif p1 == "rock" and p2 == "scissors":
    print("Rock beats scissors, you win!")
elif p1 == "paper" and p2 == "rock":
    print("Paper beats rock, you win!")
elif p1 == "paper" and p2 == "scissors":
    print("Scissors beat paper, you lose!")
elif p1 == "scissors" and p2 == "rock":
    print("Rock beats scissors, you lose!")
elif p1 == "scissors" and p2 == "paper":
    print("Scissors beat paper, you win!")