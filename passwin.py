# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passwin.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_PassWin(object):
    def GET_DATA(self):
        db=sqlite3.connect("C:\Python36\PROJECT\Password Buddy\PassDB.db")
        cursor=db.cursor()

        command="SELECT * FROM passwords"
        result=cursor.execute(command)
        self.tableWidget.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))


    def setupUi(self, PassWin):
        PassWin.setObjectName("PassWin")
        PassWin.resize(335, 403)
        PassWin.setMinimumSize(QtCore.QSize(335, 403))
        PassWin.setMaximumSize(QtCore.QSize(335, 403))
        self.centralwidget = QtWidgets.QWidget(PassWin)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Adobe Garamond Pro Bold")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.tableWidget.setFont(font)
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout.addWidget(self.tableWidget)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.GET_DATA)
        
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI")
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(PassWin.close)

        self.verticalLayout.addWidget(self.pushButton_2)
        PassWin.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(PassWin)
        QtCore.QMetaObject.connectSlotsByName(PassWin)

    def retranslateUi(self, PassWin):
        _translate = QtCore.QCoreApplication.translate
        PassWin.setWindowTitle(_translate("PassWin", "Saved Password"))
        self.pushButton.setText(_translate("PassWin", "Load"))
        self.pushButton_2.setText(_translate("PassWin", "Exit"))
        self.label.setText(_translate("PassWin", "SAVED PASSWORDS"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PassWin = QtWidgets.QMainWindow()
    ui = Ui_PassWin()
    ui.setupUi(PassWin)
    PassWin.show()
    sys.exit(app.exec_())