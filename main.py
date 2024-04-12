import sys
from PyQt5 import QtWidgets
from db import *
from windows.admin import AdminWindow
from windows.login import LoginWindow
from windows.signup import SignupWindow
from windows.user import UserWindow


class App(QtWidgets.QApplication):
    def __init__(self, *argv):
        super().__init__(*argv)
        self.login_window = LoginWindow()
        self.user_window = UserWindow()
        self.admin_window = AdminWindow()
        self.signup_window = SignupWindow()
        self.admin_window.show()

        self.login_window.pushButton.clicked.connect(self.try_to_login)
        self.signup_window.pushButton.clicked.connect(self.try_to_signup)

        self.login_window.pushButton_2.clicked.connect(self.switch_to_signup)
        self.signup_window.pushButton_2.clicked.connect(self.switch_to_login)

    def switch_to_signup(self):
        self.signup_window.show()
        self.login_window.close()

    def switch_to_login(self):
        self.login_window.show()
        self.signup_window.close()

    def try_to_login(self):
        login = self.login_window.lineEdit.text()
        password = self.login_window.lineEdit_2.text()

        if not len(login) or not len(password):
            return

        if login == 'root' and password == 'root':
            self.login_window.close()
            self.admin_window.show()
        else:
            user = User.get_or_none(User.login == login, User.password == password)
            if user:
                self.login_window.close()
                self.user_window.show()
            else:
                QtWidgets.QMessageBox.critical(
                    self.login_window,
                    "Ошибка",
                    "Пользователь не существует"
                )

    def try_to_signup(self):
        # todo signup
        pass


app = App(sys.argv)
app.exec_()
