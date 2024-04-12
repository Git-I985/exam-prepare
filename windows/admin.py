from PyQt5 import QtWidgets
from uic.admin import Ui_AdminWindow
from qt_models.position import position_model
from qt_models.employee import employee_model
from db import db

class AdminWindow(QtWidgets.QMainWindow, Ui_AdminWindow):
    def __init__(self, *argv):
        super(QtWidgets.QMainWindow, self).__init__(*argv)
        super(Ui_AdminWindow, self).__init__()
        self.setupUi(self)
        self.tableView.setModel(employee_model)
        self.tableView_2.setModel(position_model)
        self.pushButton.clicked.connect(self.add_user)
        self.pushButton_2.clicked.connect(self.delete_user)
        self.pushButton_3.clicked.connect(self.fill_user)
        self.pushButton_4.clicked.connect(self.save_user)
        self.pushButton_17.clicked.connect(self.recalculate_payments)
        self.comboBox.setModel(position_model)
        self.pushButton_4.setDisabled(True)
    def recalculate_payments(self):
        cols = [
            'Сотрудник',
            'Оклад',
            'Дней отпуска',
            'Сумма отпускных',
            'Отпускные с надбавкой',
        ]
        cursor  = db.execute_sql("""
            SELECT employee.name,
       (SELECT salary FROM position WHERE position.id = employee.position_id) as salary,
       (SELECT sum(vacation.days) FROM vacation WHERE vacation.employee_id = employee.id) as vacation,
       (SELECT sum(bonus.amount) FROM bonus WHERE bonus.employee_id = employee.id) as bonus
        FROM employee
        """)
        self.tableWidget_5.setColumnCount(5)
        for rowId, row in enumerate(cursor.fetchall()):
            self.tableWidget_5.setRowCount(self.tableWidget_5.rowCount() + 1)
            self.tableWidget_5.setItem(rowId, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget_5.setItem(rowId, 1, QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget_5.setItem(rowId, 2, QtWidgets.QTableWidgetItem(str(row[2] or 0)))
            vacation_sum = round(float(row[1]) / 29.3 * int(row[2] or 1), 2)
            self.tableWidget_5.setItem(rowId, 3, QtWidgets.QTableWidgetItem(str(vacation_sum)))
            self.tableWidget_5.setItem(rowId, 4, QtWidgets.QTableWidgetItem(str(round(vacation_sum + float(row[3] or 0), 2))))
        self.tableWidget_5.setHorizontalHeaderLabels(cols)


    def add_user(self):
        employee_model.create_employee(
            name=self.lineEdit.text(),
            position=position_model.positions[self.comboBox.currentIndex()]
        )

    def delete_user(self):
        indexes = self.tableView.selectedIndexes()
        if len(indexes) == 0:
            return
        employee_model.delete_employee(indexes[0])

    def fill_user(self):
        indexes = self.tableView.selectedIndexes()
        self.pushButton.setDisabled(True)
        self.pushButton_2.setDisabled(True)
        self.pushButton_3.setDisabled(True)
        self.pushButton_4.setDisabled(False)
        if len(indexes) == 0:
            print('return')
            return
        employee = employee_model.employees[indexes[0].row()]
        self.lineEdit.setText(employee.name)
        self.comboBox.setCurrentIndex(list(position_model.positions).index(employee.position))
        self.editing_index = indexes[0]

    def save_user(self):
        if self.editing_index is None:
            return
        self.pushButton.setDisabled(False)
        self.pushButton_2.setDisabled(False)
        self.pushButton_3.setDisabled(False)
        self.pushButton_4.setDisabled(True)
        employee_model.update_employee(
            self.editing_index,
            name=self.lineEdit.text(),
            position=position_model.positions[self.comboBox.currentIndex()]
        )
        self.lineEdit.clear()
        self.comboBox.setCurrentIndex(0)
        self.editing_index = None
