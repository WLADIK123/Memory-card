from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QPushButton, QGroupBox, QButtonGroup
from random import shuffle, randint

app = QApplication([])
main = QWidget()


class Question():
    def __init__(self, question, rightAnswer, wrong1, wrong2, wrong3):
        self.question = question
        self.rightAnswer = rightAnswer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions = []
questions.append(Question('Смертельная доза сыр косички', '5кг', '3кг', '4кг', '6кг'))
questions.append(Question('Сколько весит слон?', '5т', '10т', '3г', '3.5т'))
questions.append(Question('Какая цена танка Emil-II', 'бесценно', '5$', '60000$', '125000$'))
questions.append(Question('Какая смертельная доза бананов?', '400', '350', '300', '469'))

main.total = 0
main.score = 0


main.setWindowTitle('Memory Card')
mainQuestion = QLabel('Какая смертельная доза бананов?')

buttonAnswer = QPushButton('Ответить')

RadioGroupBox = QGroupBox('Варианты ответа')
rbtn1 = QRadioButton('400')
rbtn2 = QRadioButton('350')
rbtn3 = QRadioButton('300')
rbtn4 = QRadioButton('555')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn1)
RadioGroup.addButton(rbtn2)
RadioGroup.addButton(rbtn3)
RadioGroup.addButton(rbtn4)

line1 = QHBoxLayout()
line2 = QVBoxLayout()
line3 = QVBoxLayout()

line2.addWidget(rbtn1)
line2.addWidget(rbtn2)
line3.addWidget(rbtn3)
line3.addWidget(rbtn4)

line1.addLayout(line2)
line1.addLayout(line3)

RadioGroupBox.setLayout(line1)

AnsGroupBox = QGroupBox('Результаты теста')
lbResult = QLabel('Неправильно')
lbCorrect = QLabel('Правильный ответ: 400')

lineRes = QVBoxLayout()
lineRes.addWidget(lbResult, alignment=(Qt.AlignLeft | Qt.AlignTop))
lineRes.addWidget(lbCorrect, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(lineRes)

def showQuestion():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    buttonAnswer.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn1.setChecked(False)
    rbtn2.setChecked(False)
    rbtn3.setChecked(False)
    rbtn4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn1, rbtn2, rbtn3, rbtn4]

def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.rightAnswer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    mainQuestion.setText(q.question)
    lbCorrect.setText(q.rightAnswer)
    showQuestion()

def showCorrect(res):
    lbResult.setText(res)
    showResult()

def showResult():
    AnsGroupBox.show()
    RadioGroupBox.hide()
    buttonAnswer.setText('Следущий Вопрос')



def checkAnswer():
    if answers[0].isChecked():
        showCorrect('Правильно!')
        main.score += 1
        print('Рейтинг:', main.score / main.total  * 100 ,'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            showCorrect('Неправильно!')
            print('Рейтинг:', main.score / main.total * 100 ,'%')
            
     

#main.num = -1

def nextQuestion():
    #main.num += 1
    #if main.num >= len(questions):
       # main.num = 0
    #numQuestion = questions[main.num]
    main.total += 1
    curQuestion = randint(0, len(questions) - 1)
    q = questions[curQuestion]
    ask(q)
    print('Статистика')
    print('-Всего вопросов:', main.total)
    print('-Правильных ответов:', main.score)
    
            



    
def clickOK():
    if buttonAnswer.text() == 'Ответить':
        checkAnswer()
    else:
        nextQuestion()


layoutLine1 = QHBoxLayout()
layoutLine2 = QHBoxLayout()
layoutLine3 = QHBoxLayout()

layoutLine1.addWidget(mainQuestion, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layoutLine2.addWidget(RadioGroupBox)
layoutLine2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layoutLine3.addStretch(1)
layoutLine3.addWidget(buttonAnswer, stretch=3)
layoutLine3.addStretch(1)

lineCard = QVBoxLayout()


lineCard.addLayout(layoutLine1, stretch=3)
lineCard.addLayout(layoutLine2, stretch=8)
lineCard.addStretch(1)
lineCard.addLayout(layoutLine3, stretch=1)
lineCard.addStretch(1)
lineCard.addSpacing(5)


buttonAnswer.clicked.connect(clickOK)


main.resize(600, 300)
main.setLayout(lineCard)
nextQuestion()
main.show()
app.exec_()