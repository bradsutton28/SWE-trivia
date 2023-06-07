from json import *
from tkinter import *
from tkinter import messagebox as mbox
import json

"""
Bradley Sutton
Questions and Answers from InterviewBit.com
Ref: https://www.tutorialspoint.com/python/python_gui_programming.htm
Ref: https://www.tutorialspoint.com/python/tk_anchors.htm
"""


class Quiz:
    def __init__(self):
        self.sizeOfData = len(questions)
        self.questionNumber = 0
        self.showTitle()
        self.showQuestion()
        self.opt_selected = IntVar()
        self.opts = self.checkBoxes()
        self.showMPCdata()
        self.userButtons()
        self.answersCorrect = 0
        self.answersWrong = 0

    def showResults(self):
        numCorrect = f"Number of Questions Correct: {self.answersCorrect}"
        numWrong = f"Number of Questions Incorrect: {self.sizeOfData - self.answersCorrect}"
        userScore = int(self.answersCorrect / self.sizeOfData * 100)
        userResult = f"Your Score: {userScore}%"
        mbox.showinfo("-- Your Results --", f"{userResult}\n{numCorrect}\n{numWrong}")

    def checkAnswer(self, questionNumber):
        if self.opt_selected.get() == answers[questionNumber]:
            return True

    def next(self):
        if self.checkAnswer(self.questionNumber):
            self.answersCorrect += 1
        self.questionNumber += 1
        if self.questionNumber == self.sizeOfData:
            self.showResults()
            root.destroy()
        else:
            self.showQuestion()
            self.showMPCdata()

    def userButtons(self):
        nextButton = Button(root, text="Next", command=self.next,
                            width=5, bg="white", fg="red", font=("ariel", 16, "bold"))
        nextButton.place(x=350, y=380)

        quitButton = Button(root, text="Quit", command=root.destroy, width=5,
                            bg="white", fg="red", font=("ariel", 16, "bold"))
        quitButton.place(x=450, y=380)

    def showMPCdata(self):
        value = 0
        self.opt_selected.set(0)
        for option in options[self.questionNumber]:
            self.opts[value]['text'] = option
            value += 1

    def showQuestion(self):
        questionNumber = Label(root, text=questions[self.questionNumber], width = 100,
                               font=("ariel", 16, "bold"), anchor="w")
        questionNumber.place(x=70, y=100)

    def showTitle(self):
        title = Label(root, text="Software Engineering Trivia Questions",
        width=100, fg="purple", bg="black", font=("ariel", 20, "bold"), anchor="w")
        title.place(x=0, y=1)


    def checkBoxes(self):
        questionList = []
        yPosition = 150
        while len(questionList) < 4:
            checkBox = Radiobutton(root, text=" ", variable=self.opt_selected,
                                   value=len(questionList) + 1, font=("ariel", 14))
            questionList.append(checkBox)
            checkBox.place(x=100, y=yPosition)
            yPosition += 40
        return questionList


root = Tk()
root.geometry("1200x450")
root.title("Software Engineering Trivia Game")
with open('questions.json') as jsonFile:
    data = json.load(jsonFile)
questions = (data["questions"])
options = (data["options"])
answers = (data["answers"])
quiz = Quiz()
root.mainloop()