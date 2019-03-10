'''
Michael Brickley
Trivia Quiz
This program is a trivia quiz which asks the user 15 questions of varying topics.
The program calculates the users score and outputs the results to a text file.
The user is allowed the option to start the quiz over again, or terminate the program
Python Version [2/3]: 3
'''

#import modules
import Questions
import sys

#title
print('Trivia Quiz')

#import answer key
try:
    answerKey = open('answerKey.txt','r')
except FileNotFoundError:
    sys.exit('Answer key not found. Please save answerKey.txt in your working directory and restart program')

#create list from answer key
keys = answerKey.read().strip().split(',')

#main function
def main():
    '''
    Description: Runs main program
    :return: None
    '''
    #list of question objects
    questions = [
        Questions.Question('What country won the first FIFA World Cup?\n',
                           ['A) Switzerland', 'B) Uruguay', 'C) Brazil', 'D) Argentina\n'], keys[0]),
        Questions.Question('Who is considered the Father of the Computer?',
                           ['A) Charles Babbage', 'B) Herman Hollerith', 'C) Steve Jobs', 'D) Alan Turing\n'], keys[1]),
        Questions.Question('Which of the following inventions was the first to be patented?\n',
                           ['A) Cash Register', 'B) Chewing Gum', 'C) Rubber Band', 'D) Dishwasher\n'],keys[2]),
        Questions.Question('How long did the Hundred Years\' War last?\n',
                           ['A) 116 Years', 'B) 99 Years', 'C) 100 Years', 'D) 86 Years\n'], keys[3]),
        Questions.Question('Which of the following terms does not refer to a potentially harmful computer program?\n',
                           ['A) Rootkit', 'B) Spyware', 'C) Adware', 'D) Hardware\n'], keys[4]),
        Questions.Question('When the first Burger King opened in 1954, how much did a hamburger cost?\n',
                           ['A) 9 cents', 'B) 18 cents', 'C) 50 cents', 'D) 37 cents\n'], keys[5]),
        Questions.Question('Who is the 16th president of the United States?\n',
                           ['A) Andrew Jackson',
                            'B) Franklin Pierce',
                            'C) Abraham Lincoln',
                            'D) Grover Cleveland\n'], keys[6]),
        Questions.Question('What is the color of Donald Duck\'s bowtie?\n',
                           ['A) Yellow', 'B) Blue', 'C) Red', 'D) Green\n'],keys[7]),
        Questions.Question('What is the largest planet in our Solar System?\n',
                           ['A) Jupiter', 'B) Pluto', 'C) Saturn', 'D) Earth\n'], keys[8]),
        Questions.Question('Which movie was the first to win 11 Academy Awards?\n',
                           ['A) La La Land', 'B) Titanic', 'C) Sound of Music', 'D) Ben-Hur\n'], keys[9]),
        Questions.Question('How many spaces are on a standard Monopoly board?\n',
                           ['A) 60', 'B) 80', 'C) 40', 'D) 20\n'], keys[10]),
        Questions.Question('How many blue stripes does the United States of America national flag have?\n',
                           ['A) 7', 'B) 0', 'C) 13', 'D) 6\n'], keys[11]),
        Questions.Question('Adele performed the theme song to which James Bond film?\n',
                           ['A) From Russia With Love',
                            'B) Skyfall',
                            'C) Casino Royale',
                            'D) Quantum of Solace\n'], keys[12]),
        Questions.Question('What was the first successful vaccine developed in history?\n',
                           ['A) Smallpox', 'B) Scarlet Fever', 'C) Rabies', 'D) Cholera\n'], keys[13]),
        Questions.Question('Which mammal first reached Earth\'s orbit alive?\n',
                           ['A) Human', 'B) Cat', 'C) Monkey', 'D) Dog\n'], keys[14])
    ]

    #run through quiz
    score = 0
    for i in questions:
        #ask question
        i.askQuestion()
        #inform user if correct
        print(i.isCorrect())
        #increment score
        if i.tallyScore() == 1:
            score += 1

    #output results
    printResults = 'results.txt'
    newFile = open(printResults,'w')
    newFile.write('Score = ' + str(score) + '/' + str(len(questions)))
    newFile.close()
    print('Score outputted to working directory; file name = results.txt\n')

    #if user wants to play again
    playAgainList = ['Y','N']
    playAgain = input('Want to play again? [Y/N]: ').strip().upper()
    while True:
        while playAgain not in playAgainList:
            playAgain = input('Response not valid. Try again: ').strip().upper()
        break
    if playAgain == 'Y':
        #line break
        print()
        #re-run main function
        main()
    else:
        sys.exit('Thanks for playing!')

#run program
main()


