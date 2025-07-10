from PyQt5 import QtCore, QtGui, QtWidgets
from Pictures import Hpac_rc


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 225)
        Dialog.setMinimumSize(QtCore.QSize(450, 225))
        Dialog.setMaximumSize(QtCore.QSize(450, 225))
        Dialog.setStyleSheet("background-color: #D8EDF3;")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
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
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/Staff.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(self.frame_3)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox = QtWidgets.QCheckBox(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox.sizePolicy().hasHeightForWidth())
        self.checkBox.setSizePolicy(sizePolicy)
        self.checkBox.setMinimumSize(QtCore.QSize(15, 50))
        self.checkBox.setMaximumSize(QtCore.QSize(15, 50))
        self.checkBox.setStyleSheet("QCheckBox {\n"
"    font-family: \"Merriweather Sans\";\n"
"    font: bold;\n"
"    font-size: 10px;\n"
"    color: #072A42;\n"
"}\n"
"")
        self.checkBox.setText("")
        self.checkBox.setTristate(False)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_3.addWidget(self.checkBox)
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setStyleSheet("QLabel {\n"
"    font-family: \"Merriweather Sans\";\n"
"    font: italic;\n"
"    font-size: 12px;\n"
"    color: #072A42;\n"
"}\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.verticalLayout.addWidget(self.frame_4)
        self.horizontalLayout_4.addWidget(self.frame_3)
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setMinimumSize(QtCore.QSize(250, 0))
        self.frame.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setMinimumSize(QtCore.QSize(240, 150))
        self.label.setMaximumSize(QtCore.QSize(240, 150))
        self.label.setStyleSheet("QLabel {\n"
"    font-family: \"Merriweather Sans\";\n"
"    font: bold;\n"
"    font-size: 15px;\n"
"    color: #072A42;\n"
"}\n"
"")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.buttframe = QtWidgets.QFrame(self.frame)
        self.buttframe.setMinimumSize(QtCore.QSize(240, 45))
        self.buttframe.setMaximumSize(QtCore.QSize(240, 45))
        self.buttframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttframe.setObjectName("buttframe")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.buttframe)
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
        self.verticalLayout_2.addWidget(self.buttframe)
        self.horizontalLayout_4.addWidget(self.frame)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "Don\'t show this dialog again during this session."))
        self.label.setText(_translate("Dialog", "Are you sure you want to update this staff\'s information?                                   Changes cannot be undone unless you edit it again! （• ˕ •マ"))
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
