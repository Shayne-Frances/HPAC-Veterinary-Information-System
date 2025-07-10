from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 225)
        Dialog.setMinimumSize(QtCore.QSize(450, 225))
        Dialog.setMaximumSize(QtCore.QSize(450, 225))
        Dialog.setStyleSheet("background-color: #D8EDF3;")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_3 = QtWidgets.QFrame(Dialog)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setMinimumSize(QtCore.QSize(100, 100))
        self.label_2.setMaximumSize(QtCore.QSize(100, 100))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("HPAC IS/Staff.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.frame_2)
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setMinimumSize(QtCore.QSize(280, 0))
        self.frame.setMaximumSize(QtCore.QSize(280, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setMinimumSize(QtCore.QSize(260, 140))
        self.frame_4.setMaximumSize(QtCore.QSize(260, 140))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.first = QtWidgets.QLabel(self.frame_4)
        self.first.setStyleSheet("QLabel {\n"
"    font-family: \"Merriweather Sans\";\n"
"    font: bold;\n"
"    font-size: 14px;\n"
"    color: #072A42;\n"
"}\n"
"")
        self.first.setAlignment(QtCore.Qt.AlignCenter)
        self.first.setWordWrap(True)
        self.first.setObjectName("first")
        self.verticalLayout_2.addWidget(self.first)
        self.second = QtWidgets.QLabel(self.frame_4)
        self.second.setStyleSheet("QLabel {\n"
"    font-family: \"Merriweather Sans\";\n"
"    font: bold;\n"
"    font-size: 14px;\n"
"    color: #072A42;\n"
"}\n"
"")
        self.second.setAlignment(QtCore.Qt.AlignCenter)
        self.second.setWordWrap(True)
        self.second.setObjectName("second")
        self.verticalLayout_2.addWidget(self.second)
        self.third = QtWidgets.QLabel(self.frame_4)
        self.third.setStyleSheet("QLabel {\n"
"    font-family: \"Merriweather Sans\";\n"
"    font: bold;\n"
"    font-size: 14px;\n"
"    color: #072A42;\n"
"}\n"
"")
        self.third.setAlignment(QtCore.Qt.AlignCenter)
        self.third.setWordWrap(True)
        self.third.setObjectName("third")
        self.verticalLayout_2.addWidget(self.third)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.buttframe = QtWidgets.QFrame(self.frame)
        self.buttframe.setMinimumSize(QtCore.QSize(240, 45))
        self.buttframe.setMaximumSize(QtCore.QSize(260, 45))
        self.buttframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttframe.setObjectName("buttframe")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.buttframe)
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.nobutt = QtWidgets.QPushButton(self.buttframe)
        self.nobutt.setMinimumSize(QtCore.QSize(90, 25))
        self.nobutt.setMaximumSize(QtCore.QSize(90, 25))
        self.nobutt.setStyleSheet("QPushButton {\n"
"    font: Merriweather Sans;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    color: #072A42;\n"
"    background-color: #fafafa;\n"
"    border: 2px solid #072A42;\n"
"    border-radius: 6px;\n"
"    padding: 3px;\n"
"    width: 80px;\n"
"    height: 15px;\n"
"            }\n"
"\n"
"QPushButton:hover {\n"
"            background-color: #c1c8d4;  \n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: #DD5C6D;\n"
"        }\n"
"")
        self.nobutt.setObjectName("nobutt")
        self.horizontalLayout.addWidget(self.nobutt)
        self.yesbutt = QtWidgets.QPushButton(self.buttframe)
        self.yesbutt.setMinimumSize(QtCore.QSize(90, 25))
        self.yesbutt.setMaximumSize(QtCore.QSize(90, 25))
        self.yesbutt.setStyleSheet("QPushButton {\n"
"    font: Merriweather Sans;\n"
"    font-size: 12px;\n"
"    font-weight: bold;\n"
"    color: #072A42;\n"
"    background-color: #DA99A5;\n"
"    border: 2px solid #072A42;\n"
"    border-radius: 6px;\n"
"    padding: 3px;\n"
"    width: 80px;\n"
"    height: 15px;\n"
"            }\n"
"\n"
"QPushButton:hover {\n"
"            background-color: #c1c8d4;  \n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: #DD5C6D;\n"
"        }\n"
"")
        self.yesbutt.setObjectName("yesbutt")
        self.horizontalLayout.addWidget(self.yesbutt)
        self.verticalLayout_3.addWidget(self.buttframe)
        self.horizontalLayout_3.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.first.setText(_translate("Dialog", "Possible duplicate entry found:"))
        self.second.setText(_translate("Dialog", "{first_name} + {last_name} : {ID}"))
        self.third.setText(_translate("Dialog", "Proceed to add entry?"))
        self.nobutt.setText(_translate("Dialog", "Nopers!"))
        self.yesbutt.setText(_translate("Dialog", "Yep!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
