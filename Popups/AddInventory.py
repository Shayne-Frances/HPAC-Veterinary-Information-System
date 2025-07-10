from PyQt5 import QtCore, QtGui, QtWidgets
from Pictures import Hpac_rc
from Database_Manager.database import DBManager
from PyQt5.QtGui import QIntValidator, QIcon

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



class AddInventoryControl(QtWidgets.QDialog):
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
        spacerItem = QtWidgets.QSpacerItem(25, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.titlelogoframe = QtWidgets.QFrame(self.alltopframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titlelogoframe.sizePolicy().hasHeightForWidth())
        self.titlelogoframe.setSizePolicy(sizePolicy)
        self.titlelogoframe.setMinimumSize(QtCore.QSize(277, 100))
        self.titlelogoframe.setMaximumSize(QtCore.QSize(277, 80))
        self.titlelogoframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.titlelogoframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.titlelogoframe.setObjectName("titlelogoframe")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.titlelogoframe)
        self.horizontalLayout.setContentsMargins(0, 0, 0, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.inventorylogo = QtWidgets.QLabel(self.titlelogoframe)
        self.inventorylogo.setMaximumSize(QtCore.QSize(90, 90))
        self.inventorylogo.setText("")
        self.inventorylogo.setPixmap(QtGui.QPixmap(":/icons/Inventory.png"))
        self.inventorylogo.setScaledContents(True)
        self.inventorylogo.setObjectName("inventorylogo")
        self.horizontalLayout.addWidget(self.inventorylogo)
        self.addinventorytitle = QtWidgets.QLabel(self.titlelogoframe)
        self.addinventorytitle.setStyleSheet("QLabel {\n"
"    font: Merriweather Sans;\n"
"    font: bold;\n"
"    font-size: 25px;\n"
"    color: #072A42;\n"
"}")
        self.addinventorytitle.setObjectName("addinventorytitle")
        self.horizontalLayout.addWidget(self.addinventorytitle)
        self.horizontalLayout_2.addWidget(self.titlelogoframe)
        spacerItem1 = QtWidgets.QSpacerItem(75, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addWidget(self.alltopframe)
        self.allmiddleframe = QtWidgets.QFrame(self)
        self.allmiddleframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.allmiddleframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.allmiddleframe.setObjectName("allmiddleframe")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.allmiddleframe)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.IAFrame = QtWidgets.QFrame(self.allmiddleframe)
        self.IAFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.IAFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.IAFrame.setObjectName("IAFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.IAFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.I1AFrame = QtWidgets.QFrame(self.IAFrame)
        self.I1AFrame.setMinimumSize(QtCore.QSize(145, 55))
        self.I1AFrame.setMaximumSize(QtCore.QSize(145, 55))
        self.I1AFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I1AFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I1AFrame.setObjectName("I1AFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.I1AFrame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.I1A = QtWidgets.QLabel(self.I1AFrame)
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
        self.I2AFrame.setMinimumSize(QtCore.QSize(145, 55))
        self.I2AFrame.setMaximumSize(QtCore.QSize(145, 55))
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
        self.I6AFrame.setMinimumSize(QtCore.QSize(0, 55))
        self.I6AFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I6AFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I6AFrame.setObjectName("I6AFrame")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.I6AFrame)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.I6A = QtWidgets.QLabel(self.I6AFrame)
        self.I6A.setStyleSheet("QLabel {\n"
"    font: Merriweather Sans;\n"
"    font: bold;\n"
"    font-size: 20px;\n"
"    color: #072A42;\n"
"}")
        self.I6A.setObjectName("I6A")
        self.horizontalLayout_7.addWidget(self.I6A)
        self.verticalLayout.addWidget(self.I6AFrame)
        self.I7AFrame = QtWidgets.QFrame(self.IAFrame)
        self.I7AFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I7AFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I7AFrame.setObjectName("I7AFrame")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.I7AFrame)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.I7A = QtWidgets.QLabel(self.I7AFrame)
        self.I7A.setStyleSheet("QLabel {\n"
"    font: Merriweather Sans;\n"
"    font: bold;\n"
"    font-size: 20px;\n"
"    color: #072A42;\n"
"}")
        self.I7A.setObjectName("I7A")
        self.horizontalLayout_19.addWidget(self.I7A)
        self.verticalLayout.addWidget(self.I7AFrame)
        self.horizontalLayout_17.addWidget(self.IAFrame)
        self.IBFrame = QtWidgets.QFrame(self.allmiddleframe)
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
        self.I2B_2 = QtWidgets.QComboBox(self.I2BFrame)
        self.I2B_2.setMinimumSize(QtCore.QSize(0, 40))
        self.I2B_2.setStyleSheet("QComboBox {\n"
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
        self.I2B_2.setEditable(False)
        self.I2B_2.setObjectName("I2B_2")
        self.I2B_2.addItem("")
        self.I2B_2.addItem("")
        self.I2B_2.addItem("")
        self.I2B_2.addItem("")
        self.I2B_2.addItem("")
        self.horizontalLayout_9.addWidget(self.I2B_2)
        self.verticalLayout_2.addWidget(self.I2BFrame)
        self.I3BCFrame = QtWidgets.QFrame(self.IBFrame)
        self.I3BCFrame.setMinimumSize(QtCore.QSize(0, 55))
        self.I3BCFrame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.I3BCFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I3BCFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I3BCFrame.setObjectName("I3BCFrame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.I3BCFrame)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
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
        self.horizontalLayout_10.addWidget(self.I3B)
        self.I3C = QtWidgets.QLineEdit(self.I3BCFrame)
        self.I3C.setMinimumSize(QtCore.QSize(0, 40))
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
        self.horizontalLayout_10.addWidget(self.I3C)
        self.verticalLayout_2.addWidget(self.I3BCFrame)
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
        self.I5B = QtWidgets.QComboBox(self.I5BCFrame)
        self.I5B.setMinimumSize(QtCore.QSize(0, 40))
        self.I5B.setMaximumSize(QtCore.QSize(16777215, 40))
        self.I5B.setStyleSheet("QComboBox {\n"
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
        self.I5B.setEditable(True)
        self.I5B.setObjectName("I5B")
        self.I5B.addItem("")
        self.I5B.addItem("")
        self.I5B.addItem("")
        self.I5B.addItem("")
        self.I5B.addItem("")
        self.I5B.addItem("")
        self.I5B.addItem("")
        self.I5B.addItem("")
        self.horizontalLayout_16.addWidget(self.I5B)
        self.verticalLayout_2.addWidget(self.I5BCFrame)
        self.I6BFrame = QtWidgets.QFrame(self.IBFrame)
        self.I6BFrame.setMinimumSize(QtCore.QSize(0, 55))
        self.I6BFrame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.I6BFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I6BFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I6BFrame.setObjectName("I6BFrame")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.I6BFrame)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.I6B = QtWidgets.QSpinBox(self.I6BFrame)
        self.I6B.setMinimumSize(QtCore.QSize(0, 40))
        self.I6B.setMaximumSize(QtCore.QSize(16777215, 40))
        self.I6B.setStyleSheet("QSpinBox {\n"
"    font-family: \"Merriweather Sans\";\n"
"    color: #DA99A5;\n"
"    font-size: 18px;\n"
"    font-weight: bold;\n"
"    padding: 5px;\n"
"    border: 2px solid #072A42;\n"
"    border-radius: 5px;\n"
"    background-color: #fafafa;\n"
"}\n"
"\n"
"\n"
"")
        self.I6B.setObjectName("I6B")
        self.horizontalLayout_12.addWidget(self.I6B)
        self.verticalLayout_2.addWidget(self.I6BFrame)
        self.I7BFrame = QtWidgets.QFrame(self.IBFrame)
        self.I7BFrame.setMinimumSize(QtCore.QSize(0, 55))
        self.I7BFrame.setMaximumSize(QtCore.QSize(16777215, 55))
        self.I7BFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.I7BFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.I7BFrame.setObjectName("I7BFrame")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.I7BFrame)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.I7B = QtWidgets.QLineEdit(self.I7BFrame)
        self.I7B.setMinimumSize(QtCore.QSize(0, 40))
        self.I7B.setMaximumSize(QtCore.QSize(16777215, 40))
        self.I7B.setStyleSheet("QLineEdit {\n"
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
        self.I7B.setObjectName("I7B")
        self.horizontalLayout_20.addWidget(self.I7B)
        self.verticalLayout_2.addWidget(self.I7BFrame)
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

# TINTIN WAS HERE - AUTO GENERATE INVENTORY ID
        try:
                db = DBManager()
                db.connect_DB()
                kuryente = db.kuryente
                cable = db.cable

                kuryente.execute("SELECT MAX(Inventory_ID) FROM inventorytb")
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
                print("Error generating Inventory ID:", e)
                self.I3C.setText("IV-0001") 






        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)





# TINTIN WAS HERE to change the window icon
        self.setWindowIcon(QIcon("Pictures/Inventory.png"))


#TINTIN WAS HERE to connect the buttons to their functions
        self.addbutt.clicked.connect(self.saveinventory)
        self.cancellbutt.clicked.connect(self.cancel)

        

#TINTIN was here to initial the edit part
        self.existing_data = existing_data
        if self.existing_data:
                self.fillanswers()
                self.addbutt.setText("Update")
                self.addinventorytitle.setText("Edit Inventory")
                self.setWindowTitle("HPAC VIS - Edit Inventory")



#TINTIN WAS HERE to limit the characters each answer sa pop-up
        self.I1B.setMaxLength(50)  
        self.I4B.setMaxLength(10)
        self.I5B.lineEdit().setMaxLength(10)
        self.I6B.setRange(0, 9999999)
        self.I7B.setMaxLength(10)
        self.I7B.setValidator(QIntValidator(self))






    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate








# TINTIN WAS HERE to manually change the window name
        Dialog.setWindowTitle(_translate("Dialog", "HPAC VIS - Add Inventory"))

        self.addinventorytitle.setText(_translate("Dialog", "Add Inventory"))
        self.I1A.setText(_translate("Dialog", "Name:"))
        self.I2A.setText(_translate("Dialog", "Type:"))
        self.I3A.setText(_translate("Dialog", "Inventory-ID:"))
        self.I4A.setText(_translate("Dialog", "Quantity:"))
        self.I5A.setText(_translate("Dialog", "Unit:"))
        self.I6A.setText(_translate("Dialog", "Stock:"))
        self.I7A.setText(_translate("Dialog", "Price(PHP):"))
        self.I2B_2.setCurrentText(_translate("Dialog", "Services"))
        self.I2B_2.setItemText(0, _translate("Dialog", "Services"))
        self.I2B_2.setItemText(1, _translate("Dialog", "Diagnostic"))
        self.I2B_2.setItemText(2, _translate("Dialog", "Medicine"))
        self.I2B_2.setItemText(3, _translate("Dialog", "Vitamins"))
        self.I2B_2.setItemText(4, _translate("Dialog", "Others"))
        self.I3B.setText(_translate("Dialog", "IV -"))
        self.I5B.setItemText(0, _translate("Dialog", "mL"))
        self.I5B.setItemText(1, _translate("Dialog", "L"))
        self.I5B.setItemText(2, _translate("Dialog", "tablet"))
        self.I5B.setItemText(3, _translate("Dialog", "capsule"))
        self.I5B.setItemText(4, _translate("Dialog", "vial"))
        self.I5B.setItemText(5, _translate("Dialog", "g"))
        self.I5B.setItemText(6, _translate("Dialog", "pack"))
        self.I5B.setItemText(7, _translate("Dialog", "kg"))
        self.addbutt.setText(_translate("Dialog", "Add"))
        self.cancellbutt.setText(_translate("Dialog", "Cancel"))


#TINTIN WAS HERE to create the function for saving and cancelling
    def saveinventory(self):
        if self.existing_data:
                if not globalsession.skip_update_confirmation_flag:
                        dialog = UpdateCon(table_name="inventorytb")
                        if dialog.exec_() == QDialog.Accepted:
                                if dialog.skip_dialog:
                                        globalsession.skip_update_confirmation_flag = True
                                self.actuallysave()
                else:
                        self.actuallysave()
        else:
                name = self.I1B.text().strip()

                if not self.check_duplicate_inventory(name):
                       return
                
                self.actuallysave()        



#TINTIN WAS HERE to check if there are duplicate entries
    def check_duplicate_inventory(self, name):
        try:
                db = DBManager()
                db.connect_DB()
                kuryente = db.kuryente

                input_name = name.strip().lower()
                input_name_parts = input_name.split()
                input_name_clean = f"{input_name_parts[0]} {input_name_parts[-1]}" if len(input_name_parts) > 1 else input_name

                query = "SELECT Name, Inventory_ID FROM inventorytb"
                kuryente.execute(query)
                results = kuryente.fetchall()

                for db_name, inventory_id in results:
                        db_name_parts = db_name.strip().split()
                        db_name_clean = f"{db_name_parts[0]} {db_name_parts[-1]}" if len(db_name_parts) > 1 else db_name.strip().lower()

                        if input_name_clean == db_name_clean:
                                dialog = DupCon(db_name.title(), "", inventory_id, table_name="inventorytb")
                                return dialog.exec_() == QDialog.Accepted

                return True

        except Exception as e:
                print("Duplicate check error (inventory):", e)
                return True
        


#TINTIN WAS HERE to create the function for saving and cancelling
    def actuallysave(self):

        name = self.I1B.text().strip()
        type = self.I2B_2.currentText().strip()
        inventory_id = f"IV-{self.I3C.text().strip()}"
        quantity = self.I4B.text().strip()
        unit = self.I5B.currentText().strip()
        stock = str(self.I6B.value())
        price = self.I7B.text().strip()
        

        if not self.validate_inputs():
                return


        try:
                db = DBManager()
                db.connect_DB()
                kuryente = db.kuryente
                cable = db.cable

                if self.existing_data:
                      
                        query = """
                        UPDATE inventorytb SET
                                name=%s,
                                type=%s,
                                Inventory_ID=%s,
                                quantity=%s,
                                unit=%s,
                                stock=%s,
                                `Price(PHP)`=%s
                        WHERE Inventory_ID=%s
                        """
                        values = (name, type, inventory_id, quantity, unit, stock, price, inventory_id)
                
                else:        
                        query = """
                        INSERT INTO inventorytb (name, type, Inventory_ID, `quantity`, unit, `stock`, `Price(PHP)`)
                        VALUES (%s, %s, %s, %s, %s, %s, %s)
                        """

                        values = (name, type, inventory_id, quantity, unit, stock, price)

                kuryente.execute(query, values)
                cable.commit()
                self.accept()

        except Exception as e:
                print("Something went wrong:", e)

    def cancel(self):
        self.close()



#TINTIN WAS HERE to validate inputs
    def validate_inputs(self):
        name = self.I1B.text().strip()
        type_ = self.I2B_2.currentText().strip()
        inventory_id = self.I3C.text().strip()
        quantity = self.I4B.text().strip()
        unit = self.I5B.currentText().strip()
        price = self.I7B.text().strip()

        # Check required fields
        if not name or not type_ or not inventory_id or not quantity or not unit or not price:
                self.choosetb("Please complete all required fields.")
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



# TINTIN WAS HERE for the function to fill the blanks with existing data
    def fillanswers(self):
        self.I1B.setText(self.existing_data[0])          
        self.I2B_2.setCurrentText(self.existing_data[1])

        full_inventory_id = self.existing_data[2]
        prefix, sep, number_part = full_inventory_id.partition("-")
        self.I3C.setText(number_part)

        self.I4B.setText(self.existing_data[3])          
        self.I5B.setCurrentText(self.existing_data[4])
        self.I6B.setValue(int(self.existing_data[5]))
        self.I7B.setText(self.existing_data[6])



#TINTIN WAS HERE to customize warning qmessagebox
    def choosetb(self, message):
                dialog = QtWidgets.QDialog()
                uic.loadUi("Warning/warningchoosetb.ui", dialog)

                dialog.setWindowIcon(QIcon("Pictures/Inventory.png"))
                dialog.setWindowTitle("Hmm...")
                dialog.text.setText(message)
                dialog.okbutt.clicked.connect(dialog.accept) 

                QApplication.beep()

                dialog.exec_()