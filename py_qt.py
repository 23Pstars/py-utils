from PyQt5 import QtWidgets, uic
import sys


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('py_qt.ui', self)
        self.btnChangeText.clicked.connect(self._change_text)
        self.show()

    def _change_text(self):
        self.labelHello.setText('Change the World !')


app = QtWidgets.QApplication(sys.argv)
window = Ui()
app.exec_()
