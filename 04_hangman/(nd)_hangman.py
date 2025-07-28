from random import choice

def run_game():
    word: str = choice(['apple' , 'secret' , 'banana'])

    #A friendly interactive welcome message
    username: str = input('What is your name, Human?')
    print(f'Welcome to hangman, {username}, you damn Human!')


    #set up
    guessed: str = '' #will contain all the letters used to guess
    tries: int = 3 # Set the amount of tries you want the user to have

    # the game!
    while tries > 0:
        blanks: int = 0

        print('Word: ' , end='')
        for char in word: 
            if char in guessed:
                print(char , end = '')
            else:
                print('_' , end = '')
                blanks += 1
                
                
        print() # add a blank

        # if there are no blanks left, that means the suer won the game
        if blanks == 0: 
            print('You got it you damn Human!')
            break

        # get user input
        guess: str = input('Enter a letter: ')

        # check that the user isn't just guessing the same letter again
        if guess in guessed: 
            print(f'You already used: "{guess}". Please try another letter you loser.')
            continue

        # add the guess to the guessed string
        guessed += guess

        # check that the guess is in the word
        if guess not in word:
            tries -= 1
            print(f'Sorry dude that was wrong . . . ({tries} tries remaining)')

            #game over if tries reach 0
            if tries == 0:
                print('No more tries remaining sucker . .  . You lose.')
                break

if __name__ == '__main__':
    run_game()