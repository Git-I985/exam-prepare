# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminWindow(object):
    def setupUi(self, AdminWindow):
        AdminWindow.setObjectName("AdminWindow")
        AdminWindow.resize(883, 730)
        self.centralwidget = QtWidgets.QWidget(AdminWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_13 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout_4.addWidget(self.pushButton_13, 2, 3, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout_4.addWidget(self.pushButton_16, 0, 3, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout_4.addWidget(self.pushButton_14, 2, 2, 1, 1)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.gridLayout_4.addWidget(self.comboBox_3, 0, 1, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout_4.addWidget(self.pushButton_15, 0, 2, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout_4.addWidget(self.lineEdit_7, 0, 0, 1, 1)
        self.tableView_3 = QtWidgets.QTableView(self.groupBox_2)
        self.tableView_3.setObjectName("tableView_3")
        self.gridLayout_4.addWidget(self.tableView_3, 1, 0, 1, 4)
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 5, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 0, 2, 1, 1)
        self.tableView = QtWidgets.QTableView(self.groupBox)
        self.tableView.setObjectName("tableView")
        self.gridLayout_2.addWidget(self.tableView, 1, 1, 1, 5)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 3, 5, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 3, 4, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 4, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout_3.addWidget(self.pushButton_6, 2, 5, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_3.addWidget(self.pushButton_5, 2, 6, 1, 1)
        self.tableView_2 = QtWidgets.QTableView(self.groupBox_3)
        self.tableView_2.setObjectName("tableView_2")
        self.gridLayout_3.addWidget(self.tableView_2, 1, 1, 1, 6)
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_3.addWidget(self.pushButton_7, 0, 6, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_3.addWidget(self.pushButton_8, 0, 5, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_3.addWidget(self.lineEdit_4, 0, 4, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_3.addWidget(self.lineEdit_3, 0, 3, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 2, 2, 1, 3)
        self.gridLayout.addWidget(self.groupBox_3, 0, 1, 1, 1)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_5.addWidget(self.lineEdit_5, 0, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_4)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout_5.addWidget(self.lineEdit_6, 0, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_2.setObjectName("comboBox_2")
        self.gridLayout_5.addWidget(self.comboBox_2, 0, 2, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_5.addWidget(self.pushButton_9, 0, 3, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout_5.addWidget(self.pushButton_10, 0, 4, 1, 1)
        self.tableView_4 = QtWidgets.QTableView(self.groupBox_4)
        self.tableView_4.setObjectName("tableView_4")
        self.gridLayout_5.addWidget(self.tableView_4, 1, 0, 1, 5)
        self.pushButton_12 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout_5.addWidget(self.pushButton_12, 2, 4, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.groupBox_4)
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout_5.addWidget(self.pushButton_11, 2, 3, 1, 1)
        self.gridLayout.addWidget(self.groupBox_4, 1, 1, 1, 1)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButton_17 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout_6.addWidget(self.pushButton_17, 1, 1, 1, 1)
        self.pushButton_18 = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_18.setObjectName("pushButton_18")
        self.gridLayout_6.addWidget(self.pushButton_18, 1, 0, 1, 1)
        self.tableWidget_5 = QtWidgets.QTableWidget(self.groupBox_5)
        self.tableWidget_5.setObjectName("tableWidget_5")
        self.tableWidget_5.setColumnCount(0)
        self.tableWidget_5.setRowCount(0)
        self.gridLayout_6.addWidget(self.tableWidget_5, 0, 0, 1, 2)
        self.gridLayout.addWidget(self.groupBox_5, 2, 0, 1, 2)
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.tableView_6 = QtWidgets.QTableView(self.groupBox_6)
        self.tableView_6.setObjectName("tableView_6")
        self.gridLayout_7.addWidget(self.tableView_6, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_6, 3, 0, 1, 2)
        AdminWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AdminWindow)
        QtCore.QMetaObject.connectSlotsByName(AdminWindow)

    def retranslateUi(self, AdminWindow):
        _translate = QtCore.QCoreApplication.translate
        AdminWindow.setWindowTitle(_translate("AdminWindow", "Панель администратора"))
        self.groupBox_2.setTitle(_translate("AdminWindow", "Отпуска"))
        self.pushButton_13.setText(_translate("AdminWindow", "Изменить"))
        self.pushButton_16.setText(_translate("AdminWindow", "Удалить"))
        self.pushButton_14.setText(_translate("AdminWindow", "Сохранить"))
        self.pushButton_15.setText(_translate("AdminWindow", "Добавить"))
        self.lineEdit_7.setPlaceholderText(_translate("AdminWindow", "Кол-во дней"))
        self.groupBox.setTitle(_translate("AdminWindow", "Пользователи"))
        self.pushButton_2.setText(_translate("AdminWindow", "Удалить"))
        self.lineEdit.setPlaceholderText(_translate("AdminWindow", "ФИО"))
        self.pushButton_3.setText(_translate("AdminWindow", "Изменить"))
        self.pushButton_4.setText(_translate("AdminWindow", "Сохранить"))
        self.pushButton.setText(_translate("AdminWindow", "Добавить"))
        self.groupBox_3.setTitle(_translate("AdminWindow", "Должности"))
        self.pushButton_6.setText(_translate("AdminWindow", "Сохранить"))
        self.pushButton_5.setText(_translate("AdminWindow", "Изменить"))
        self.pushButton_7.setText(_translate("AdminWindow", "Удалить"))
        self.pushButton_8.setText(_translate("AdminWindow", "Добавить"))
        self.lineEdit_4.setPlaceholderText(_translate("AdminWindow", "Зарплата"))
        self.lineEdit_3.setPlaceholderText(_translate("AdminWindow", "Отпускных дней"))
        self.lineEdit_2.setPlaceholderText(_translate("AdminWindow", "Название"))
        self.groupBox_4.setTitle(_translate("AdminWindow", "Надбавки"))
        self.lineEdit_5.setPlaceholderText(_translate("AdminWindow", "Размер"))
        self.lineEdit_6.setPlaceholderText(_translate("AdminWindow", "Название"))
        self.pushButton_9.setText(_translate("AdminWindow", "Добавить"))
        self.pushButton_10.setText(_translate("AdminWindow", "Удалить"))
        self.pushButton_12.setText(_translate("AdminWindow", "Изменить"))
        self.pushButton_11.setText(_translate("AdminWindow", "Сохранить"))
        self.groupBox_5.setTitle(_translate("AdminWindow", "Расчет выплат"))
        self.pushButton_17.setText(_translate("AdminWindow", "Расчитать выплаты"))
        self.pushButton_18.setText(_translate("AdminWindow", "Сохранить/записать"))
        self.groupBox_6.setTitle(_translate("AdminWindow", "Выплаты"))
