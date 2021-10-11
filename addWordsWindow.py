from PySide2 import QtCore, QtWidgets, QtGui
import sys
from PySide2.QtCore import Qt
from PySide2.QtGui import QPalette, QColor,QIcon
from PySide2.QtWidgets import QWidget, QVBoxLayout, QLabel,QPushButton
from PySide2.QtWidgets import *


class Add_words_window(QDialog):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        self.dictionary = {"a":"a"}
        self.setWindowIcon(QIcon("icon.png"))
        layout = QVBoxLayout()
        self.label_main_text = QLabel("Dodaj tłumaczenie")
        self.label_main_text.setAlignment(Qt.AlignCenter)
        self.label_main_text.setStyleSheet(u"font: 75 13pt \"Arial\";")
        self.label_es = QLabel("ES")
        self.label_es.setAlignment(Qt.AlignCenter)
        self.ES = QtWidgets.QLineEdit()
        self.label_pl = QLabel("PL")
        self.label_pl.setAlignment(Qt.AlignCenter)
        self.PL = QtWidgets.QLineEdit()
        add_button = QPushButton('add')
        add_button.clicked.connect(self.add_new_translaction)

        layout.addWidget(self.label_main_text)
        layout.addWidget(self.label_es)
        layout.addWidget(self.ES)
        layout.addWidget(self.label_pl)
        layout.addWidget(self.PL)
        layout.addWidget(add_button)
        self.setLayout(layout)

    def add_new_translaction(self):
        self.dictionary[self.PL.text()] = self.ES.text()
        print(self.dictionary.items())


if __name__== '__main__':
    app = QtWidgets.QApplication([])
    app.setApplicationDisplayName('Słownik')
    appWidget = Add_words_window()
    appWidget.resize(300,200)
    appWidget.show()
    sys.exit(app.exec_())