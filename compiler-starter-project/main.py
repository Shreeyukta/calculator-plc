import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLCDNumber

from components.lexica import MyLexer
from components.parsers import PrefixParser
from components.memory import Memory

class MainWindow(QMainWindow):

    # Do this for intellisense
    button_1:QPushButton
    button_2:QPushButton
    button_3:QPushButton
    button_4:QPushButton
    button_5:QPushButton
    button_6:QPushButton
    button_7:QPushButton
    button_8:QPushButton
    button_9:QPushButton
    button_0:QPushButton
    button_plus:QPushButton
    button_multiply:QPushButton
    button_equal:QPushButton
    button_clear:QPushButton

    input_text:QLineEdit

    output_lcd:QLCDNumber
    output_infix: QLCDNumber

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("./components/main.ui", self)

        self.button_1.clicked.connect(lambda: self.push("1"))
        self.button_2.clicked.connect(lambda: self.push("2"))
        self.button_3.clicked.connect(lambda: self.push("3"))
        self.button_4.clicked.connect(lambda: self.push("4"))
        self.button_5.clicked.connect(lambda: self.push("5"))
        self.button_6.clicked.connect(lambda: self.push("6"))
        self.button_7.clicked.connect(lambda: self.push("7"))
        self.button_8.clicked.connect(lambda: self.push("8"))
        self.button_9.clicked.connect(lambda: self.push("9"))
        self.button_0.clicked.connect(lambda: self.push("0"))

        self.button_plus.clicked.connect(lambda: self.push("+"))
        self.button_multiply.clicked.connect(lambda: self.push("*"))

        self.button_clear.clicked.connect(lambda: self.clear_all())

        self.button_equal.clicked.connect(self.push_equal)

        self.output_infix.setReadOnly(True)
    
    def push(self, text:str):
        current_text:str = self.input_text.text()
        self.input_text.setText(f"{current_text}{text}")

    def clear_all(self):
        self.input_text.clear()
        self.output_infix.clear()
        self.output_lcd.display(0)
    
    def push_equal(self):
        print("Calculate")
        lexer = MyLexer()
        prefixparser = PrefixParser()
        memory = Memory()
        # parser = PrefixParser()
        input_text = self.input_text.text()
        result = prefixparser.parse(lexer.tokenize(input_text))
        print(type(result))

        self.output_lcd.display(result)
        self.output_infix.setText(prefixparser.get_infix())
        # for debug
        print(memory)
    



if __name__ == "__main__":
    app = QApplication(sys.argv)
    with open("style.qss", "r") as file:
        app.setStyleSheet(file.read())
    window = MainWindow()
    window.show()
    app.exec()