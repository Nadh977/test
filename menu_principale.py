# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os
import subprocess
from time import sleep


class Ui_Dialog(object):
    def __init__(self):
        self.choice = 2
        self.server = None
        self.client = None
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(783, 582)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 60, 711, 471))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.clientPlainText = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.clientPlainText.setReadOnly(True)
        self.clientPlainText.setObjectName("clientPlainText")
        self.verticalLayout_2.addWidget(self.clientPlainText)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_2.addWidget(self.pushButton_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.serverPlainText = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget)
        self.serverPlainText.setReadOnly(True)
        self.serverPlainText.setObjectName("serverPlainText")
        self.verticalLayout_3.addWidget(self.serverPlainText)
        self.pushButton_4 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Interface Principale Unix"))

        self.pushButton_4.setText(_translate("Dialog", "Serveur"))
        self.pushButton_4.clicked.connect(self.init_serveur)

        self.pushButton.setText(_translate("Dialog", "Sockets"))
        self.pushButton.setStyleSheet("background-color: cyan")
        self.pushButton.clicked.connect(self.sockets)

        self.pushButton_2.setText(_translate("Dialog", "Tubes"))
        self.pushButton_2.clicked.connect(self.tubes)

        self.pushButton_3.setText(_translate("Dialog", "Client"))
        self.pushButton_3.clicked.connect(self.init_client)

    def init_serveur(self):
        outputserveur = open("outputserveur.txt", "w+")

        outputserveur.write("")
        if self.server is not None:
            self.server.kill()
            self.server = None
        if self.choice == 1:
            self.server = subprocess.Popen(['./Server'], cwd='./Tubes_Nomees', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else:
            self.server = subprocess.Popen(['./Server'], cwd='./Sockets', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        sleep(0.5)
        self.serverPlainText.setPlainText(outputserveur.read())
        outputserveur.close()


    def init_client(self):
        if self.server is None:
            self.clientPlainText.setPlainText("Server is not running...")
            return

        if self.client is not None:
            self.client.kill()

        if self.choice == 1: # PIPE (Project 1)
            self.client = subprocess.Popen(['./Client'], cwd='./Tubes_Nomees', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        else: # TCP Socket (Project 2)
            self.client = subprocess.Popen(['./Client'], cwd='./Sockets', stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Connexion au process client
        try:
            client_stdout, client_stderr = self.client.communicate(timeout=2)
        except subprocess.TimeoutExpired:
            self.client.kill()
            self.clientPlainText.setPlainText("Client timed out...")
            return
        if self.client.poll() is None:
            self.client.kill()
            self.clientPlainText.setPlainText("Client timed out...")
            return

        # decoder l'output du client
        client_output = client_stdout.decode("utf-8")
        client_error = client_stderr.decode("utf-8")

        # affichage de l'output
        self.clientPlainText.setPlainText(client_output)
        if client_error:
            self.clientPlainText.setPlainText(client_error)

        outputserveur = open("outputserveur.txt", "r")
        self.serverPlainText.setPlainText(outputserveur.read())
        outputserveur.close()

    def sockets(self):
        if self.server is not None:
            self.server.kill()
            self.server = None
        self.choice = 2
        self.pushButton.setStyleSheet("background-color: cyan")

        self.pushButton_2.setStyleSheet("background-color: white")

        # vider le contenu des zone de texte
        self.serverPlainText.setPlainText("")
        self.clientPlainText.setPlainText("")
        outputserveur = open("outputserveur.txt", "w")
        # empty the server log file
        outputserveur.write("")
        outputserveur.close()


    def tubes(self):
        if self.server is not None:
            self.server.kill()
            self.server = None
        self.choice = 1
        self.pushButton_2.setStyleSheet("background-color: cyan")

        self.pushButton.setStyleSheet("background-color: white")

        # vider le contenu des zones de texte
        self.serverPlainText.setPlainText("")
        self.clientPlainText.setPlainText("")
        outputserveur = open("outputserveur.txt", "w")
        # empty the server log file
        outputserveur.write("")
        outputserveur.close()





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())