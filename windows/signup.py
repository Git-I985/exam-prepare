from PyQt5 import QtWidgets
from uic.signup import Ui_SignupWindow


class SignupWindow(QtWidgets.QMainWindow, Ui_SignupWindow):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_SignupWindow, self).__init__()
        self.setupUi(self)
