import random

name = input("Enter your name : ")
words = ['hangman','programming','python','binod','codesnail']

word = random.choice(words)

print('Guess the characters')
guesses = ''
turns = 12

while turns > 0:
    failed= 0
    for ans in word:
        if ans in guesses:
            print(ans)
        else:
            print("_")
            failed += 1
    if failed== 0:
        print('You Win!')
        print(f'The word is : {word}')
        break

    guess = input('Guess the character : ')
    guesses += guess

    if guess not in word:
        turns -= 1
        print('Wong')
        print(f'no. of guesses left = {turns}')

        if turns == 0:
            print('You loss!')
