from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel,QButtonGroup)
from random import shuffle
class Questions():
    def __init__(self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
questions_list = []
questions_list.append(Questions('Государвственный язык бразилии', 'Португальский', 'Английский', 'Испанский', 'Бразильский'))
questions_list.append(Questions('Какого цвета нет на флаге россии','Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Questions('Национальныя хижина якутов','Ураса', 'Юрта', 'Иглу', 'Хата'))

app = QApplication([])


window = QWidget()
window.setWindowTitle('Memo Card')
 
'''Интерфейс приложения Memory Card'''
btn_OK = QPushButton('Ответить') # кнопка ответа
lb_Question = QLabel('Самый сложный вопрос в мире') # текст вопроса
 
RadioGroupBox = QGroupBox("Варианты ответов") # группа на экране для переключателей с ответами
rbtn_1 = QRadioButton('Вариант 1 ')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
 
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() # вертикальные будут внутри горизонтального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) # два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) # два ответа во второй столбец
layout_ans3.addWidget(rbtn_4)
 
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке
 
RadioGroupBox.setLayout(layout_ans1) # готова "панель" с вариантами ответов 
AnsGroupBox = QGroupBox('result of the test')
lb_Result = QLabel('Are you right?')
lb_Correct = QLabel('Answer will be here')

layout_line1 = QHBoxLayout() # вопрос
layout_line2 = QHBoxLayout() # варианты ответов или результат теста
layout_line3 = QHBoxLayout() # кнопка "Ответить"
 
layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
 
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)
 
# Теперь созданные строки разместим друг под другой:
layout_card = QVBoxLayout()
 
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым
def show_result(): 
    RadioGroupBox.hide()
    AnsGroupBox.show()
    tn_OK.setText('Следующий вопрос')
def show_question(): 
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Оветить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
answer = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]
def ask(question,right_answer,wrong1,wrong2,wrong3):
    shuffle(answers)
    answers[0].setText(right_answer)
    answers[1].setText(wrong1)
    answers[2].setText(wrong1)
    answers[3].setText(wrong1)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()
def show_correct(res):
    lb_result.setText(res)
    show_result()
def check_answer(): 
    if answer[0].isChecked():
        show_correct('Правильно')
    else:
        if answer[1].isChecked or answer[2].isChecked or answer[3].isChecked():
            show_correct('Неверно!!')
def next_question():
    window.cur_question = window.car_question +1
    if windiow.cur_question>=len(questions_list):
        window.cur_question = 0
    q = questions_list[window.cur_question]
    ask(q)
def click_OK():
    if btn_OK.text()=='Ответить':
        check_answer()
    else:
        next_question()

window = QWidget()
window.setLayout(layout_card)
window.show()
window.setWindowTitle('Memo Card')
window.cur_question = -1

btn_OK.clicked.connect(click_OK)

next_question

app.exec()