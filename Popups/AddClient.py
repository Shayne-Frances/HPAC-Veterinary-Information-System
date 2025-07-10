from PyQt5 import QtCore, QtGui, QtWidgets
from Pictures import Hpac_rc
from Database_Manager.database import DBManager
from PyQt5.QtGui import QIntValidator, QIcon
from PyQt5.QtGui import QRegularExpressionValidator
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



class AddClientControl(QtWidgets.QDialog):
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
        self.clientlogo = QtWidgets.QLabel(self.titlelogoframe)
        self.clientlogo.setEnabled(True)
        self.clientlogo.setMaximumSize(QtCore.QSize(90, 90))
        self.clientlogo.setText("")
        self.clientlogo.setPixmap(QtGui.QPixmap(":/icons/Client.png"))
        self.clientlogo.setScaledContents(True)
        self.clientlogo.setObjectName("clientlogo")
        self.horizontalLayout.addWidget(self.clientlogo)
        self.addclienttitle = QtWidgets.QLabel(self.titlelogoframe)
        self.addclienttitle.setStyleSheet("QLabel {\n"
"    font: Merriweather Sans;\n"
"    font: bold;\n"
"    font-size: 25px;\n"
"    color: #072A42;\n"
"}")
        self.addclienttitle.setObjectName("addclienttitle")
        self.horizontalLayout.addWidget(self.addclienttitle)
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
        self.I1AFrame.setMaximumSize(QtCore.QSize(16777215, 55))
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
        self.I2AFrame.setMaximumSize(QtCore.QSize(16777215, 55))
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
        self.I3AFrame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.I3AFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I3AFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I3AFrame.setObjectName("I3AFrame")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.I3AFrame)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.I3A = QtWidgets.QLabel(self.I3AFrame)
        self.I3A.setStyleSheet("QLabel {\n"
"    font: Merriweather Sans;\n"
"    font: bold;\n"
"    font-size: 20px;\n"
"    color: #072A42;\n"
"}")
        self.I3A.setObjectName("I3A")
        self.horizontalLayout_14.addWidget(self.I3A)
        self.verticalLayout.addWidget(self.I3AFrame)
        self.I4AFrame = QtWidgets.QFrame(self.IAFrame)
        self.I4AFrame.setMinimumSize(QtCore.QSize(0, 50))
        self.I4AFrame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.I4AFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I4AFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I4AFrame.setObjectName("I4AFrame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.I4AFrame)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.I4A = QtWidgets.QLabel(self.I4AFrame)
        self.I4A.setStyleSheet("QLabel {\n"
"    font: Merriweather Sans;\n"
"    font: bold;\n"
"    font-size: 20px;\n"
"    color: #072A42;\n"
"}")
        self.I4A.setObjectName("I4A")
        self.horizontalLayout_6.addWidget(self.I4A)
        self.verticalLayout.addWidget(self.I4AFrame)
        self.I5AFrame = QtWidgets.QFrame(self.IAFrame)
        self.I5AFrame.setMinimumSize(QtCore.QSize(0, 55))
        self.I5AFrame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.I5AFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I5AFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I5AFrame.setObjectName("I5AFrame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.I5AFrame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.I5A = QtWidgets.QLabel(self.I5AFrame)
        self.I5A.setStyleSheet("QLabel {\n"
"    font: Merriweather Sans;\n"
"    font: bold;\n"
"    font-size: 20px;\n"
"    color: #072A42;\n"
"}")
        self.I5A.setObjectName("I5A")
        self.horizontalLayout_7.addWidget(self.I5A)
        self.verticalLayout.addWidget(self.I5AFrame)
        self.I6AFrame = QtWidgets.QFrame(self.IAFrame)
        self.I6AFrame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.I6AFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I6AFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I6AFrame.setObjectName("I6AFrame")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.I6AFrame)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.I6A = QtWidgets.QLabel(self.I6AFrame)
        self.I6A.setStyleSheet("QLabel {\n"
"    font: Merriweather Sans;\n"
"    font: bold;\n"
"    font-size: 20px;\n"
"    color: #072A42;\n"
"}")
        self.I6A.setObjectName("I6A")
        self.horizontalLayout_19.addWidget(self.I6A)
        self.verticalLayout.addWidget(self.I6AFrame)
        self.I7AFrame = QtWidgets.QFrame(self.IAFrame)
        self.I7AFrame.setMinimumSize(QtCore.QSize(0, 55))
        self.I7AFrame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.I7AFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I7AFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I7AFrame.setObjectName("I7AFrame")
        self.verticalLayout.addWidget(self.I7AFrame)
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
        self.I1B.setMaximumSize(QtCore.QSize(16777215, 40))
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
        self.I2B.setMaximumSize(QtCore.QSize(16777215, 40))
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
        self.I3BCFrame = QtWidgets.QFrame(self.IBFrame)
        self.I3BCFrame.setMinimumSize(QtCore.QSize(0, 55))
        self.I3BCFrame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.I3BCFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I3BCFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I3BCFrame.setObjectName("I3BCFrame")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.I3BCFrame)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.I3C = QtWidgets.QLineEdit(self.I3BCFrame)
        self.I3C.setMinimumSize(QtCore.QSize(0, 40))
        self.I3C.setMaximumSize(QtCore.QSize(16777215, 40))
        self.I3C.setStyleSheet("QLineEdit {\n"
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
        self.I3C.setReadOnly(True)
        self.I3C.setObjectName("I3C")
        self.horizontalLayout_16.addWidget(self.I3C)
        self.I3B = QtWidgets.QLabel(self.I3BCFrame)
        self.I3B.setMinimumSize(QtCore.QSize(0, 40))
        self.I3B.setStyleSheet("QLabel {\n"
"    font-family: \"Merriweather Sans\";\n"
"    font: bold;\n"
"    font-size: 18px;\n"
"    color: #072A42;\n"
"\n"
"}\n"
"\n"
"")
        self.I3B.setObjectName("I3B")
        self.horizontalLayout_16.addWidget(self.I3B)
        self.verticalLayout_2.addWidget(self.I3BCFrame)
        self.I4BFrame = QtWidgets.QFrame(self.IBFrame)
        self.I4BFrame.setMinimumSize(QtCore.QSize(0, 55))
        self.I4BFrame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.I4BFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I4BFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I4BFrame.setObjectName("I4BFrame")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.I4BFrame)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.I4B = QtWidgets.QLineEdit(self.I4BFrame)
        self.I4B.setMinimumSize(QtCore.QSize(0, 40))
        self.I4B.setMaximumSize(QtCore.QSize(16777215, 40))
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
        self.I4B.setObjectName("I4B")
        self.horizontalLayout_11.addWidget(self.I4B)
        self.verticalLayout_2.addWidget(self.I4BFrame)
        self.I5BFrame = QtWidgets.QFrame(self.IBFrame)
        self.I5BFrame.setMinimumSize(QtCore.QSize(0, 55))
        self.I5BFrame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.I5BFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I5BFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I5BFrame.setObjectName("I5BFrame")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.I5BFrame)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.I5B = QtWidgets.QLineEdit(self.I5BFrame)
        self.I5B.setMinimumSize(QtCore.QSize(0, 40))
        self.I5B.setMaximumSize(QtCore.QSize(16777215, 40))
        self.I5B.setStyleSheet("QLineEdit {\n"
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
        self.I5B.setObjectName("I5B")
        self.horizontalLayout_12.addWidget(self.I5B)
        self.verticalLayout_2.addWidget(self.I5BFrame)
        self.I6BFrame = QtWidgets.QFrame(self.IBFrame)
        self.I6BFrame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.I6BFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I6BFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I6BFrame.setObjectName("I6BFrame")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.I6BFrame)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.I6B = QtWidgets.QComboBox(self.I6BFrame)
        self.I6B.setMinimumSize(QtCore.QSize(0, 40))
        self.I6B.setMaximumSize(QtCore.QSize(16777215, 40))
        self.I6B.setStyleSheet("QComboBox {\n"
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
        self.I6B.setObjectName("I6B")
        self.I6B.addItem("")
        self.I6B.addItem("")
        self.horizontalLayout_20.addWidget(self.I6B)
        self.verticalLayout_2.addWidget(self.I6BFrame)
        self.I7BCFrame = QtWidgets.QFrame(self.IBFrame)
        self.I7BCFrame.setEnabled(True)
        self.I7BCFrame.setMinimumSize(QtCore.QSize(0, 55))
        self.I7BCFrame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.I7BCFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I7BCFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I7BCFrame.setObjectName("I7BCFrame")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.I7BCFrame)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.I7C = QtWidgets.QLineEdit(self.I7BCFrame)
        self.I7C.setEnabled(True)
        self.I7C.setMinimumSize(QtCore.QSize(0, 40))
        self.I7C.setMaximumSize(QtCore.QSize(16777215, 40))
        self.I7C.setStyleSheet("QLineEdit {\n"
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
        self.I7C.setObjectName("I7C")
        self.horizontalLayout_5.addWidget(self.I7C)
        self.I7B = QtWidgets.QLabel(self.I7BCFrame)
        self.I7B.setStyleSheet("QLabel {\n"
"    font-family: \"Merriweather Sans\";\n"
"    font: bold;\n"
"    font-size: 18px;\n"
"    color: #072A42;\n"
"}\n"
"\n"
"")
        self.I7B.setObjectName("I7B")
        self.horizontalLayout_5.addWidget(self.I7B)
        self.verticalLayout_2.addWidget(self.I7BCFrame)
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
        self.setWindowIcon(QIcon("Pictures/Client.png"))



# TINTIN WAS HERE - this is for the pending line to be editable (connecting)
        self.I6B.currentTextChanged.connect(self.pendingedit)



# TINTIN WAS HERE - AUTO GENERATE CLIENT ID
        try:
                db = DBManager()
                db.connect_DB()
                kuryente = db.kuryente
                cable = db.cable

                kuryente.execute("SELECT MAX(Client_ID) FROM clientb")
                result = kuryente.fetchone()[0]

                if result is None:
                        next_id_number = 1
                else:
                        next_id_number = int(result.split('-')[1]) + 1

                formatted_id = f"{next_id_number:04d}"

                self.I3C.setText(formatted_id)
                self.I3C.setReadOnly(True)

                kuryente.close()
                cable.close()

        except Exception as e:
                print("Error generating Client ID:", e)
                self.I3C.setText("CL-0001")



# TINTIN WAS HERE to hide the pending line at the start
        self.I7B.hide() 
        self.I7C.hide()  

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)



# TINTIN WAS HERE to connect the add and cancel button
        self.addbutt.clicked.connect(self.saveclient)
        self.cancellbutt.clicked.connect(self.cancel)



#TINTIN was here to initialize the edit part, also change some labels and other stuff in the dialog
        self.existing_data = existing_data
        if self.existing_data:
                self.fillanswers()
                self.addbutt.setText("Update")
                self.addclienttitle.setText("Edit Client")
                self.setWindowTitle("HPAC VIS - Edit Client")



#TINTIN WAS HERE to limit the characters each answer sa pop-up

        self.I1B.setMaxLength(50)  
        self.I2B.setMaxLength(50) 
        self.I4B.setMaxLength(11)   
        self.I5B.setMaxLength(100)
        self.I7C.setMaxLength(10)
        self.I4B.setValidator(QRegularExpressionValidator(QRegularExpression(r"\d{0,11}")))
        self.I7C.setValidator(QIntValidator())







    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate






# TINTIN WAS HERE to manually change the window name
        Dialog.setWindowTitle(_translate("Dialog", "HPAC VIS - Add Client"))

        self.addclienttitle.setText(_translate("Dialog", "Add Client"))
        self.I1A.setText(_translate("Dialog", "First Name:"))
        self.I2A.setText(_translate("Dialog", "Last Name:"))
        self.I3A.setText(_translate("Dialog", "Client-ID:"))
        self.I4A.setText(_translate("Dialog", "Contact No.:"))
        self.I5A.setText(_translate("Dialog", "Address:"))
        self.I6A.setText(_translate("Dialog", "Status:"))
        self.I3B.setText(_translate("Dialog", "CL -"))
        self.I6B.setItemText(0, _translate("Dialog", "No Balance"))
        self.I6B.setItemText(1, _translate("Dialog", "Pending"))
        self.I7B.setText(_translate("Dialog", "Amount:"))
        self.addbutt.setText(_translate("Dialog", "Add"))
        self.cancellbutt.setText(_translate("Dialog", "Cancel"))



#TINTIN WAS HERE FOR checking if mag pop up ba or not
    def saveclient(self):
        if self.existing_data:        
                if not globalsession.skip_update_confirmation_flag:
                        dialog = UpdateCon(table_name="clientb")
                        if dialog.exec_() == QDialog.Accepted:
                                if dialog.skip_dialog:
                                        globalsession.skip_update_confirmation_flag = True
                                self.actuallysave()
                else:
                       self.actuallysave()
        else:
                first_name = self.I1B.text().strip()
                last_name = self.I2B.text().strip()

                if not self.check_duplicate_client(first_name, last_name):
                       return
                
                self.actuallysave()



#TINTIN WAS HERE to check if there are duplicate entries
    def check_duplicate_client(self, first_name, last_name):
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
                SELECT First_Name, Last_Name, Client_ID
                FROM clientb
                """
                kuryente.execute(query)
                results = kuryente.fetchall()

                for db_first, db_last, client_id in results:
                        db_first_simple = simplify(db_first)[0]
                        db_last_simple = simplify(db_last)[-1]

                        if input_first in db_first_simple or db_first_simple in input_first:
                                if input_last in db_last_simple or db_last_simple in input_last:
                                        full_name = f"{db_first.strip().title()} {db_last.strip().title()}"
                                        dialog = DupCon(full_name, client_id, table_name="clientb")
                                        return dialog.exec_() == QDialog.Accepted

                return True

        except Exception as e:
                print("Duplicate check error (client - fuzzy):", e)
                return True
        


#TINTIN WAS HERE to create the function for saving and cancelling
    def actuallysave(self):

        first_name = self.I1B.text().strip()
        last_name = self.I2B.text().strip()
        Client_ID = f"CL-{self.I3C.text().strip()}"
        contact_number = self.I4B.text().strip()
        address = self.I5B.text().strip()
        status_selection = self.I6B.currentText().strip()
        pending_amount = self.I7C.text().strip()

        if not self.validate_inputs():
               return

        if status_selection == "Pending":
                status = f"Pending: {pending_amount}"
        else:
                status = status_selection

        try:
                db = DBManager()
                db.connect_DB()
                kuryente = db.kuryente
                cable = db.cable

                if self.existing_data:
                       
                       query = """
                       UPDATE clientb SET
                                first_name=%s,
                                last_name=%s,
                                Client_ID=%s,
                                Contact_Number=%s,
                                Address=%s,
                                Status=%s
                        WHERE Client_ID=%s
                        """
                       values = (first_name, last_name, Client_ID, contact_number, address, status, Client_ID)
                else:
                        query = """
                        INSERT INTO clientb (first_name, last_name, Client_ID, `Contact_number`, address, status)
                        VALUES (%s, %s, %s, %s, %s, %s)
                        """

                        values = (first_name, last_name, Client_ID, contact_number, address, status)

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
        contact_number = self.I4B.text().strip()
        address = self.I5B.text().strip()
        status = self.I6B.currentText().strip()
        pending_amount = self.I7C.text().strip()


        if not first_name or not last_name or not contact_number or not address:
                self.choosetb("Please complete all required fields.")
                return False

        if not contact_number.isdigit() or len(contact_number) != 11:
                self.choosetb("Contact Number must be exactly 11 digits.")
                return False

        if status == "Pending":
                if not pending_amount:
                        self.choosetb("Please enter the pending amount.")
                        return False
                if not pending_amount.replace('.', '', 1).isdigit():
                        self.choosetb("Pending amount must be a number.")
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

#TINTIN WAS HERE - edit the pending number

    def pendingedit(self, text):
        if text == "Pending":
                self.I7B.show()
                self.I7C.show()
                self.I7C.setStyleSheet("""
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

        else:
                self.I7B.hide()
                self.I7C.hide()
                self.I7C.clear()
                self.I7C.setStyleSheet("""
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
        


# TINTIN WAS HERE for the function to fill the blanks with existing data
    def fillanswers(self):
        self.I1B.setText(self.existing_data[0])          
        self.I2B.setText(self.existing_data[1]) 

        full_client_id = self.existing_data[2]
        prefix, sep, number_part = full_client_id.partition("-")
        self.I3C.setText(number_part)

        self.I4B.setText(self.existing_data[3])          
        self.I5B.setText(self.existing_data[4])
        self.I6B.setCurrentText(self.existing_data[5])

        status_field = self.existing_data[5] 
        status_part, _, amount_part = status_field.partition(":")
        if status_part.strip() == "Pending":
                self.I6B.setCurrentText("Pending")       
                self.I7C.setText(amount_part.strip())      
                self.I7B.show()
                self.I7C.show()
        else:
                self.I6B.setCurrentText(status_field)
                self.I7C.clear()
                self.I7B.hide()
                self.I7C.hide()


#TINTIN WAS HERE to customize warning qmessagebox
    def choosetb(self, message):
                dialog = QtWidgets.QDialog()
                uic.loadUi("Warning/warningchoosetb.ui", dialog)

                dialog.setWindowIcon(QIcon("Pictures/Client.png"))
                dialog.setWindowTitle("Oops!")
                dialog.text.setText(message)
                dialog.okbutt.clicked.connect(dialog.accept) 

                QApplication.beep()

                dialog.exec_()