# Simple hangman

def check_word():
    correct_word = True
    if len(word) == 0:
        correct_word = False

    else:
        for letters in range(len(word)):
            if word[letters] == ' ':
                correct_word = False
            elif word[letters].isdigit():
                correct_word = False

    return correct_word


def display_dash():
    print("Display:", end=' ')
    for dash in empty_word:
        print(dash, end='')
    print()


guess_count = 0
word = list(input("Word to be guessed: ").lower())

valid_word = check_word()

while valid_word is False:
    word = list(input("Invalid entry. Word to be guessed: ").lower())
    valid_word = check_word()

empty_word = []

for i in range(len(word)):
    empty_word.append("-")

display_dash()

while word != empty_word:
    guess = input("Letter guessed: ").lower()

    while len(guess) == 0 or len(guess) > 1 or guess == ' ' or guess.isdigit():
        guess = input("Invalid entry. Enter guess: ").lower()

    guess_count += 1

    for letter in range(len(word)):
        if guess == word[letter]:
            empty_word[letter] = guess

    display_dash()

print("Number of guesses:", guess_count)
