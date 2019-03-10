class Question():
    def __init__(self,question,options,answer):
        self.question = question
        self.options = options
        self.answer = answer

    def askQuestion(self):
        print(self.question)
        for i in self.options:
            print(i)

        #list of options
        optionList = ['A','B','C','D']

        #user input
        global response
        response = input('Answer: ').strip().upper()
        while True:
            while response not in optionList:
                response = input('Answer not valid. Try again: ').strip().upper()
            break

    def isCorrect(self):
        if response == self.answer:
            return 'Correct\n'
        else:
            return 'Incorrect\n'

    def tallyScore(self):
        if response == self.answer:
            return 1
        else:
            return 0

    #repr() function
    def __repr__(self):
        return 'question: ' + str(self.question) + ' ; ' + \
               'options ' + str(self.options) + ' ; ' + \
               'answer ' + str(self.answer)






