from PySide2 import QtCore, QtWidgets, QtGui
import sys


class InlineTranslation:
    def __init__(self, to_translate,input_form, translated, correct_translation):
        self.to_translate = to_translate
        self.input_form = input_form
        self.translated = translated
        self.correct_translation = correct_translation



class AppWidget(QtWidgets.QWidget):
    def __init__(self, words):
        super().__init__()
        self.points = 0
        self.words = words
        self.state = []
        self.layout = self.initalize_layout()
        self.setLayout(self.layout)

    def on_submit(self):
        self.points = 0
        for inline in self.state:
            if inline.correct_translation == inline.input_form.text():
                self.points += 1
            print(inline.to_translate)
            print(inline.correct_translation)
            print(inline.input_form.text())

        msg = QtWidgets.QMessageBox()
        msg.setText(f'Ilość poprawnych odpowiedzi to : {self.points}')


    def initalize_layout(self):
        row = 0
        grid = QtWidgets.QGridLayout()
        for key, correct_translation in self.words.items():
            to_translate = QtWidgets.QLabel(key)
            input_form = QtWidgets.QLineEdit()
            self.state.append(InlineTranslation(key,input_form, '', correct_translation))
            grid.addWidget(to_translate,row,0)
            grid.addWidget(input_form,row,1)
            row += 1
        submit = QtWidgets.QPushButton('Sprawdz')
        submit.clicked.connect(self.on_submit)
        grid.addWidget(submit, row, 1)

        return grid

        #layout = QtWidgets.QVBoxLayout()
        #layout.addWidget(label)


if __name__== '__main__':
    words = {
        'el perro' : 'pies',
        'el gato' : 'kot'
    }
    app = QtWidgets.QApplication([])
    app.setApplicationDisplayName('Tarjetas espanoles')
    appWidget = AppWidget(words)
    appWidget.resize(800,600)
    appWidget.show()
    sys.exit(app.exec_())