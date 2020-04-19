# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app1.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_APP1(object):
    f_1 = 0
    def setupUi(self, APP1):
        APP1.setObjectName("APP1")
        APP1.resize(424, 249)
        APP1.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(APP1)
        self.centralwidget.setObjectName("centralwidget")

        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setGeometry(QtCore.QRect(90, 70, 75, 23))
        self.b1.setObjectName("b1")
        self.b1.clicked.connect(self._input_)

        self.l1 = QtWidgets.QLineEdit(self.centralwidget)
        self.l1.setGeometry(QtCore.QRect(60, 10, 113, 20))
        self.l1.setObjectName("l1")

        self.l2 = QtWidgets.QLineEdit(self.centralwidget)
        self.l2.setGeometry(QtCore.QRect(60, 40, 113, 20))
        self.l2.setObjectName("l2")

        self.t1 = QtWidgets.QTableWidget(self.centralwidget)
        self.t1.setGeometry(QtCore.QRect(190, 20, 231, 201))
        self.t1.setRowCount(0)
        self.t1.setColumnCount(2)
        self.t1.setObjectName("t1")
        self.t1.horizontalHeader().setCascadingSectionResizes(False)
        self.t1.setHorizontalHeaderLabels(["Name", "Roll"])

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 47, 21))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 47, 13))
        self.label_2.setObjectName("label_2")

        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setGeometry(QtCore.QRect(10, 70, 71, 23))
        self.b2.setObjectName("b2")
        APP1.setCentralWidget(self.centralwidget)

        self.retranslateUi(APP1)
        QtCore.QMetaObject.connectSlotsByName(APP1)

    def _input_(self):
        v1 = self.l1.text()
        v2 = self.l2.text()
        self.l1.clear()
        self.l2.clear()
        self.t1.insertRow(self.f_1)
        self.t1.setItem(self.f_1, 0, QtWidgets.QTableWidgetItem(str(v1)))
        self.t1.setItem(self.f_1, 1, QtWidgets.QTableWidgetItem(str(v2)))
        self.f_1 += 1

    def retranslateUi(self, APP1):
        _translate = QtCore.QCoreApplication.translate
        APP1.setWindowTitle(_translate("APP1", "App1"))
        self.b1.setText(_translate("APP1", "ok"))
        self.label.setText(_translate("APP1", "NAME:"))
        self.label_2.setText(_translate("APP1", "ROLL:"))
        self.b2.setText(_translate("APP1", "view"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    APP1 = QtWidgets.QMainWindow()
    ui = Ui_APP1()
    ui.setupUi(APP1)
    APP1.show()
    sys.exit(app.exec_())
