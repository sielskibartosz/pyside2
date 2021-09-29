from PySide2 import QtCore, QtWidgets, QtGui
import sys


class AppWidget(QtWidgets.QWidget):
    def __init__(self, to_translate):
        super().__init__()
        self.to_translate = to_translate
        self.layout = self.initalize_layout()
        self.setLayout(self.layout)

    def initalize_layout(self):
        row = 0
        grid = QtWidgets.QGridLayout()
        for key in self.to_translate:
            label = QtWidgets.QLabel(key)
            enter = QtWidgets.QLineEdit()
            grid.addWidget(label,row,0)
            grid.addWidget(enter,row,1)
            row += 1

        return grid

        #layout = QtWidgets.QVBoxLayout()
        #layout.addWidget(label)


if __name__== '__main__':
    to_translate = {
        'el perro' : 'pies',
        'el gato' : 'kot'
    }
    app = QtWidgets.QApplication([])
    app.setApplicationDisplayName('Tarjetas espanoles')
    appWidget = AppWidget(to_translate)
    appWidget.resize(800,600)
    appWidget.show()
    sys.exit(app.exec_())