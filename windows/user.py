from PyQt5 import QtWidgets
from uic.user import Ui_UserWindow

class UserWindow(QtWidgets.QMainWindow, Ui_UserWindow):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_UserWindow, self).__init__()
        self.setupUi(self)
