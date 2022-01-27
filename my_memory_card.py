#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QRadioButton, QGroupBox, QButtonGroup
from random import shuffle
from random import randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question 
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3  

question_list = []
question_list.append(Question("Какой национальности не существует?", "Смурфы", "Энцы", "Чулымцы","Алеуты"))
question_list.append(Question("Какого цвета нет на флаге Германии", "Синего", "Красного", "Чёрного","Жёлтого"))
question_list.append(Question("Какой основной язык в Австралии?", "Английский", "Французкий", "Китайский", "Португальский"))

app = QApplication([])

main_win = QWidget()

main_win.setWindowTitle("Memory Card")
question = QLabel("Какой национальности не существует?")
bt_ans = QPushButton("Ответить")
main_win.resize(400,400)

RadioGroupBox = QGroupBox("Варианты ответов")
rbt_1 = QRadioButton("Энцы")
rbt_2 = QRadioButton("Смурфы")
rbt_3 = QRadioButton("Чулымцы")
rbt_4 = QRadioButton("Алеуты")

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbt_1)
RadioGroup.addButton(rbt_2)
RadioGroup.addButton(rbt_3)
RadioGroup.addButton(rbt_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()

layout_ans2.addWidget(rbt_1)
layout_ans2.addWidget(rbt_2)

layout_ans3.addWidget(rbt_3)
layout_ans3.addWidget(rbt_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

ansGroupBox = QGroupBox("Результат теста")
result = QLabel("прав ты  или нет?")
correct = QLabel("ответ будет тут")

layout_res = QVBoxLayout()
layout_res.addWidget(result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(correct, alignment= Qt.AlignHCenter, stretch=2)
ansGroupBox.setLayout(layout_res)


layout_l1 = QHBoxLayout()
layout_l2 = QHBoxLayout()
layout_l3 = QHBoxLayout()

layout_l1.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_l2.addWidget(RadioGroupBox)
layout_l2.addWidget(ansGroupBox)
ansGroupBox.hide()

layout_l3.addStretch(1)
layout_l3.addWidget(bt_ans, stretch=3)
layout_l3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_l1, stretch=2)
layout_card.addLayout(layout_l2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_l3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)


def show_res():
    RadioGroupBox.hide()
    ansGroupBox.show()
    bt_ans.setText("Следующий вопрос")

def show_ques():
    ansGroupBox.hide()
    RadioGroupBox.show()
    bt_ans.setText("Ответить")
    RadioGroup.setExclusive(False)
    rbt_1.setChecked(False)
    rbt_2.setChecked(False)
    rbt_3.setChecked(False)
    rbt_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbt_1, rbt_2, rbt_3, rbt_4]

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    correct.setText(q.right_answer)
    show_ques()

def show_corr(res):
    result.setText(res)
    show_res()

def check_ans():

    if answers[0].isChecked():
        main_win.score +=1
        show_corr("Правильно!!")
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_corr("Неправильно!!")
    statistics = (main_win.score/main_win.total) *100
    print("Всего вопросов:",main_win.total)
    print("Правильных ответов:", main_win.score)
    print("Статистика:", statistics)

def next_question():
    
    main_win.total += 1
    cur_question = randint(0, len(question_list) - 1)
    
    q = question_list[cur_question]
    ask(q)
    

def click_ok():
    if bt_ans.text() == "Ответить":
        check_ans()
    else:
        next_question()

main_win.setLayout(layout_card)
main_win.total = 0
main_win.score = 0
#statistics = (main_win.score/main_win.total) *100
#kl =  str(statistics)
#print(kl)
bt_ans.clicked.connect(click_ok)
next_question()



main_win.show()
app.exec()





