import getpass

while True:
    word = getpass.getpass("Pick an extra-secret special word: ")
    word = word.lower()
    if (word.isalpha()):
        break
    elif (not word.isalpha()):
        print("Please, no spaces or special characters.")
    else:
        raise Exception("Input does not match either conditional above.")

print("Now pass to a friend, lover, or literate af pet.")
print("---------")

word = list(word)
length = len(word)
finished = False

while True:
    right= wrong = 0
    guess = list(input("Guess a %s-letter word: " %(length)))

    #Increment *right* for letters in the right spot
    for i in range(length):
        if word[i] == guess[i]:
            right += 1

    #TODO: Increment *wrong* for letters in the wrong spot
    # for i in range(length):
    #     if word[i] == guess[i]:
    #         right += 1

    #

    #Once there are as many *right* letters as the length of word, you've won!
    if right == length:
        print("You guessed the word! Take a shot!")
        break