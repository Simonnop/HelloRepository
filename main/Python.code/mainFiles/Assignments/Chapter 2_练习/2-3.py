answerNum=66

print('''There is a hidden integer in this program.
You can guess what it is by entering your guess.''')

while True:
    guessNum=int(input('Please enter your guess:'))

    if guessNum==answerNum:
        print('Congratulations! You guessed it!')
        break
    elif guessNum<answerNum:
        print('No,the hidden number is larger than',guessNum)
    else:
        print('No,the hidden number is smaller than {}'.format(guessNum))
        
print('Done')