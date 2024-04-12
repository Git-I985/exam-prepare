from PyQt5 import QtCore, Qt
from db import Position


class PositionModel(QtCore.QAbstractTableModel):
    cols = [
        'Название',
        'Зарплата',
        'Отпускных дней'
    ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.positions = []
        self.update()

    def update(self):
        self.positions = Position.select()
        self.layoutChanged.emit()

    def rowCount(self, index):
        return len(self.positions)

    def columnCount(self, index):
        return len(self.cols)

    def headerData(self, column, orientation, role=QtCore.Qt.DisplayRole):
        if not role == QtCore.Qt.DisplayRole:
            return QtCore.QVariant()
        if orientation == QtCore.Qt.Horizontal:
            return QtCore.QVariant(self.cols[column])

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            position = self.positions[index.row()]
            return [
                position.name,
                position.salary,
                position.vacation_days
            ][index.column()]

    def create_position(self,
                        name,
                        salary, vacation_days):
        Position.create(
            name=name,
            salary=salary,
            vacation_days=vacation_days
        )
        self.update()

    def delete_position(self, index):
        self.positions[index.row()].delete_instance()
        self.update()

    def update_position(self,
                        index,
                        name,
                        salary, vacation_days):
        position = self.positions[index.row()]
        position.name = name
        position.salary = salary
        position.vacation_days = vacation_days
        position.save()
        self.update()


position_model = PositionModel()
