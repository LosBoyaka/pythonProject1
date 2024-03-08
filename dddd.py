from PyQt5.QtWidgets import*

app = QApplication([])
window = QWidget()
window.resize(500, 500)
quest_lbl = QLabel("В якому році народився Т. Г. Шевченко")
radio1 = QRadioButton("2010")
radio2 = QRadioButton("1814")
radio3 = QRadioButton("2000")
radio4 = QRadioButton("1764")

main_line = QVBoxLayout()
main_line.addWidget(quest_lbl)

h1 = QHBoxLayout()
h1.addWidget(radio1)
h1.addWidget(radio2)
main_line.addLayout(h1)

def wrong_answet_func():
    msg = QMessageBox()
    msg.setText("Не вірно!")
    msg.exec()

radio1.clicked.connect(wrong_answet_func)
radio3.clicked.connect(wrong_answet_func)
radio4.clicked.connect(wrong_answet_func)

def true_answet_func():
    msg = QMessageBox()
    msg.setText("Bірно!")
    msg.exec()

radio2.clicked.connect(true_answet_func)

h2 = QHBoxLayout()
h2.addWidget(radio3)
h2.addWidget(radio4)
main_line.addLayout(h2)

quest_lbl2 = QLabel("В якому році Україна здобула незалежність?")
radio5 = QRadioButton("2010")
radio6 = QRadioButton("1991")
radio7 = QRadioButton("2020")
radio8 = QRadioButton("1256")


main_line.addWidget(quest_lbl2)

h3 = QHBoxLayout()
h3.addWidget(radio5)
h3.addWidget(radio6)
main_line.addLayout(h3)

def wrong2_answet_func():
    msg = QMessageBox()
    msg.setText("Не вірно!")
    msg.exec()

radio5.clicked.connect(wrong2_answet_func)
radio7.clicked.connect(wrong2_answet_func)
radio8.clicked.connect(wrong2_answet_func)

def true2_answet_func():
    msg = QMessageBox()
    msg.setText("Bірно!")
    msg.exec()

radio6.clicked.connect(true2_answet_func)

h4 = QHBoxLayout()
h4.addWidget(radio7)
h4.addWidget(radio8)
main_line.addLayout(h4)

quest_lbl3 = QLabel("Де зробили першу піцу?")
radio9 = QRadioButton("Рим")
radio10 = QRadioButton("Київ")
radio11 = QRadioButton("Неаполь")
radio12 = QRadioButton("Воронеж")


main_line.addWidget(quest_lbl3)

h5 = QHBoxLayout()
h5.addWidget(radio9)
h5.addWidget(radio10)
main_line.addLayout(h5)

def wrong3_answet_func():
    msg = QMessageBox()
    msg.setText("Не вірно!")
    msg.exec()

radio9.clicked.connect(wrong3_answet_func)
radio10.clicked.connect(wrong3_answet_func)
radio12.clicked.connect(wrong3_answet_func)

def true3_answet_func():
    msg = QMessageBox()
    msg.setText("Bірно!")
    msg.exec()

radio11.clicked.connect(true3_answet_func)

h6 = QHBoxLayout()
h6.addWidget(radio11)
h6.addWidget(radio12)
main_line.addLayout(h6)

window.setLayout(main_line)
window.show()
app.exec()

