from PyQt5 import QtCore, Qt
from db import Employee


class EmployeeModel(QtCore.QAbstractTableModel):
    cols = [
        'ФИО',
        'Должность'
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.employees = []
        self.update()

    def update(self):
        self.employees = Employee.select()
        self.layoutChanged.emit()

    def rowCount(self, index):
        return len(self.employees)

    def columnCount(self, index):
        return len(self.cols)

    def headerData(self, column, orientation, role=QtCore.Qt.DisplayRole):
        if not role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        if orientation == QtCore.Qt.Horizontal:
            return QtCore.QVariant(self.cols[column])

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            employee = self.employees[index.row()]
            return [
                employee.name,
                employee.position.name,
            ][index.column()]

    def create_employee(self,
                        name,
                        position):
        Employee.create(
            name=name,
            position=position
        )
        self.update()

    def delete_employee(self, index):
        self.employees[index.row()].delete_instance()
        self.update()

    def update_employee(self,
                        index,
                        name,
                        position):
        employee = self.employees[index.row()]
        employee.name = name
        employee.position = position
        employee.save()
        self.update()


employee_model = EmployeeModel()
