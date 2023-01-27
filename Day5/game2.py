import random

# List of words for the game
word_list = ["python", "programming", "language", "computer", "science"]

# Select a random word from the list
answer = random.choice(word_list)

# Create a list of underscores the same length as the answer
display = ["_"] * len(answer)

# Number of incorrect guesses
incorrect_guesses = 0

# Start the game
while incorrect_guesses < 6:
    print(" ".join(display))
    guess = input("Guess a letter: ").lower()
    if guess in answer:
        for i in range(len(answer)):
            if answer[i] == guess:
                display[i] = guess
        if "_" not in display:
            print(" ".join(display))
            print("Congratulations! You won the game!")
            break
    else:
        incorrect_guesses += 1
        print(f"Incorrect! You have {6 - incorrect_guesses} guesses left.")

if "_" in display:
    print("Sorry, you lost the game. The word was", answer + ".")