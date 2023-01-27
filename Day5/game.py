import random

# Generate a random number for the game
answer = str(random.randint(1000, 9999))

# Start the game
while True:
    guess = input("Guess a 4-digit number: ")
    if guess == answer:
        print("Congratulations! You won the game!")
        break
    else:
        strike = 0
        ball = 0
        for i in range(4):
            if guess[i] in answer:
                if guess[i] == answer[i]:
                    strike += 1
                else:
                    ball += 1
        print(f"{strike} strike(s), {ball} ball(s)")