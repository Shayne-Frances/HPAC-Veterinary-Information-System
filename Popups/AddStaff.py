from PyQt5 import QtCore, QtGui, QtWidgets
from Pictures import Hpac_rc
from Database_Manager.database import DBManager
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QRegularExpressionValidator, QIcon
from PyQt5.QtCore import QRegularExpression


#TINTIN WAS HERE - import what's needed for the warning
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication

#TINTIN WAS HERE to import those needed for updating
from Warning.updcon import UpdateCon
from PyQt5.QtWidgets import QDialog
import globalsession

#TINTIN WAS HERE - import duplicate? popup
from Warning.dup import DupCon
import difflib


class AddStaffControl(QtWidgets.QDialog):
    def __init__(self, parent=None, existing_data=None, skip_update_confirmation=False):
        super().__init__(parent)



#TINTIN WAS HERE to pass existing data if naa
        self.existing_data = existing_data



# TINTIN WAS HERE to initialize the confirmation part from global session
        self.skip_update_confirmation = skip_update_confirmation 

        self.setObjectName("Dialog")
        self.resize(428, 800)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        self.setMinimumSize(QtCore.QSize(400, 800))
        self.setMaximumSize(QtCore.QSize(500, 800))
        self.setStyleSheet("QDialog {\n"
"    background-color: #D8EDF3;\n"
"}\n"
"")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.alltopframe = QtWidgets.QFrame(self)
        self.alltopframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.alltopframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.alltopframe.setObjectName("alltopframe")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.alltopframe)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.titlelogoframe = QtWidgets.QFrame(self.alltopframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titlelogoframe.sizePolicy().hasHeightForWidth())
        self.titlelogoframe.setSizePolicy(sizePolicy)
        self.titlelogoframe.setMinimumSize(QtCore.QSize(250, 100))
        self.titlelogoframe.setMaximumSize(QtCore.QSize(210, 80))
        self.titlelogoframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.titlelogoframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.titlelogoframe.setObjectName("titlelogoframe")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.titlelogoframe)
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stafflogo = QtWidgets.QLabel(self.titlelogoframe)
        self.stafflogo.setMaximumSize(QtCore.QSize(90, 90))
        self.stafflogo.setText("")
        self.stafflogo.setPixmap(QtGui.QPixmap(":/icons/Staff.png"))
        self.stafflogo.setScaledContents(True)
        self.stafflogo.setObjectName("stafflogo")
        self.horizontalLayout.addWidget(self.stafflogo)
        self.addstafftitle = QtWidgets.QLabel(self.titlelogoframe)
        self.addstafftitle.setStyleSheet("QLabel {\n"
"    font: Merriweather Sans;\n"
"    font: bold;\n"
"    font-size: 25px;\n"
"    color: #072A42;\n"
"}")
        self.addstafftitle.setObjectName("addstafftitle")
        self.horizontalLayout.addWidget(self.addstafftitle)
        self.horizontalLayout_2.addWidget(self.titlelogoframe)
        spacerItem1 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.alltopframe)
        self.allmiddleframe = QtWidgets.QFrame(self)
        self.allmiddleframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.allmiddleframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.allmiddleframe.setObjectName("allmiddleframe")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.allmiddleframe)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.IAFrame = QtWidgets.QFrame(self.allmiddleframe)
        self.IAFrame.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.IAFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.IAFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.IAFrame.setObjectName("IAFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.IAFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.I1AFrame = QtWidgets.QFrame(self.IAFrame)
        self.I1AFrame.setMinimumSize(QtCore.QSize(0, 55))
        self.I1AFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I1AFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I1AFrame.setObjectName("I1AFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.I1AFrame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.I1A = QtWidgets.QLabel(self.I1AFrame)
        self.I1A.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.I1A.setStyleSheet("QLabel {\n"
"    font: Merriweather Sans;\n"
"    font: bold;\n"
"    font-size: 20px;\n"
"    color: #072A42;\n"
"}")
        self.I1A.setObjectName("I1A")
        self.horizontalLayout_3.addWidget(self.I1A)
        self.verticalLayout.addWidget(self.I1AFrame)
        self.I2AFrame = QtWidgets.QFrame(self.IAFrame)
        self.I2AFrame.setMinimumSize(QtCore.QSize(0, 55))
        self.I2AFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I2AFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I2AFrame.setObjectName("I2AFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.I2AFrame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.I2A = QtWidgets.QLabel(self.I2AFrame)
        self.I2A.setStyleSheet("QLabel {\n"
"    font: Merriweather Sans;\n"
"    font: bold;\n"
"    font-size: 20px;\n"
"    color: #072A42;\n"
"}")
        self.I2A.setObjectName("I2A")
        self.horizontalLayout_4.addWidget(self.I2A)
        self.verticalLayout.addWidget(self.I2AFrame)
        self.I3AFrame = QtWidgets.QFrame(self.IAFrame)
        self.I3AFrame.setMinimumSize(QtCore.QSize(0, 55))
        self.I3AFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I3AFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I3AFrame.setObjectName("I3AFrame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.I3AFrame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.I3A = QtWidgets.QLabel(self.I3AFrame)
        self.I3A.setStyleSheet("QLabel {\n"
"    font: Merriweather Sans;\n"
"    font: bold;\n"
"    font-size: 20px;\n"
"    color: #072A42;\n"
"}")
        self.I3A.setObjectName("I3A")
        self.horizontalLayout_5.addWidget(self.I3A)
        self.verticalLayout.addWidget(self.I3AFrame)
        self.I4AFrame = QtWidgets.QFrame(self.IAFrame)
        self.I4AFrame.setMinimumSize(QtCore.QSize(0, 55))
        self.I4AFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I4AFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I4AFrame.setObjectName("I4AFrame")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.I4AFrame)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.I4A = QtWidgets.QLabel(self.I4AFrame)
        self.I4A.setStyleSheet("QLabel {\n"
"    font: Merriweather Sans;\n"
"    font: bold;\n"
"    font-size: 20px;\n"
"    color: #072A42;\n"
"}")
        self.I4A.setObjectName("I4A")
        self.horizontalLayout_13.addWidget(self.I4A)
        self.verticalLayout.addWidget(self.I4AFrame)
        self.I5AFrame = QtWidgets.QFrame(self.IAFrame)
        self.I5AFrame.setMinimumSize(QtCore.QSize(0, 55))
        self.I5AFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I5AFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I5AFrame.setObjectName("I5AFrame")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.I5AFrame)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.I5A = QtWidgets.QLabel(self.I5AFrame)
        self.I5A.setStyleSheet("QLabel {\n"
"    font: Merriweather Sans;\n"
"    font: bold;\n"
"    font-size: 20px;\n"
"    color: #072A42;\n"
"}")
        self.I5A.setObjectName("I5A")
        self.horizontalLayout_14.addWidget(self.I5A)
        self.verticalLayout.addWidget(self.I5AFrame)
        self.I6AFrame = QtWidgets.QFrame(self.IAFrame)
        self.I6AFrame.setMinimumSize(QtCore.QSize(0, 50))
        self.I6AFrame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.I6AFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I6AFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I6AFrame.setObjectName("I6AFrame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.I6AFrame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.I6A = QtWidgets.QLabel(self.I6AFrame)
        self.I6A.setStyleSheet("QLabel {\n"
"    font: Merriweather Sans;\n"
"    font: bold;\n"
"    font-size: 20px;\n"
"    color: #072A42;\n"
"}")
        self.I6A.setObjectName("I6A")
        self.horizontalLayout_6.addWidget(self.I6A)
        self.verticalLayout.addWidget(self.I6AFrame)
        self.I7AFrame = QtWidgets.QFrame(self.IAFrame)
        self.I7AFrame.setMinimumSize(QtCore.QSize(0, 55))
        self.I7AFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I7AFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I7AFrame.setObjectName("I7AFrame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.I7AFrame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.I7A = QtWidgets.QLabel(self.I7AFrame)
        self.I7A.setStyleSheet("QLabel {\n"
"    font: Merriweather Sans;\n"
"    font: bold;\n"
"    font-size: 20px;\n"
"    color: #072A42;\n"
"}")
        self.I7A.setObjectName("I7A")
        self.horizontalLayout_7.addWidget(self.I7A)
        self.verticalLayout.addWidget(self.I7AFrame)
        self.I8AFrame = QtWidgets.QFrame(self.IAFrame)
        self.I8AFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I8AFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I8AFrame.setObjectName("I8AFrame")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.I8AFrame)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.I8A = QtWidgets.QLabel(self.I8AFrame)
        self.I8A.setStyleSheet("QLabel {\n"
"    font: Merriweather Sans;\n"
"    font: bold;\n"
"    font-size: 20px;\n"
"    color: #072A42;\n"
"}")
        self.I8A.setObjectName("I8A")
        self.horizontalLayout_19.addWidget(self.I8A)
        self.verticalLayout.addWidget(self.I8AFrame)
        self.horizontalLayout_17.addWidget(self.IAFrame)
        self.IBFrame = QtWidgets.QFrame(self.allmiddleframe)
        self.IBFrame.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.IBFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.IBFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.IBFrame.setObjectName("IBFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.IBFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.I1BFrame = QtWidgets.QFrame(self.IBFrame)
        self.I1BFrame.setMinimumSize(QtCore.QSize(0, 55))
        self.I1BFrame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.I1BFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I1BFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I1BFrame.setObjectName("I1BFrame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.I1BFrame)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.I1B = QtWidgets.QLineEdit(self.I1BFrame)
        self.I1B.setMinimumSize(QtCore.QSize(0, 40))
        self.I1B.setStyleSheet("QLineEdit {\n"
"    font-family: \"Merriweather Sans\";\n"
"    font: bold;\n"
"    font-size: 18px;\n"
"    color: #072A42;\n"
"    background-color: #fafafa;\n"
"    border: 2px solid #072A42;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #DD5C6D;\n"
"    font-style: italic;\n"
"}\n"
"")
        self.I1B.setObjectName("I1B")
        self.horizontalLayout_8.addWidget(self.I1B)
        self.verticalLayout_2.addWidget(self.I1BFrame)
        self.I2BFrame = QtWidgets.QFrame(self.IBFrame)
        self.I2BFrame.setMinimumSize(QtCore.QSize(0, 55))
        self.I2BFrame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.I2BFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I2BFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I2BFrame.setObjectName("I2BFrame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.I2BFrame)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.I2B = QtWidgets.QLineEdit(self.I2BFrame)
        self.I2B.setMinimumSize(QtCore.QSize(0, 40))
        self.I2B.setStyleSheet("QLineEdit {\n"
"    font-family: \"Merriweather Sans\";\n"
"    font: bold;\n"
"    font-size: 18px;\n"
"    color: #072A42;\n"
"    background-color: #fafafa;\n"
"    border: 2px solid #072A42;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #DD5C6D;\n"
"    font-style: italic;\n"
"}\n"
"")
        self.I2B.setObjectName("I2B")
        self.horizontalLayout_9.addWidget(self.I2B)
        self.verticalLayout_2.addWidget(self.I2BFrame)
        self.I3BFrame = QtWidgets.QFrame(self.IBFrame)
        self.I3BFrame.setMinimumSize(QtCore.QSize(0, 55))
        self.I3BFrame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.I3BFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I3BFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I3BFrame.setObjectName("I3BFrame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.I3BFrame)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.I3B = QtWidgets.QComboBox(self.I3BFrame)
        self.I3B.setMinimumSize(QtCore.QSize(0, 40))
        self.I3B.setStyleSheet("QComboBox {\n"
"    font-family: \"Merriweather Sans\";\n"
"    color: #D8EDF3;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    padding: 5px;\n"
"    border: 2px solid #072A42;\n"
"    border-radius: 5px;\n"
"    background-color: #DA99A5;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left: 1px solid #ccc;\n"
"    background-color: #fafafa;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/arrow down.png);\n"
"    width: 23px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #fafafa;\n"
"    color: #072A42;\n"
"    selection-background-color: #DA99A5;\n"
"    selection-color: #fafafa ;\n"
"    outline:#DA99A5;\n"
"}\n"
"")
        self.I3B.setEditable(True)
        self.I3B.setObjectName("I3B")
        self.I3B.addItem("")
        self.I3B.addItem("")
        self.I3B.addItem("")
        self.I3B.addItem("")
        self.I3B.addItem("")
        self.I3B.addItem("")
        self.horizontalLayout_10.addWidget(self.I3B)
        self.verticalLayout_2.addWidget(self.I3BFrame)
        self.I4BFrame = QtWidgets.QFrame(self.IBFrame)
        self.I4BFrame.setMinimumSize(QtCore.QSize(0, 55))
        self.I4BFrame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.I4BFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I4BFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I4BFrame.setObjectName("I4BFrame")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.I4BFrame)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.I4B = QtWidgets.QLineEdit(self.I4BFrame)
        self.I4B.setMinimumSize(QtCore.QSize(0, 40))
        self.I4B.setStyleSheet("QLineEdit {\n"
"    font-family: \"Merriweather Sans\";\n"
"    font: bold;\n"
"    font-size: 18px;\n"
"    color: #072A42;\n"
"    background-color: #fafafa;\n"
"    border: 2px solid #072A42;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #DD5C6D;\n"
"    font-style: italic;\n"
"}\n"
"")
        self.I4B.setReadOnly(True)
        self.I4B.setObjectName("I4B")
        self.horizontalLayout_15.addWidget(self.I4B)
        self.verticalLayout_2.addWidget(self.I4BFrame)
        self.I5BCFrame = QtWidgets.QFrame(self.IBFrame)
        self.I5BCFrame.setMinimumSize(QtCore.QSize(0, 55))
        self.I5BCFrame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.I5BCFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I5BCFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I5BCFrame.setObjectName("I5BCFrame")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.I5BCFrame)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.I5C = QtWidgets.QLineEdit(self.I5BCFrame)
        self.I5C.setMinimumSize(QtCore.QSize(0, 40))
        self.I5C.setStyleSheet("QLineEdit {\n"
"    font-family: \"Merriweather Sans\";\n"
"    font: bold;\n"
"    font-size: 20px;\n"
"    color: #072A42;\n"
"    background-color: #fafafa;\n"
"    border: 2px solid #072A42;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #DD5C6D;\n"
"    font-style: italic;\n"
"}\n"
"")
        self.I5C.setReadOnly(True)
        self.I5C.setObjectName("I5C")
        self.horizontalLayout_16.addWidget(self.I5C)
        self.I5B = QtWidgets.QLabel(self.I5BCFrame)
        self.I5B.setMinimumSize(QtCore.QSize(0, 40))
        self.I5B.setStyleSheet("QLabel {\n"
"    font-family: \"Merriweather Sans\";\n"
"    font: bold;\n"
"    font-size: 18px;\n"
"    color: #072A42;\n"
"\n"
"}\n"
"\n"
"")
        self.I5B.setObjectName("I5B")
        self.horizontalLayout_16.addWidget(self.I5B)
        self.verticalLayout_2.addWidget(self.I5BCFrame)
        self.I6BFrame = QtWidgets.QFrame(self.IBFrame)
        self.I6BFrame.setMinimumSize(QtCore.QSize(0, 55))
        self.I6BFrame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.I6BFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I6BFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I6BFrame.setObjectName("I6BFrame")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.I6BFrame)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.I6B = QtWidgets.QLineEdit(self.I6BFrame)
        self.I6B.setMinimumSize(QtCore.QSize(0, 40))
        self.I6B.setStyleSheet("QLineEdit {\n"
"    font-family: \"Merriweather Sans\";\n"
"    font: bold;\n"
"    font-size: 18px;\n"
"    color: #072A42;\n"
"    background-color: #fafafa;\n"
"    border: 2px solid #072A42;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QLineEdit::placeholder {\n"
"    color: #DD5C6D;\n"
"    font-style: italic;\n"
"}\n"
"")
        self.I6B.setObjectName("I6B")
        self.horizontalLayout_11.addWidget(self.I6B)
        self.verticalLayout_2.addWidget(self.I6BFrame)
        self.I7BFrame = QtWidgets.QFrame(self.IBFrame)
        self.I7BFrame.setMinimumSize(QtCore.QSize(0, 55))
        self.I7BFrame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.I7BFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I7BFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I7BFrame.setObjectName("I7BFrame")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.I7BFrame)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.I7B = QtWidgets.QDateEdit(self.I7BFrame)
        self.I7B.setMinimumSize(QtCore.QSize(0, 40))
        self.I7B.setStyleSheet("QDateEdit {\n"
"    font-family: \"Merriweather Sans\";\n"
"    font: bold;\n"
"    font-size: 18px;\n"
"    color: #DA99A5;\n"
"    background-color: #fafafa;\n"
"    border: 2px solid #072A42;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QDateEdit::placeholder {\n"
"    color: #DD5C6D;\n"
"    font-style: italic;\n"
"}\n"
"")
        self.I7B.setObjectName("I7B")
        self.horizontalLayout_12.addWidget(self.I7B)
        self.verticalLayout_2.addWidget(self.I7BFrame)
        self.I8BFrame = QtWidgets.QFrame(self.IBFrame)
        self.I8BFrame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.I8BFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I8BFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I8BFrame.setObjectName("I8BFrame")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.I8BFrame)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.I8B = QtWidgets.QComboBox(self.I8BFrame)
        self.I8B.setMinimumSize(QtCore.QSize(0, 40))
        self.I8B.setMaximumSize(QtCore.QSize(16777215, 35))
        self.I8B.setStyleSheet("QComboBox {\n"
"    font-family: \"Merriweather Sans\";\n"
"    color: #D8EDF3;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    padding: 5px;\n"
"    border: 2px solid #072A42;\n"
"    border-radius: 5px;\n"
"    background-color: #DA99A5;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px;\n"
"    border-left: 1px solid #ccc;\n"
"    background-color: #fafafa;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"    image: url(:/icons/arrow down.png);\n"
"    width: 23px;\n"
"    height: 25px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background-color: #fafafa;\n"
"    color: #072A42;\n"
"    selection-background-color: #DA99A5;\n"
"    selection-color: #fafafa ;\n"
"    outline:#DA99A5;\n"
"}\n"
"")
        self.I8B.setObjectName("I8B")
        self.I8B.addItem("")
        self.I8B.addItem("")
        self.I8B.addItem("")
        self.I8B.addItem("")
        self.horizontalLayout_20.addWidget(self.I8B)
        self.verticalLayout_2.addWidget(self.I8BFrame)
        self.horizontalLayout_17.addWidget(self.IBFrame)
        self.verticalLayout_3.addWidget(self.allmiddleframe)
        self.allbotframe = QtWidgets.QFrame(self)
        self.allbotframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.allbotframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.allbotframe.setObjectName("allbotframe")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.allbotframe)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        spacerItem2 = QtWidgets.QSpacerItem(175, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem2)
        self.buttframe = QtWidgets.QFrame(self.allbotframe)
        self.buttframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.buttframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.buttframe.setObjectName("buttframe")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.buttframe)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.addbutt = QtWidgets.QPushButton(self.buttframe)
        self.addbutt.setStyleSheet("QPushButton {\n"
"    font: Merriweather Sans;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    color: #072A42;\n"
"    background-color: #fafafa;\n"
"    border: 2px solid #072A42;\n"
"    border-radius: 6px;\n"
"    padding: 3px;\n"
"    width: 80px;\n"
"    height: 20px;\n"
"            }\n"
"\n"
"QPushButton:hover {\n"
"            background-color: #c1c8d4;  \n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: #DD5C6D;\n"
"        }\n"
"")
        self.addbutt.setObjectName("addbutt")
        self.horizontalLayout_18.addWidget(self.addbutt)
        self.cancellbutt = QtWidgets.QPushButton(self.buttframe)
        self.cancellbutt.setStyleSheet("QPushButton {\n"
"    font: Merriweather Sans;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    color: #072A42;\n"
"    background-color: #fafafa;\n"
"    border: 2px solid #072A42;\n"
"    border-radius: 6px;\n"
"    padding: 3px;\n"
"    width: 80px;\n"
"    height: 20px;\n"
"            }\n"
"\n"
"QPushButton:hover {\n"
"            background-color: #c1c8d4;  \n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: #DD5C6D;\n"
"        }\n"
"")
        self.cancellbutt.setObjectName("cancellbutt")
        self.horizontalLayout_18.addWidget(self.cancellbutt)
        self.horizontalLayout_21.addWidget(self.buttframe)
        self.verticalLayout_3.addWidget(self.allbotframe)



# TINTIN WAS HERE to change the popup's window icon
        self.setWindowIcon(QIcon("Pictures/Staff.png"))



# TINTIN WAS HERE - this is for the prc, make it editable (connecting)
        self.I3B.currentTextChanged.connect(self.prcedit)



# TINTIN WAS HERE - AUTO GENERATE STAFF ID
        try:
                db = DBManager()
                db.connect_DB()
                kuryente = db.kuryente
                cable = db.cable

                kuryente.execute("SELECT MAX(Staff_ID) FROM stafftb")
                result = kuryente.fetchone()[0]

                if result is None:
                        next_id_number = 1
                else:
                        next_id_number = int(result.split('-')[1]) + 1

                formatted_id = f"{next_id_number:04d}"

                self.I5C.setText(formatted_id)
                self.I5C.setReadOnly(True)

                kuryente.close()
                cable.close()

        except Exception as e:
                print("Error generating Staff ID:", e)
                self.I5C.setText("ST-0001") 

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)



#TINTIN WAS HERE to connect the buttons to their functions
        self.addbutt.clicked.connect(self.savestaff)
        self.cancellbutt.clicked.connect(self.cancel)



#TINTIN was here to initialize the edit part, also change some labels and other stuff in the dialog
        self.existing_data = existing_data
        if self.existing_data:
                self.fillanswers()
                self.addbutt.setText("Update")
                self.addstafftitle.setText("Edit Staff")
                self.setWindowTitle("HPAC VIS - Edit Staff")



#TINTIN WAS HERE to limit the characters each answer sa pop-up
        self.I1B.setMaxLength(50)  
        self.I2B.setMaxLength(50)
        self.I3B.lineEdit().setMaxLength(50)  
        self.I4B.setMaxLength(10)   
        self.I6B.setMaxLength(11) 
        self.I6B.setValidator(QRegularExpressionValidator(QRegularExpression(r"\d{0,11}")))







    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate











# TINTIN WAS HERE to manually change the window name
        Dialog.setWindowTitle(_translate("Dialog", "HPAC VIS - Add Staff"))
        
        self.addstafftitle.setText(_translate("Dialog", "Add Staff"))
        self.I1A.setText(_translate("Dialog", "First Name:"))
        self.I2A.setText(_translate("Dialog", "Last Name:"))
        self.I3A.setText(_translate("Dialog", "Position:"))
        self.I4A.setText(_translate("Dialog", "PRC LN:"))
        self.I5A.setText(_translate("Dialog", "Staff-ID:"))
        self.I6A.setText(_translate("Dialog", "Contact No.:"))
        self.I7A.setText(_translate("Dialog", "Date Hired:"))
        self.I8A.setText(_translate("Dialog", "Status:"))
        self.I3B.setCurrentText(_translate("Dialog", "Owner"))
        self.I3B.setItemText(0, _translate("Dialog", "Owner"))
        self.I3B.setItemText(1, _translate("Dialog", "Veterinarian"))
        self.I3B.setItemText(2, _translate("Dialog", "Vet Assistant"))
        self.I3B.setItemText(3, _translate("Dialog", "Secretary"))
        self.I3B.setItemText(4, _translate("Dialog", "Assistant Secretary"))
        self.I3B.setItemText(5, _translate("Dialog", "Groomer"))
        self.I4B.setText(_translate("Dialog", "N/A"))
        self.I5B.setText(_translate("Dialog", "ST -"))
        self.I8B.setItemText(0, _translate("Dialog", "Active"))
        self.I8B.setItemText(1, _translate("Dialog", "On Leave"))
        self.I8B.setItemText(2, _translate("Dialog", "Dismissed"))
        self.I8B.setItemText(3, _translate("Dialog", "Part-time"))
        self.addbutt.setText(_translate("Dialog", "Add"))
        self.cancellbutt.setText(_translate("Dialog", "Cancel"))



#TINTIN WAS HERE FOR checking if mag pop up ba or not
    def savestaff(self):        
        if self.existing_data:
                if not globalsession.skip_update_confirmation_flag:
                        dialog = UpdateCon(table_name="stafftb")
                        if dialog.exec_() == QDialog.Accepted:
                                if dialog.skip_dialog:
                                        globalsession.skip_update_confirmation_flag = True
                                self.actuallysave()
                else:
                        self.actuallysave()
        else:
                first_name = self.I1B.text().strip()
                last_name = self.I2B.text().strip()

                if not self.check_duplicate_staff(first_name, last_name):
                       return
                
                self.actuallysave()


#TINTIN WAS HERE to check if there are duplicate entries
    def check_duplicate_staff(self, first_name, last_name):
        try:
                db = DBManager()
                db.connect_DB()
                kuryente = db.kuryente

                def simplify(name):
                        parts = name.strip().lower().split()
                        return parts[0], parts[-1] if len(parts) > 1 else ""

                input_first, input_last = simplify(first_name), simplify(last_name)
                input_first = input_first[0]
                input_last = input_last[1] or input_first[0]

                query = """
                SELECT First_Name, Last_Name, Staff_ID
                FROM stafftb
                """
                kuryente.execute(query)
                results = kuryente.fetchall()

                for db_first, db_last, staff_id in results:
                        db_first_simple = simplify(db_first)[0]
                        db_last_simple = simplify(db_last)[-1]

                        if input_first in db_first_simple or db_first_simple in input_first:
                                if input_last in db_last_simple or db_last_simple in input_last:
                                        full_name = f"{db_first.strip().title()} {db_last.strip().title()}"
                                        dialog = DupCon(full_name, staff_id, table_name="stafftb")
                                        return dialog.exec_() == QDialog.Accepted

                return True

        except Exception as e:
                print("Duplicate check error (staff - fuzzy):", e)
                return True
        


#TINTIN WAS HERE to create the function for saving and cancelling
    def actuallysave(self):

        first_name = self.I1B.text().strip()
        last_name = self.I2B.text().strip()
        position = self.I3B.currentText().strip()
        prc_ln = self.I4B.text().strip()
        staff_id = f"ST-{self.I5C.text().strip()}"
        contact_number = self.I6B.text().strip()
        date_hired = self.I7B.date().toString("yyyy-MM-dd")
        status = self.I8B.currentText().strip()

        if not self.validate_inputs():
                return

        try:
                db = DBManager()
                db.connect_DB()
                kuryente = db.kuryente
                cable = db.cable

                if self.existing_data:

                        query = """
                        UPDATE stafftb SET
                                first_name=%s,
                                last_name=%s,
                                Position=%s,
                                PRC_LN=%s,
                                Contact_Number=%s,
                                Date_Hired=%s,
                                Status=%s
                        WHERE Staff_ID=%s
                        """
                        values = (first_name, last_name, position, prc_ln, contact_number, date_hired, status, staff_id)
                
                else:
                        query = """
                        INSERT INTO stafftb (first_name, last_name, Position, PRC_LN, Staff_ID, `Contact_Number`, `Date_Hired`, Status)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        """
                        values = (first_name, last_name, position, prc_ln, staff_id, contact_number, date_hired, status)
                
                kuryente.execute(query, values)
                cable.commit()
                self.accept()
                
        except Exception as e:
                print("Something went wrong:", e)

    def cancel(self):
        self.close()



#TINTIN WAS HERE to validate inputs
    def validate_inputs(self):
        first_name = self.I1B.text().strip()
        last_name = self.I2B.text().strip()
        prc_ln = self.I4B.text().strip()
        staff_id = self.I5C.text().strip()
        contact_number = self.I6B.text().strip()
        position = self.I3B.currentText().strip()

        # Check required fields
        if not first_name or not last_name or not staff_id or not contact_number:
                self.choosetb("Please complete all required fields.")
                return False

        # Check that staff code is digits
        if not staff_id.isdigit():
                self.choosetb("Staff ID must be numeric.")
                return False

        # Check that contact number is digits and 11 characters
        if not contact_number.isdigit() or len(contact_number) != 11:
                self.choosetb("Contact Number must be 11 digits.")
                return False

        # If veterinarian, PRC LRN must be filled
        if position == "Veterinarian" and not prc_ln:
                self.choosetb("PRC LRN is required for Veterinary staff.")
                return False

        return True



#TINTIN WAS HERE to create warning if there's an empty answer
    def choosetb(self, message):
        msg = QtWidgets.QMessageBox(self)
        msg.setWindowTitle("Missing Information")
        msg.setText(message)
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
        


#TINTIN WAS HERE - edit the prc_line number
    def prcedit(self, text):
        if text == "Veterinarian":
                self.I4B.setReadOnly(False)
                if self.I4B.text() == "N/A":
                        self.I4B.clear()
                self.I4B.setStyleSheet("""
                QLineEdit {
                        font-family: "Merriweather Sans";
                        font: bold;
                        font-size: 20px;
                        color: #072A42;
                        background-color: #fafafa;
                        border: 2px solid #072A42;
                        border-radius: 6px;
                        padding: 5px;
                }

                QLineEdit::placeholder {
                        color: #DD5C6D;
                        font-style: italic;
                }
                """)
                self.I4B.setPlaceholderText("Enter PRC LN")
        else:
                self.I4B.setReadOnly(True)
                self.I4B.setText("N/A")
                self.I4B.setStyleSheet("""
                QLineEdit {
                        font-family: "Merriweather Sans";
                        font: bold;
                        font-size: 20px;
                        color: #D8EDF3;
                        background-color: #072A42;
                        border: 2px solid #072A42;
                        border-radius: 6px;
                        padding: 5px;
                }

                QLineEdit::placeholder {
                        color: #DD5C6D;
                        font-style: italic;
                }
                """)
                self.I4B.setPlaceholderText("")



# TINTIN WAS HERE for the function to fill the blanks with existing data
    def fillanswers(self):
        self.I1B.setText(self.existing_data[0])          
        self.I2B.setText(self.existing_data[1])   
        self.I3B.setCurrentText(self.existing_data[2])          
        self.I4B.setText(self.existing_data[3])

        full_staff_id = self.existing_data[4]
        prefix, sep, number_part = full_staff_id.partition("-")
        self.I5C.setText(number_part)

        self.I6B.setText(self.existing_data[5])
        self.I7B.setDate(QDate.fromString(self.existing_data[6], "yyyy-MM-dd"))   
        self.I8B.setCurrentText(self.existing_data[7])



#TINTIN WAS HERE to customize warning qmessagebox
    def choosetb(self, message):
                dialog = QtWidgets.QDialog()
                uic.loadUi("Warning/warningchoosetb.ui", dialog)

                dialog.setWindowIcon(QIcon("Pictures/Staff.png"))
                dialog.setWindowTitle("Uh-oh!")
                dialog.text.setText(message)
                dialog.okbutt.clicked.connect(dialog.accept) 

                QApplication.beep()

                dialog.exec_()
