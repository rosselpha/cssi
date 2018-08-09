
def initWord(word):
    temp = []
    for i in  word:
        temp.append('_')
    return temp
def printBoard(board, guessList):
    print " ".join(board)
    print "guesses:" + " ".join(guessList)

def addGuess(board, word, guess):
    for i in range(len(word)):
        if guess == word[i]:
            board[i] = guess

def game():
    chooseWord = 'programming'.lower()
    guesses = []
    board = initWord(chooseWord)

    while '_' in board:
        printBoard(board, guesses)
        guess = raw_input('enter a letter: ').lower()

        if len(guess) == 1:
            if guess in chooseWord:
                addGuess(board, chooseWord, guess)

            guesses.append(guess)
        else:
            print **.join(board)
            print 'u win *i**h'

game()
