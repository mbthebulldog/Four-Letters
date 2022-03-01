#! python3
# A game where player 1 picks a word for player 2 to guess. Player 2 is only told
# how many (but not which) letters are in the right or wrong spot each round.

import getpass # The getpass module hides player 1's word from player 2 in the terminal

while True:
    # Get a word from player 1
    word = getpass.getpass("Pick an extra-secret special word: ")
    word = word.lower()
    
    # Check that the input is one word and only letters
    if (word.isalpha()):
        break
    elif (not word.isalpha()):
        print("Please, no spaces or special characters.")
    else:
        raise Exception("Input does not match either conditional above.")

# Once a good word is chosen, make a solution list and pass gameplay to player 2
word = list(word)
length = len(word)
finished = False

print("Now pass to a friend, lover, or literate af pet.")
print("-" * 50)

# Loop to allow player 2 to guess the word
while True:
    while True:
        # Get a guess from player 2 and make it a lowercase list
        guess = list(input("Guess a %s-letter word: " %(length)).lower())
        # Make sure the guess is the same length as the word
        if (len(guess) == length):
            break
        elif (not len(guess) == length):
            print("That word isn't the right length!")

    # Set up disposable variables to check the guess
    right = wrong = 0
    tempGuess = guess.copy()
    tempWord = word.copy()
    # print("After Guess: " + str(right) + ' ' + str(wrong) + ' ' + str(tempGuess) + ' ' + str(tempWord)) #Debug

    # Increment *right* for letters in the right spot
    for i in range(length):
        if tempGuess[i] == tempWord[i]:
            right += 1
            tempGuess[i] = '@'
            tempWord[i] = '#'
    # print("After Right Check: " + str(right) + ' ' + str(wrong) + ' ' + str(tempGuess) + ' ' + str(tempWord)) #Debug

    # Increment *wrong* for letters in the wrong spot
    for i in range(length):
        if (tempGuess[i] in tempWord):
            wrong += 1
            tempWord[tempWord.index(tempGuess[i])] = '#'
            tempGuess[i] = '@'
    # print("After Wrong Check: " + str(right) + ' ' + str(wrong) + ' ' + str(tempGuess) + ' ' + str(tempWord)) #Debug
        
    #Show player feedback
    print("Letters in the right spot: " + str(right))
    print("Letters in the wrong spot: " + str(wrong))

    #Once there are as many *right* letters as the length of word, you've won!
    if right == length:
        print("You guessed the word! Take a shot!")
        break