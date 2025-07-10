from Pictures import Hpac_rc 
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QStandardItem, QStandardItemModel
from Database_Manager.database import DBManager 
from PyQt5.QtCore import Qt, QStringListModel
from PyQt5.QtGui import QBrush, QPalette, QPixmap
from PyQt5.QtCore import QSize
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QCompleter
from PyQt5.QtWidgets import QListView
from PyQt5.QtCore import QEvent, Qt, QTimer, QPoint
from PyQt5.QtWidgets import QLabel


#TINTIN WAS HERE to import the popups
from Popups.AddStaff import AddStaffControl
from Popups.AddClient import AddClientControl
from Popups.AddPatient import AddPatientControl
from Popups.AddInventory import AddInventoryControl
from Popups.AddSupplier import AddSupplierControl

#TINTIN WAS HERE to import the warnings
from Warning.delcon import DeleteCon

#TINTIN WAS HERE to import the globals
import globalsession
import pymysql


#TINTIN WAS HERE to import what's needed for the image scaling
from PyQt5.QtWidgets import QTableView
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import Qt



#TINTIN WAS HERE to make a class for the image scaling
class ScalableBackgroundTable(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.bg_image = QPixmap("Pictures/welcomehd.png")  # default image
        self.show_bg = True  # toggle flag

    def setBackgroundImage(self, image_path):
        if image_path:
            self.bg_image = QPixmap(image_path)
            self.show_bg = True
        else:
            self.show_bg = False
        self.viewport().update()  # refresh the view

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.viewport().update()

    def paintEvent(self, event):
        painter = QPainter(self.viewport())

        # Only draw if background is enabled
        if self.show_bg and not self.bg_image.isNull():
            scaled_img = self.bg_image.scaled(
                self.viewport().size(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
            x = (self.viewport().width() - scaled_img.width()) // 2
            y = (self.viewport().height() - scaled_img.height()) // 2
            painter.drawPixmap(x, y, scaled_img)

        super().paintEvent(event)



#TINTIN WAS HERE to actually make a whole class for the completer
class SmartCompleter(QCompleter):
    def __init__(self, strings, parent=None):
        super().__init__(strings, parent)
        self.setCaseSensitivity(Qt.CaseInsensitive)
        self.setCompletionMode(QCompleter.PopupCompletion)
        self.setMaxVisibleItems(10)
        self.model = QStringListModel(strings)
        self.setModel(self.model)
        self.all_strings = strings

    def update_model(self, input_text):
        filtered = []
        for s in self.all_strings:
            name_part = s.split(":")[0].strip()
            if input_text.lower() in name_part.lower():
                filtered.append(s)
        self.model.setStringList(filtered)

    def setWidget(self, widget):
        super().setWidget(widget)
        widget.textEdited.connect(self.update_model)




class HPAC_ui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1038, 1008)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: #D8EDF3; ")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.alltopframe = QtWidgets.QFrame(self.centralwidget)
        self.alltopframe.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.alltopframe.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.alltopframe.setObjectName("alltopframe")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.alltopframe)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.logoframe = QtWidgets.QFrame(self.alltopframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logoframe.sizePolicy().hasHeightForWidth())
        self.logoframe.setSizePolicy(sizePolicy)
        self.logoframe.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logoframe.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.logoframe.setObjectName("logoframe")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.logoframe)
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.Logoframe = QtWidgets.QFrame(self.logoframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Logoframe.sizePolicy().hasHeightForWidth())
        self.Logoframe.setSizePolicy(sizePolicy)
        self.Logoframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Logoframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Logoframe.setObjectName("Logoframe")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.Logoframe)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.LOGO = QtWidgets.QLabel(self.Logoframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LOGO.sizePolicy().hasHeightForWidth())
        self.LOGO.setSizePolicy(sizePolicy)
        self.LOGO.setText("")
        self.LOGO.setPixmap(QtGui.QPixmap(":/icons/logo.png"))
        self.LOGO.setObjectName("LOGO")
        self.horizontalLayout_4.addWidget(self.LOGO)
        self.HPAClogo = QtWidgets.QLabel(self.Logoframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HPAClogo.sizePolicy().hasHeightForWidth())
        self.HPAClogo.setSizePolicy(sizePolicy)
        self.HPAClogo.setText("")
        self.HPAClogo.setPixmap(QtGui.QPixmap("HPAC IS/logo-removebg-preview.png"))
        self.HPAClogo.setScaledContents(True)
        self.HPAClogo.setObjectName("HPAClogo")
        self.horizontalLayout_4.addWidget(self.HPAClogo)
        self.horizontalLayout_5.addWidget(self.Logoframe)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout_5.addWidget(self.logoframe)
        self.allTSframe = QtWidgets.QFrame(self.alltopframe)
        self.allTSframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.allTSframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.allTSframe.setObjectName("allTSframe")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.allTSframe)
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem3)
        self.title_subframe = QtWidgets.QFrame(self.allTSframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title_subframe.sizePolicy().hasHeightForWidth())
        self.title_subframe.setSizePolicy(sizePolicy)
        self.title_subframe.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.title_subframe.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.title_subframe.setObjectName("title_subframe")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.title_subframe)
        self.verticalLayout_3.setContentsMargins(33, 0, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Titleframe = QtWidgets.QFrame(self.title_subframe)
        self.Titleframe.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Titleframe.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Titleframe.setObjectName("Titleframe")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Titleframe)
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Title1 = QtWidgets.QLabel(self.Titleframe)
        self.Title1.setStyleSheet("font: Merriweather Sans;\n"
"font: bold;\n"
"font-size: 45px;\n"
"color: #072A42;\n"
"\n"
"\n"
"")
        self.Title1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Title1.setWordWrap(False)
        self.Title1.setObjectName("Title1")
        self.horizontalLayout_2.addWidget(self.Title1)
        self.Title2 = QtWidgets.QLabel(self.Titleframe)
        self.Title2.setStyleSheet("font: Merriweather Sans;\n"
"font: bold;\n"
"font-size: 45px;\n"
"color: #DD5C6D;\n"
"\n"
"\n"
"")
        self.Title2.setObjectName("Title2")
        self.horizontalLayout_2.addWidget(self.Title2)
        self.verticalLayout_3.addWidget(self.Titleframe)
        self.subframe = QtWidgets.QFrame(self.title_subframe)
        self.subframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.subframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.subframe.setObjectName("subframe")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.subframe)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(182, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.Subtitle = QtWidgets.QLabel(self.subframe)
        self.Subtitle.setStyleSheet("font: Merriweather Sans;\n"
"font-style: italic;\n"
"font-weight: bold;\n"
"font-size: 25px;\n"
"color: #072A42;\n"
"\n"
"\n"
"")
        self.Subtitle.setObjectName("Subtitle")
        self.horizontalLayout.addWidget(self.Subtitle)
        spacerItem5 = QtWidgets.QSpacerItem(182, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.verticalLayout_3.addWidget(self.subframe)
        self.horizontalLayout_8.addWidget(self.title_subframe)
        spacerItem6 = QtWidgets.QSpacerItem(75, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.verticalLayout_5.addWidget(self.allTSframe)
        self.verticalLayout_2.addWidget(self.alltopframe)
        self.tablesframe = QtWidgets.QFrame(self.centralwidget)
        self.tablesframe.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tablesframe.sizePolicy().hasHeightForWidth())
        self.tablesframe.setSizePolicy(sizePolicy)
        self.tablesframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tablesframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tablesframe.setObjectName("tablesframe")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tablesframe)
        self.horizontalLayout_3.setContentsMargins(9, 0, -1, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Staffbutt = QtWidgets.QPushButton(self.tablesframe)
        self.Staffbutt.setStyleSheet("QPushButton {\n"
"    font: Merriweather Sans;\n"
"    font: bold;\n"
"    font-size: 25px;\n"
"    color: #072A42;\n"
"    background-color: #fafafa;\n"
"    border: 2px solid #072A42;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"            }\n"
"\n"
"QPushButton:hover {\n"
"            background-color: #c1c8d4;  \n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: #DD5C6D;\n"
"        }\n"
"")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/Staff.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Staffbutt.setIcon(icon)
        self.Staffbutt.setIconSize(QtCore.QSize(50, 50))
        self.Staffbutt.setObjectName("Staffbutt")
        self.horizontalLayout_3.addWidget(self.Staffbutt)
        self.Clientbutt = QtWidgets.QPushButton(self.tablesframe)
        self.Clientbutt.setStyleSheet("QPushButton {\n"
"    font: Merriweather Sans;\n"
"    font: bold;\n"
"    font-size: 25px;\n"
"    color: #072A42;\n"
"    background-color: #fafafa;\n"
"    border: 2px solid #072A42;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"            }\n"
"\n"
"QPushButton:hover {\n"
"            background-color: #c1c8d4;  \n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: #DD5C6D;\n"
"        }\n"
"")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/Client.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Clientbutt.setIcon(icon1)
        self.Clientbutt.setIconSize(QtCore.QSize(50, 50))
        self.Clientbutt.setObjectName("Clientbutt")
        self.horizontalLayout_3.addWidget(self.Clientbutt)
        self.Patientbutt = QtWidgets.QPushButton(self.tablesframe)
        self.Patientbutt.setStyleSheet("QPushButton {\n"
"    font: Merriweather Sans;\n"
"    font: bold;\n"
"    font-size: 25px;\n"
"    color: #072A42;\n"
"    background-color: #fafafa;\n"
"    border: 2px solid #072A42;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"            }\n"
"\n"
"QPushButton:hover {\n"
"            background-color: #c1c8d4;  \n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: #DD5C6D;\n"
"        }\n"
"")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/Patient.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Patientbutt.setIcon(icon2)
        self.Patientbutt.setIconSize(QtCore.QSize(50, 50))
        self.Patientbutt.setObjectName("Patientbutt")
        self.horizontalLayout_3.addWidget(self.Patientbutt)
        self.Inventorybutt = QtWidgets.QPushButton(self.tablesframe)
        self.Inventorybutt.setStyleSheet("QPushButton {\n"
"    font: Merriweather Sans;\n"
"    font: bold;\n"
"    font-size: 25px;\n"
"    color: #072A42;\n"
"    background-color: #fafafa;\n"
"    border: 2px solid #072A42;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"            }\n"
"\n"
"QPushButton:hover {\n"
"            background-color: #c1c8d4;  \n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: #DD5C6D;\n"
"        }\n"
"")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/Inventory.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Inventorybutt.setIcon(icon3)
        self.Inventorybutt.setIconSize(QtCore.QSize(50, 50))
        self.Inventorybutt.setObjectName("Inventorybutt")
        self.horizontalLayout_3.addWidget(self.Inventorybutt)
        self.Supplierbutt = QtWidgets.QPushButton(self.tablesframe)
        self.Supplierbutt.setStyleSheet("QPushButton {\n"
"    font: Merriweather Sans;\n"
"    font: bold;\n"
"    font-size: 25px;\n"
"    color: #072A42;\n"
"    background-color: #fafafa;\n"
"    border: 2px solid #072A42;\n"
"    border-radius: 6px;\n"
"    padding: 5px;\n"
"            }\n"
"\n"
"QPushButton:hover {\n"
"            background-color: #c1c8d4;  \n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: #DD5C6D;\n"
"        }\n"
"")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/Supplier.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Supplierbutt.setIcon(icon4)
        self.Supplierbutt.setIconSize(QtCore.QSize(50, 50))
        self.Supplierbutt.setObjectName("Supplierbutt")
        self.horizontalLayout_3.addWidget(self.Supplierbutt)
        self.verticalLayout_2.addWidget(self.tablesframe)
        self.allbotframe = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.allbotframe.sizePolicy().hasHeightForWidth())
        self.allbotframe.setSizePolicy(sizePolicy)
        self.allbotframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.allbotframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.allbotframe.setObjectName("allbotframe")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.allbotframe)
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.interactivesframe = QtWidgets.QFrame(self.allbotframe)
        self.interactivesframe.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.interactivesframe.sizePolicy().hasHeightForWidth())
        self.interactivesframe.setSizePolicy(sizePolicy)
        self.interactivesframe.setMinimumSize(QtCore.QSize(1000, 0))
        self.interactivesframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.interactivesframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.interactivesframe.setObjectName("interactivesframe")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.interactivesframe)
        self.horizontalLayout_9.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.searchbar = QtWidgets.QLineEdit(self.interactivesframe)
        self.searchbar.setMinimumSize(QtCore.QSize(150, 40))
        self.searchbar.setMaximumSize(QtCore.QSize(250, 20))
        self.searchbar.setStyleSheet("QLineEdit {\n"
"    font-family: \"Merriweather Sans\";\n"
"    font: bold;\n"
"    font-size: 15px;\n"
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
        self.searchbar.setObjectName("searchbar")
        self.horizontalLayout_9.addWidget(self.searchbar)
        self.sortframe = QtWidgets.QFrame(self.interactivesframe)
        self.sortframe.setMinimumSize(QtCore.QSize(150, 0))
        self.sortframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sortframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sortframe.setObjectName("sortframe")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.sortframe)
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.sortbutt = QtWidgets.QComboBox(self.sortframe)
        self.sortbutt.setMinimumSize(QtCore.QSize(160, 16777215))
        self.sortbutt.setMaximumSize(QtCore.QSize(160, 16777215))
        self.sortbutt.setStyleSheet("QComboBox {\n"
"    font-family: \"Merriweather Sans\";\n"
"    color: #fafafa;\n"
"    font-size: 15px;\n"
"    font-weight: bold;\n"
"    padding: 5px;\n"
"    border: 3px solid #DA99A5;\n"
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
        self.sortbutt.setObjectName("sortbutt")
        self.verticalLayout.addWidget(self.sortbutt)
        self.horizontalLayout_9.addWidget(self.sortframe)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        self.verticalLayout_4.addWidget(self.interactivesframe)
        self.table = ScalableBackgroundTable(self.allbotframe)




# Tintin was here - editing the font of the table
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setFamily("Merriweather Sans")
        self.table.setFont(font)

        self.table.setMinimumSize(QtCore.QSize(500, 350))
        self.table.setMaximumSize(QtCore.QSize(1900,350))
        self.table.setStyleSheet("""
                QTableView {
                        background: url("Pictures/welcomed.png");
                        background-repeat: repeat-y;
                        background-position: center;
                        background-origin: content;
                        background-attachment: scroll;
                        background-size: cover;
                                 
                        border: 2px solid #072A42;
                        border-radius: 6px;
                        gridline-color: #00416A;
                        selection-background-color: #CCE7FF;
                        font-family: "Merriweather Sans";
                        font-size: 14px;
                        background-color: #D8EDF3;
                        alternate-background-color: #D8EDF3;
                }

                QHeaderView::section {
                        background-color: #072A42;
                        color: white;
                        font-size: 14px;
                        padding: 5px;
                        border: none;
                }

                QTableView::item:selected {
                        color: #072A42;
                }
                """)
        self.table.setObjectName("table")



# Tintin was here - edit the design of the table
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.table.setFocusPolicy(Qt.NoFocus)
        self.verticalLayout_4.addWidget(self.table)



# Tintin was here - edit the header of the table
        header = self.table.horizontalHeader()
        font = QtGui.QFont("Merriweather Sans", 15)
        font.setBold(True)
        header.setFont(font)



# Tintin was here to enable the mouse tracking for the hover part
        self.table.setMouseTracking(True)


        
# Tintin was here - Add data model that stores information to be shown in views
        self.model = QtGui.QStandardItemModel(MainWindow)
        self.table.setModel(self.model)

        self.footerframe = QtWidgets.QFrame(self.allbotframe)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.footerframe.sizePolicy().hasHeightForWidth())
        self.footerframe.setSizePolicy(sizePolicy)
        self.footerframe.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.footerframe.setFrameShadow(QtWidgets.QFrame.Plain)
        self.footerframe.setObjectName("footerframe")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.footerframe)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem8 = QtWidgets.QSpacerItem(570, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem8)
        self.AREframe = QtWidgets.QFrame(self.footerframe)
        self.AREframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.AREframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.AREframe.setObjectName("AREframe")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.AREframe)
        self.horizontalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.addbutt = QtWidgets.QPushButton(self.AREframe)
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
        self.horizontalLayout_6.addWidget(self.addbutt)
        self.editbutt = QtWidgets.QPushButton(self.AREframe)
        self.editbutt.setStyleSheet("QPushButton {\n"
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
        self.editbutt.setObjectName("editbutt")
        self.horizontalLayout_6.addWidget(self.editbutt)
        self.removebutt = QtWidgets.QPushButton(self.AREframe)
        self.removebutt.setStyleSheet("QPushButton {\n"
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
        self.removebutt.setObjectName("removebutt")
        self.horizontalLayout_6.addWidget(self.removebutt)
        self.horizontalLayout_7.addWidget(self.AREframe)
        self.verticalLayout_4.addWidget(self.footerframe)
        self.verticalLayout_2.addWidget(self.allbotframe)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1038, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)



#TINTIN WAS HERE - hide some widgets upon starting
        self.sortbutt.hide()
        self.addbutt.hide()
        self.editbutt.hide()
        self.removebutt.hide()








        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)









# TINTIN WAS HERE to initialize the floating label if maghover
        self.hover_label = QLabel(self)
        self.hover_label.setStyleSheet("""
        QLabel {
        background-color: #FFFFFF;
        border: 2px solid #072A42;
        border-radius: 6px;
        padding: 6px;
        font-family: Merriweather Sans;
        font-size: 17px;
        color: #072A42;
        }
        """)
        self.hover_label.setFixedWidth(300)
        self.hover_label.setWordWrap(True)

        # Correct flags and attributes
        self.hover_label.setWindowFlags(Qt.ToolTip)
        self.hover_label.setAttribute(Qt.WA_TransparentForMouseEvents)
        self.hover_label.hide()

        self.hover_timer = QTimer()
        self.hover_timer.setSingleShot(True)
        self.hover_timer.timeout.connect(self.show_hover_label)

        self.hover_index = None
        self.hover_text = ""

        self.table.viewport().installEventFilter(self)



#TINTIN WAS HERE build the searchable data iinitialize and mga completer
        self.search_data = [] 
        self.build_search_data()
        self.setup_searchbar()



# TINTIN  WAS HERE - connecting to database
        self.callDB = DBManager()



# TINTIN WAS HERE - initializing table name later for the butts :3
        self.current_table = None



# TINTIN WAS HERE - Buttons for the tables
        self.Staffbutt.clicked.connect(self.staffbutt)
        self.Clientbutt.clicked.connect(self.clientbutt)
        self.Patientbutt.clicked.connect(self.patientbutt)
        self.Inventorybutt.clicked.connect(self.inventorybutt)
        self.Supplierbutt.clicked.connect(self.supplierbutt)



# TINTIN WAS HERE - to connect the buttons to their functions
        self.addbutt.clicked.connect(self.openAddPopup)
        self.editbutt.clicked.connect(self.openEditPopup)
        self.removebutt.clicked.connect(self.deleterow)
        self.searchbar.returnPressed.connect(self.on_search_enter)
        


#TINTIN WAS HERE to call a function that will handle what happens next if the sorbutt text is gonna be changed
        self.sortbutt.currentIndexChanged.connect(self.handle_sort_selection)



#TINTIN WAS HERE to pull searchable entries from each table
    def build_search_data(self):
        db = DBManager()
        db.connect_DB()
        kuryente = db.kuryente
        cable = db.cable

        tables = [
            ("stafftb", "Staff", ["CONCAT(first_name, ' ', last_name)", "Staff_ID"]),
            ("clientb", "Client", ["CONCAT(first_name, ' ', last_name)", "Client_ID"]),
            ("patienttb", "Patient", ["Name", "Patient_ID"]),
            ("inventorytb", "Inventory", ["Name", "Inventory_ID"]),
            ("suppliertb", "Supplier", ["CONCAT(first_name, ' ', last_name)", "Supplier_ID", "Notes"])
        ]
        
        self.search_data.clear()
        
        for tbl, display_tbl, columns in tables:
            for col in columns:
                try:
                    query = f"SELECT {col}, {columns[-1]} FROM {tbl}"
                    kuryente.execute(query)
                    for name_or_note, pk in kuryente.fetchall():
                        if name_or_note:
                            key = name_or_note.strip()
                            self.search_data.append((key, display_tbl, pk, tbl))
                except Exception as e:
                    print("Search load error", tbl, e)
        
        kuryente.close()
        cable.close()



#TINTIN WAS HERE to make the function for completer in searchbar
    def setup_searchbar(self):
        strings = [f"{name}: {table}" for name, table, _, _ in self.search_data]
        self.completer = SmartCompleter(strings, self.searchbar)
        self.popup=QListView()
        self.completer.setPopup(self.popup)

        self.completer.popup().setStyleSheet("""
                QListView {
                        font-family: "Merriweather Sans";
                        font-size: 18px;
                        background-color: #FAFAFA;
                        color: #072A42;
                        border: 1px solid #072A42;
                        padding: 2px;
                        selection-background-color: #D8EDF3;
                        selection-color: #DA99A5;
                }

                QListView::item:hover {
                        background-color: #FFE4E1; 
                        color: #072A42;
                }
                """)

        self.searchbar.setCompleter(self.completer)
        self.searchbar.returnPressed.connect(self.on_search_enter)
        self.completer.activated.connect(self.on_search_activate)



#TINTIN WAS HERE to handle all functions for search activation
    def on_search_enter(self):
        text = self.searchbar.text().strip()
        self.perform_search(text)



    def on_search_activate(self, text):
        self.perform_search(text)



    def perform_search(self, text):
        # Exact match
        for name, table_display, pk, tbl in self.search_data:
            label = f"{name}: {table_display}"
            if label.lower() == text.lower():
                self.show_table(tbl)
                self.highlight_pk(tbl, pk)
                return
            
        # No full match; allow partial
        for name, table_display, pk, tbl in self.search_data:
            if text.lower() in name.lower():
                self.show_table(tbl)
                self.highlight_pk(tbl, pk)
                return
        self.choosetb(f"No results found for '{text}'.")



    def show_table(self, tbl):
        self.current_table = tbl 
        self.displayDB(tbl)
        # TINTIN WAS HERE - Show table and controls when search activates it
        self.sortbutt.show()
        self.addbutt.show()
        self.editbutt.show()
        self.removebutt.show()



    def highlight_pk(self, tbl, pk):
        model = self.table.model()
        # iterate rows, find matching pk column
        col_index = {"stafftb":3, "clientb":1, "patienttb":2, 
                     "inventorytb":2, "suppliertb":1}[tbl]
        for r in range(model.rowCount()):
            if model.index(r, col_index).data() == pk:
                self.table.selectRow(r)
                self.table.scrollTo(model.index(r, col_index))
                break



# TINTIN WAS HERE to modify the table background each table
    def staffbutt (self):
        self.model.clear()
        self.current_table = "stafftb"
        self.displayDB("stafftb")

    def clientbutt (self):
        self.model.clear()
        self.current_table = "clientb"
        self.displayDB("clientb")

    def patientbutt (self):
        self.model.clear()
        self.current_table = "patienttb"
        self.displayDB("patienttb")

    def inventorybutt (self):
        self.model.clear()
        self.current_table = "inventorytb"
        self.displayDB("inventorytb")

    def supplierbutt (self):
        self.model.clear()
        self.current_table = "suppliertb"
        self.displayDB("suppliertb")



# Tintin was here to display the picture sa mga tab and specify the function called above
    def setTableBackground(self, image_path):
        self.table.setStyleSheet(f"""
                QTableView {{
                        background: white url("{image_path}") repeat-y center;
                        border: 3px solid #072A42;
                        border-radius: 6px;
                }}

                QTableView::item {{
                        selection-background-color: rgba(0, 128, 255, 60);
                        selection-color: black;
                }}

                QHeaderView::section {{
                        background-color: #00416A;
                        color: white;
                        font-weight: bold;
                        font-size: 15px;
                }}
                
                QHeaderView::section:pressed,
                QHeaderView::section:checked,
                QHeaderView::section:focus {{
                        background-color: #00416A;
                }}
        """)

# TINTIN WAS HERE to display the values inputted into SQL (either manual or thru pop ups) to the table
    def displayDB (self, table):
        try:
            self.sortbutt.clear()

            self.sortbutt.show()
            self.addbutt.show()
            self.editbutt.show()
            self.removebutt.show()

            self.sortbutt.blockSignals(True)
            self.sortbutt.clear()

            if table == "stafftb":
                self.sortbutt.addItems(["Staff-ID", "Last Name", "Position", "Status"])
                self.table.setBackgroundImage("")
                self.setTableBackground("Pictures/StaffTB.png")

            if table == "clientb":
                self.sortbutt.addItems(["Client-ID", "Last Name", "Status"])
                self.table.setBackgroundImage("")
                self.setTableBackground("Pictures/ClientTB.png")
            
            if table == "patienttb":
                self.sortbutt.addItems(["Patient-ID", "Name", "Owner", "Species", "Breed", "Sex", "Status"])
                self.table.setBackgroundImage("")
                self.setTableBackground("Pictures/PatientTB.png")

            if table == "inventorytb":
                self.sortbutt.addItems(["Inventory-ID", "Name", "Type", "Unit", "Price"])
                self.table.setBackgroundImage("")
                self.setTableBackground("Pictures/InventoryTB.png")
        
            if table == "suppliertb":
                self.sortbutt.addItems(["Supplier-ID", "Last Name", "Company"])
                self.table.setBackgroundImage("")
                self.setTableBackground("Pictures/SupplierTB.png")

            self.sortbutt.blockSignals(False)

            self.callDB.connect_DB()
            kuryente = self.callDB.kuryente
            cable = self.callDB.cable

            self.model = QtGui.QStandardItemModel()
            self.table.setModel(self.model)
            
            if table == "stafftb":
                kuryente.execute("""
                        SELECT 
                                CONCAT(First_name, ' ', Last_name) AS Name, 
                                Position, 
                                PRC_LN, 
                                Staff_ID, 
                                `Contact_Number`, 
                                `Date_Hired`, 
                                Status 
                        FROM stafftb
                """)

            elif table == "clientb":
                kuryente.execute("""
                        SELECT 
                                CONCAT(First_name, ' ', Last_name) AS Name, 
                                Client_ID, 
                                `Contact_Number`,  
                                Address,
                                Status
                        FROM clientb
                """)

            elif table == "suppliertb":
                kuryente.execute("""
                        SELECT 
                                CONCAT(First_name, ' ', Last_name) AS Name, 
                                Supplier_ID,
                                Company,
                                `Contact_Number`,  
                                Notes
                        FROM suppliertb
                """)
            else:
                kuryente.execute(f"SELECT * FROM {table}")

            row_table = kuryente.fetchall()
            column_table = [desc[0].replace("_", " ") for desc in kuryente.description]


            self.model.setHorizontalHeaderLabels(column_table)
            self.model.removeRows(0, self.model.rowCount())

            for i in row_table:
                new_row = []
                for value in i:
                        value = value if value is not None else ""
                        item = QtGui.QStandardItem(str(value))
                        item.setData(str(value), Qt.UserRole)
                        new_row.append(item)
                self.model.appendRow(new_row)


            self.apply_status_coloring(table)

        except Exception as e:
            print(f"Error occurred from {table}: {e}")
        finally:
                kuryente.close()
                cable.close()


        
# TINTIN WAS HERE to make a function unsay buhaton if machange ang sortbox
    def handle_sort_selection(self):
        current_option = self.sortbutt.currentText()
        current_table = self.current_table

    # Handle default sort options early (NO DB NEEDED)
        if current_table == "stafftb" and current_option == "Staff-ID":
                self.displayDB("stafftb")
                self.highlight_column_by_name("Staff_ID")
                return
        elif current_table == "clientb" and current_option == "Client-ID":
                self.displayDB("clientb")
                self.highlight_column_by_name("Client_ID")
                return
        elif current_table == "patienttb" and current_option == "Patient-ID":
                self.displayDB("patienttb")
                self.highlight_column_by_name("Patient_ID")
                return
        elif current_table == "inventorytb" and current_option == "Inventory-ID":
                self.displayDB("inventorytb")
                self.highlight_column_by_name("Inventory_ID")
                return
        elif current_table == "suppliertb" and current_option == "Supplier-ID":
                self.displayDB("suppliertb")
                self.highlight_column_by_name("Supplier_ID")
                return

    # Only connect if we're not returning early
        db = DBManager()
        db.connect_DB()
        kuryente = db.kuryente
        cable = db.cable

        try:
                # Table-specific queries
                if current_table == "stafftb":
                        if current_option == "Staff-ID":
                                self.displayDB("stafftb")
                                return

                        elif current_option == "Last Name":
                                query = """
                                SELECT 
                                CONCAT(last_name, ', ', first_name) AS Name,
                                Position,
                                PRC_LN,
                                Staff_ID,
                                Contact_Number,
                                Date_Hired,
                                Status
                                FROM stafftb
                                ORDER BY last_name
                                """

                        elif current_option == "Position":
                                query = """
                                SELECT 
                                CONCAT(first_name, ' ', last_name) AS Name,
                                Position,
                                PRC_LN,
                                Staff_ID,
                                Contact_Number,
                                Date_Hired,
                                Status
                                FROM stafftb
                                ORDER BY
                                CASE Position
                                        WHEN 'Owner' THEN 1
                                        WHEN 'Veterinarian' THEN 2
                                        WHEN 'Veterinarian Asst.' THEN 3
                                        WHEN 'Secretary' THEN 4
                                        WHEN 'Asst. Secretary' THEN 5
                                        ELSE 6
                                END
                                """

                        elif current_option == "Status":
                                query = """
                                SELECT 
                                CONCAT(first_name, ' ', last_name) AS Name,
                                Position,
                                PRC_LN,
                                Staff_ID,
                                Contact_Number,
                                Date_Hired,
                                Status
                                FROM stafftb
                                ORDER BY
                                CASE Status
                                        WHEN 'Active' THEN 1
                                        WHEN 'Part-time' THEN 2
                                        WHEN 'On Leave' THEN 3
                                        WHEN 'Dismissed' THEN 4
                                        ELSE 5
                                END
                                """

                elif current_table == "clientb":
                        if current_option == "Client-ID":
                                self.displayDB("clientb")
                                return

                        elif current_option == "Last Name":
                                query = """
                                SELECT 
                                CONCAT(last_name, ', ', first_name) AS Name,
                                Client_ID,
                                Contact_Number,
                                Address,
                                Status
                                FROM clientb
                                ORDER BY last_name
                                """

                        elif current_option == "Status":
                                query = """
                                SELECT 
                                CONCAT(first_name, ' ', last_name) AS Name,
                                Client_ID,
                                Contact_Number,
                                Address,
                                Status
                                FROM clientb
                                ORDER BY
                                CASE Status
                                        WHEN 'Pending' THEN 1
                                        WHEN 'No Balance' THEN 2
                                        ELSE 3
                                END
                                """


                elif current_table == "patienttb":
                        if current_option == "Patient-ID":
                                self.displayDB("patienttb")
                                return

                        elif current_option == "Name":
                                query = """
                                SELECT 
                                Name,
                                Owner,
                                Patient_ID,
                                Species,
                                Breed,
                                Birthdate,
                                Sex,
                                Status
                                FROM patienttb 
                                ORDER BY Name
                                """

                        elif current_option == "Owner":
                                query = """
                                SELECT 
                                Name,
                                Owner,
                                Patient_ID,
                                Species,
                                Breed,
                                Birthdate,
                                Sex,
                                Status
                                FROM patienttb 
                                ORDER BY Owner
                                """

                        elif current_option == "Species":
                                query = """
                                SELECT 
                                Name,
                                Owner,
                                Patient_ID,
                                Species,
                                Breed,
                                Birthdate,
                                Sex,
                                Status
                                FROM patienttb 
                                ORDER BY Species
                                """

                        elif current_option == "Breed":
                                query = """
                                SELECT 
                                Name,
                                Owner,
                                Patient_ID,
                                Species,
                                Breed,
                                Birthdate,
                                Sex,
                                Status
                                FROM patienttb 
                                ORDER BY Breed
                                """

                        elif current_option == "Sex":
                                query = """
                                SELECT 
                                Name,
                                Owner,
                                Patient_ID,
                                Species,
                                Breed,
                                Birthdate,
                                Sex,
                                Status
                                FROM patienttb 
                                ORDER BY 
                                CASE Sex
                                        WHEN 'Hermaphrodite' THEN 1
                                        WHEN 'Female' THEN 2
                                        WHEN 'Male' THEN 3
                                        ELSE 4
                                END
                                """
                        elif current_option == "Status":
                                query = """
                                SELECT 
                                Name,
                                Owner,
                                Patient_ID,
                                Species,
                                Breed,
                                Birthdate,
                                Sex,
                                Status
                                FROM patienttb 
                                ORDER BY 
                                CASE Status
                                        WHEN 'Deceased' THEN 1
                                        WHEN 'Alive' THEN 2
                                        ELSE 3
                                END
                                """


                elif current_table == "inventorytb":
                        if current_option == "Inventory-ID":
                                self.displayDB("inventorytb")
                                return

                        elif current_option == "Name":
                                query = """
                                SELECT 
                                Name,
                                Type,
                                Inventory_ID,
                                Quantity,
                                Unit,
                                Stock,
                                `Price(PHP)`
                                FROM inventorytb 
                                ORDER BY Name
                                """

                        elif current_option == "Type":
                                query = """
                                SELECT 
                                Name,
                                Type,
                                Inventory_ID,
                                Quantity,
                                Unit,
                                Stock,
                                `Price(PHP)`
                                FROM inventorytb 
                                ORDER BY
                                CASE Type
                                        WHEN 'Services' THEN 1
                                        WHEN 'Diagnostic' THEN 2
                                        WHEN 'Medicine' THEN 3
                                        WHEN 'Vitamins' THEN 4
                                        WHEN 'Others' THEN 5
                                END
                                """

                        elif current_option == "Unit":
                                query = """
                                SELECT 
                                Name,
                                Type,
                                Inventory_ID,
                                Quantity,
                                Unit,
                                Stock,
                                `Price(PHP)`
                                FROM inventorytb 
                                ORDER BY Unit
                                """
                        
                        elif current_option == "Price":
                                query = """
                                SELECT 
                                Name,
                                Type,
                                Inventory_ID,
                                Quantity,
                                Unit,
                                Stock,
                                `Price(PHP)`
                                FROM inventorytb 
                                ORDER BY `Price(PHP)` ASC;
                                """


                elif current_table == "suppliertb":
                        if current_option == "Supplier-ID":
                                self.displayDB("suppliertb")
                                return

                        elif current_option == "Last Name":
                                query = """
                                SELECT 
                                CONCAT(last_name, ', ', first_name) AS Name,
                                Supplier_ID,
                                Company,
                                Contact_Number,
                                Notes
                                FROM suppliertb 
                                ORDER BY last_name
                                """

                        elif current_option == "Company":
                                query = """
                                SELECT 
                                CONCAT(last_name, ', ', first_name) AS Name,
                                Supplier_ID,
                                Company,
                                Contact_Number,
                                Notes
                                FROM suppliertb 
                                ORDER BY Company
                                """

                                
                else:
                        return  

                if "query" not in locals():
                        print("Sort error: no valid query matched (this is fine!)")
                        return
                
                kuryente.execute(query)
                results = kuryente.fetchall()
                headers = [desc[0].replace("_", " ") for desc in kuryente.description]
                self.populate_table(results, headers)

                header_map = {
                        "Staff-ID": "Staff_ID",
                        "Client-ID": "Client_ID",
                        "Patient-ID": "Patient_ID",
                        "Inventory-ID": "Inventory_ID",
                        "Supplier-ID": "Supplier_ID",
                        "Last Name": "Name",
                        "Price": "Price(PHP)",
                        }

                highlight_col_name = header_map.get(current_option, current_option)

                if highlight_col_name in headers:
                        col_index = headers.index(highlight_col_name)
                        self.highlight_column(col_index)

                if current_option == "Status":
                        self.apply_status_cell_coloring(current_table)

                if current_table == "patienttb" and current_option == "Owner":
                        self.apply_status_cell_coloring("patienttb", column_name="Owner")

        except Exception as e:
                print("Sort error:", e)

        finally:
                kuryente.close()
                cable.close()



#TINTIN WAS HERE for specific highlighting
    def apply_status_coloring(self, table):
        status_colors = {
                "stafftb": {
                "Active": QtGui.QColor("#57A773"),
                "On Leave": QtGui.QColor("#888888"),
                "Part-time": QtGui.QColor("#4C90D0"),
                "Dismissed": QtGui.QColor("#DA99A5"),
                },
                "clientb": {
                "No Balance": QtGui.QColor("#57A773"),
                },
                "patienttb": {
                "Alive": QtGui.QColor("#57A773"),
                "Deceased": QtGui.QColor("#DA99A5"),
                "DeletedOwner": QtGui.QColor("#888888"),
                }
        }

        if table not in status_colors:
                return

        headers = [self.model.horizontalHeaderItem(i).text().replace(" ", "_") for i in range(self.model.columnCount())]
        if "Status" not in headers:
                return
        col_index = headers.index("Status")

        for row in range(self.model.rowCount()):
                item = self.model.item(row, col_index)
                if not item:
                        continue

                value = item.text()

                # Client special check
                if table == "clientb" and value.startswith("Pending:"):
                        item.setForeground(QtGui.QColor("#DA99A5"))
                elif value in status_colors[table]:
                        item.setForeground(status_colors[table][value])
        if table == "patienttb" and "Owner" in headers:
                owner_index = headers.index("Owner")
                for row in range(self.model.rowCount()):
                        owner_item = self.model.item(row, owner_index)
                        if owner_item and owner_item.text().startswith("[Client Deleted:"):
                                owner_item.setForeground(status_colors[table]["DeletedOwner"])
                                font = owner_item.font()
                                font.setItalic(True)
                                owner_item.setFont(font)



    def apply_status_cell_coloring(self, table, column_name="Status"):
        headers = [self.model.horizontalHeaderItem(i).text() for i in range(self.model.columnCount())]
        if column_name not in headers:
                return

        col_index = headers.index(column_name)

        for row in range(self.model.rowCount()):
                item = self.model.item(row, col_index)
                if not item:
                        continue
                value = item.text()

                # Special for Owner column in patienttb
                if table == "patienttb" and column_name == "Owner":
                        if value.startswith("[Client Deleted:"):
                                item.setBackground(QtGui.QColor("#E0E0E0"))
                                item.setForeground(QtGui.QColor("#fafafa"))
                                italic_font = item.font()
                                italic_font.setItalic(True)
                                item.setFont(italic_font)
                                continue

                if table == "stafftb":
                        if value.startswith("Active"):
                                item.setBackground(QtGui.QColor("#C7F6D0"))
                                item.setForeground(QtGui.QColor("#57A773"))
                        elif value.startswith("On Leave"):
                                item.setBackground(QtGui.QColor("#E0E0E0"))
                                item.setForeground(QtGui.QColor("#fafafa"))
                        elif value.startswith("Part-time"):
                                item.setBackground(QtGui.QColor("#D3E8F9"))
                                item.setForeground(QtGui.QColor("#4C90D0"))
                        elif value.startswith("Dismissed"):
                                item.setBackground(QtGui.QColor("#FAD4DB"))
                                item.setForeground(QtGui.QColor("#DD5C6D"))

                elif table == "clientb":
                        if value.startswith("Pending:"):
                                item.setBackground(QtGui.QColor("#FAD4DB"))
                                item.setForeground(QtGui.QColor("#DD5C6D"))
                        elif value.startswith("No Balance"):
                                item.setBackground(QtGui.QColor("#C7F6D0"))
                                item.setForeground(QtGui.QColor("#57A773"))

                elif table == "patienttb":
                        if value.startswith("Deceased"):
                                item.setBackground(QtGui.QColor("#FAD4DB"))
                                item.setForeground(QtGui.QColor("#DD5C6D"))
                        elif value.startswith("Alive"):
                                item.setBackground(QtGui.QColor("#C7F6D0"))
                                item.setForeground(QtGui.QColor("#57A773"))




#TINTIN WAS HERE TO populate the table 
    def populate_table(self, data, headers):
        self.model.clear()
        self.model.setHorizontalHeaderLabels(headers)

        for row_data in data:
                row_items = []
                for value in row_data:
                        value = value if value is not None else ""
                        item = QtGui.QStandardItem(str(value))
                        item.setData(str(value), Qt.UserRole)
                        row_items.append(item)
                self.model.appendRow(row_items)

        self.apply_status_coloring(self.current_table)




#TINTIN WAS HERE to highlight the columns depending on the sort option
    def highlight_column(self, col_index):
        for row in range(self.model.rowCount()):
                item = self.model.item(row, col_index)
                if item:
                        item.setBackground(QtGui.QColor("#DA99A5"))
                        item.setForeground(QtGui.QColor("#fafafa"))



#TINTIN WAS HERE to highlight the column for IDs as well
    def highlight_column_by_name(self, header_name):
        headers = [self.model.horizontalHeaderItem(i).text().replace(" ", "_") for i in range(self.model.columnCount())]
        if header_name in headers:
                col_index = headers.index(header_name)
                self.highlight_column(col_index)




# Tintin was here to connect the add button to add pop-ups
    def openAddPopup(self):

        if self.current_table == "stafftb":
            dialog = AddStaffControl()
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                self.displayDB("stafftb")

        elif self.current_table == "clientb":
            dialog = AddClientControl()
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                self.displayDB("clientb")

        elif self.current_table == "patienttb":
            dialog = AddPatientControl()
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                self.displayDB("patienttb")
            
        elif self.current_table == "inventorytb":
            dialog = AddInventoryControl()
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                self.displayDB("inventorytb")
            
        elif self.current_table == "suppliertb":
            dialog = AddSupplierControl()
            if dialog.exec_() == QtWidgets.QDialog.Accepted:
                self.displayDB("suppliertb")

        else:
            self.choosetb("Oops! Please select a table first ૮₍ • ᴥ • ₎ა.")



#TINTIN WAS HERE to connect the edit button to edit pop ups
    def openEditPopup(self):
        global skip_update_confirmation_flag

        if not self.current_table:
                self.choosetb("Oops! Please select a table first ૮₍ • ᴥ • ₎ა.")
                return

        selected_row = self.table.currentIndex().row()
        if selected_row == -1:
                self.choosetb("Please select a row to edit! ᓚ₍ ^. .^₎")
                return

        model = self.table.model()
        row_data = []

        for col in range(model.columnCount()):
                index = model.index(selected_row, col)
                data = model.data(index)
                row_data.append(data if data else "")

        #This is where u start "un-CONCAT-ing" the names T_T for stafftb, clienttb, and suppliertb

        if self.current_table == "stafftb":
                index = model.index(selected_row, 3)
                staff_id = model.data(index)  

                self.callDB.connect_DB()
                kuryente = self.callDB.kuryente
                cable = self.callDB.cable

                try:
                        kuryente.execute("""
                                SELECT 
                                        First_name, 
                                        Last_name, 
                                        Position, 
                                        PRC_LN, 
                                        Staff_ID, 
                                        `Contact_Number`, 
                                        `Date_Hired`, 
                                        Status 
                                FROM stafftb
                                WHERE Staff_ID = %s
                        """, (staff_id,))
                        result = kuryente.fetchone()

                        if result:
                                row_data = [str(i) if i is not None else "" for i in result]
                        else:
                                self.choosetb("Error: No matching staff data found.")
                                return

                except Exception as e:
                        self.choosetb(f"Database error while fetching staff: {e}")
                        return
                finally:
                        kuryente.close()
                        cable.close()
                
                dialog = AddStaffControl(existing_data=row_data, skip_update_confirmation=globalsession.skip_update_confirmation_flag)

                if dialog.exec_() == QtWidgets.QDialog.Accepted:
                        skip_update_confirmation_flag = dialog.skip_update_confirmation
                        self.displayDB("stafftb")


        elif self.current_table == "clientb":
                index = model.index(selected_row, 1)
                Client_ID = model.data(index)  

                self.callDB.connect_DB()
                kuryente = self.callDB.kuryente
                cable = self.callDB.cable

                try:
                        kuryente.execute("""
                                SELECT 
                                        First_name, 
                                        Last_name, 
                                        Client_ID, 
                                        `Contact_Number`, 
                                        Address,
                                        Status 
                                FROM clientb
                                WHERE Client_ID = %s
                        """, (Client_ID,))
                        result = kuryente.fetchone()

                        if result:
                                row_data = [str(i) if i is not None else "" for i in result]
                        else:
                                self.choosetb("Error: No matching client data found.")
                                return

                except Exception as e:
                        self.choosetb(f"Database error while fetching staff: {e}")
                        return
                finally:
                        kuryente.close()
                        cable.close()

                dialog = AddClientControl(existing_data=row_data, skip_update_confirmation=globalsession.skip_update_confirmation_flag)

                if dialog.exec_() == QtWidgets.QDialog.Accepted:
                        skip_update_confirmation_flag = dialog.skip_update_confirmation
                        self.displayDB("clientb")


        elif self.current_table == "patienttb":
                index = model.index(selected_row, 2)
                Patient_ID = model.data(index)  

                self.callDB.connect_DB()
                kuryente = self.callDB.kuryente
                cable = self.callDB.cable

                try:
                        kuryente.execute("""
                                SELECT 
                                        Name, 
                                        Owner, 
                                        Patient_ID, 
                                        Species, 
                                        Breed,
                                        Birthdate,
                                        Sex,
                                        Status 
                                FROM patienttb
                                WHERE Patient_ID = %s
                        """, (Patient_ID,))
                        result = kuryente.fetchone()

                        if result:
                                row_data = [str(i) if i is not None else "" for i in result]
                        else:
                                self.choosetb("Error: No matching client data found.")
                                return

                except Exception as e:
                        self.choosetb(f"Database error while fetching staff: {e}")
                        return
                finally:
                        kuryente.close()
                        cable.close()

                dialog = AddPatientControl(existing_data=row_data, skip_update_confirmation=globalsession.skip_update_confirmation_flag)

                if dialog.exec_() == QtWidgets.QDialog.Accepted:
                        skip_update_confirmation_flag = dialog.skip_update_confirmation
                        self.displayDB("patienttb")


        elif self.current_table == "inventorytb":
                index = model.index(selected_row, 2)
                Inventory_ID = model.data(index)  

                self.callDB.connect_DB()
                kuryente = self.callDB.kuryente
                cable = self.callDB.cable

                try:
                        kuryente.execute("""
                                SELECT 
                                        Name, 
                                        Type, 
                                        Inventory_ID, 
                                        Quantity, 
                                        Unit,
                                        Stock,
                                        `Price(PHP)` 
                                FROM inventorytb
                                WHERE Inventory_ID = %s
                        """, (Inventory_ID,))
                        result = kuryente.fetchone()

                        if result:
                                row_data = [str(i) if i is not None else "" for i in result]
                        else:
                                self.choosetb("Error: No matching client data found.")
                                return

                except Exception as e:
                        self.choosetb(f"Database error while fetching staff: {e}")
                        return
                finally:
                        kuryente.close()
                        cable.close()

                dialog = AddInventoryControl(existing_data=row_data, skip_update_confirmation=globalsession.skip_update_confirmation_flag)

                if dialog.exec_() == QtWidgets.QDialog.Accepted:
                        skip_update_confirmation_flag = dialog.skip_update_confirmation
                        self.displayDB("inventorytb")


        elif self.current_table == "suppliertb":
                index = model.index(selected_row, 1)
                Supplier_ID = model.data(index)  

                self.callDB.connect_DB()
                kuryente = self.callDB.kuryente
                cable = self.callDB.cable

                try:
                        kuryente.execute("""
                                SELECT 
                                        First_name, 
                                        Last_name, 
                                        Supplier_ID,
                                        Company, 
                                        `Contact_Number`, 
                                         Notes
                                FROM suppliertb
                                WHERE Supplier_ID = %s
                        """, (Supplier_ID,))
                        result = kuryente.fetchone()

                        if result:
                                row_data = [str(i) if i is not None else "" for i in result]
                        else:
                                self.choosetb("Error: No matching client data found.")
                                return

                except Exception as e:
                        self.choosetb(f"Database error while fetching staff: {e}")
                        return
                finally:
                        kuryente.close()
                        cable.close()

                dialog = AddSupplierControl(existing_data=row_data, skip_update_confirmation=globalsession.skip_update_confirmation_flag)
                
                if dialog.exec_() == QtWidgets.QDialog.Accepted:
                        skip_update_confirmation_flag = dialog.skip_update_confirmation
                        self.displayDB("suppliertb")

        else:
                self.choosetb("Unsupported table.")



#TINTIN WAS HERE to select a row to delete
    def deleterow(self):
        if not self.current_table:
                self.choosetb("Oops! Please select a table first ૮₍ • ᴥ • ₎ა.")
                return

        selected_row = self.table.currentIndex().row()
        if selected_row == -1:
                self.choosetb("Please select a row to delete! (｡•́︿•̀｡)")
                return

        model = self.table.model()

        if self.current_table == "stafftb":
                index = model.index(selected_row, 3)
                staff_id = model.data(index)

                if not globalsession.skip_delete_confirmation_flag:
                        confirm_dialog = DeleteCon(table_name="stafftb")
                        result = confirm_dialog.exec_()

                        if result == QDialog.Accepted:
                                if confirm_dialog.skip_dialog:
                                        globalsession.skip_delete_confirmation_flag = True
                                self.actuallydelete(staff_id)

                        else:
                                self.choosetb("Deletion cancelled. ₍ᐢ. .ᐢ₎")
                else:
                        self.actuallydelete(staff_id)
        
        elif self.current_table == "clientb":
                index = model.index(selected_row, 1)
                client_id = model.data(index)

                if not globalsession.skip_delete_confirmation_flag:
                        confirm_dialog = DeleteCon(table_name="clientb")
                        result = confirm_dialog.exec_()

                        if result == QDialog.Accepted:
                                if confirm_dialog.skip_dialog:
                                        globalsession.skip_delete_confirmation_flag = True
                                self.actuallydelete(client_id)

                        else:
                                self.choosetb("Deletion cancelled. ₍ᐢ. .ᐢ₎")
                else:
                        self.actuallydelete(client_id)

        elif self.current_table == "patienttb":
                index = model.index(selected_row, 2)
                patient_id = model.data(index)

                if not globalsession.skip_delete_confirmation_flag:
                        confirm_dialog = DeleteCon(table_name="patienttb")
                        result = confirm_dialog.exec_()

                        if result == QDialog.Accepted:
                                if confirm_dialog.skip_dialog:
                                        globalsession.skip_delete_confirmation_flag = True
                                self.actuallydelete(patient_id)

                        else:
                                self.choosetb("Deletion cancelled. ₍ᐢ. .ᐢ₎")
                else:
                        self.actuallydelete(patient_id)

        elif self.current_table == "inventorytb":
                index = model.index(selected_row, 2)
                inventory_id = model.data(index)

                if not globalsession.skip_delete_confirmation_flag:
                        confirm_dialog = DeleteCon(table_name="inventorytb")
                        result = confirm_dialog.exec_()

                        if result == QDialog.Accepted:
                                if confirm_dialog.skip_dialog:
                                        globalsession.skip_delete_confirmation_flag = True
                                self.actuallydelete(inventory_id)

                        else:
                                self.choosetb("Deletion cancelled. ₍ᐢ. .ᐢ₎")
                else:
                        self.actuallydelete(inventory_id)

        elif self.current_table == "suppliertb":
                index = model.index(selected_row, 1)
                supplier_id = model.data(index)

                if not globalsession.skip_delete_confirmation_flag:
                        confirm_dialog = DeleteCon(table_name="suppliertb")
                        result = confirm_dialog.exec_()

                        if result == QDialog.Accepted:
                                if confirm_dialog.skip_dialog:
                                        globalsession.skip_delete_confirmation_flag = True
                                self.actuallydelete(supplier_id)

                        else:
                                self.choosetb("Deletion cancelled. ₍ᐢ. .ᐢ₎")
                else:
                        self.actuallydelete(supplier_id)

        else:
               self.choosetb("Unsupported row!")


#TINTIN WAS HERE to actually delete
    def actuallydelete(self, id):
        self.callDB.connect_DB()
        kuryente = self.callDB.kuryente
        cable = self.callDB.cable

        try:
                if self.current_table == "stafftb":
                        kuryente.execute("DELETE FROM stafftb WHERE Staff_ID = %s", (id,))

                elif self.current_table == "clientb":
                        kuryente.execute("SELECT CONCAT(first_name, ' ', last_name) FROM clientb WHERE Client_ID =%s", (id,))
                        client_name = kuryente.fetchone()[0]

                        if client_name:
                                placeholder_owner = f"[Client Deleted: {client_name}]"
                                kuryente.execute("UPDATE patienttb SET Owner = %s WHERE Owner =%s", (placeholder_owner, client_name))

                        kuryente.execute("DELETE FROM clientb WHERE Client_ID = %s", (id,))

                elif self.current_table == "patienttb":
                        kuryente.execute("DELETE FROM patienttb WHERE Patient_ID = %s", (id,))

                elif self.current_table == "inventorytb":
                        kuryente.execute("DELETE FROM inventorytb WHERE Inventory_ID = %s", (id,))

                elif self.current_table == "suppliertb":
                        kuryente.execute("DELETE FROM suppliertb WHERE Supplier_ID = %s", (id,))

                else:
                        self.choosetb("Oops! Unsupported table for deletion. ( •̥́ ˍ •̀ू )")
                        return


                cable.commit()
                self.displayDB(self.current_table)


                if self.current_table == "stafftb":
                        self.choosetb("Staff successfully deleted.\n See you later!")

                elif self.current_table == "clientb":
                        self.choosetb("Client successfully deleted.\n Goodbye!")

                elif self.current_table == "patienttb":
                        self.choosetb("Patient successfully deleted.\n See you around, fur friend.")

                elif self.current_table == "inventorytb":
                        self.choosetb("Inventory successfuly deleted.\n Bye-bye!")

                elif self.current_table == "suppliertb":
                        self.choosetb("Supplier successfuly deleted.\n Thank you for everything!")

                else:
                        self.choosetb("Successfully deleted!")
                        

        except Exception as e:
                self.choosetb(f"Error deleting row: {e}")

        finally:
                kuryente.close()
                cable.close()



#TINTIN WAS HERE to define what happens BTS during hover
    def eventFilter(self, obj, event):
        if obj == self.table.viewport():
                if event.type() == QEvent.MouseMove:
                        index = self.table.indexAt(event.pos())

                        if index != self.hover_index:
                                self.hover_timer.stop()
                                self.hover_label.hide()
                                self.hover_index = index

                                if index.isValid():
                                        text = index.data()
                                        if text and len(str(text)) > 20:
                                                self.hover_text = text
                                                self.hover_timer.start(700)  # 0.7 seconds
                                else:
                                        self.hover_text = ""
                        elif event.type() in (QEvent.Leave, QEvent.MouseButtonPress):
                                self.hover_timer.stop()
                                self.hover_label.hide()
                                self.hover_index = None

        return super().eventFilter(obj, event)





#TINTIN WAS HERE for the function that displays the label
    def show_hover_label(self):
        if not self.hover_index:
                return

        rect = self.table.visualRect(self.hover_index)
        global_pos = self.table.viewport().mapToGlobal(rect.bottomLeft())

        self.hover_label.setText(self.hover_text)
        self.hover_label.adjustSize()

        # Position: directly below the cell, aligned to left
        self.hover_label.move(global_pos + QPoint(0, 4))  # small vertical offset
        self.hover_label.show()







#TINTIN WAS HERE to customize warning qmessagebox
    def choosetb(self, message):
                dialog = QtWidgets.QDialog()
                uic.loadUi("Warning/warningchoosetb.ui", dialog)

                dialog.setWindowTitle("Hold on!")
                dialog.text.setText(message)
                dialog.okbutt.clicked.connect(dialog.accept) 
                dialog.text.setAlignment(Qt.AlignCenter)
                QApplication.beep()

                dialog.exec_()



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Healing Paws Animal Clinic Veterinary Information System"))
        self.Title1.setText(_translate("MainWindow", "Healing Paws"))
        self.Title2.setText(_translate("MainWindow", "Animal Clinic"))
        self.Subtitle.setText(_translate("MainWindow", "Information System"))
        self.Staffbutt.setText(_translate("MainWindow", "Staff"))
        self.Clientbutt.setText(_translate("MainWindow", "Client"))
        self.Patientbutt.setText(_translate("MainWindow", "Patient"))
        self.Inventorybutt.setText(_translate("MainWindow", "Inventory"))
        self.Supplierbutt.setText(_translate("MainWindow", "Supplier"))
        self.searchbar.setPlaceholderText(_translate("MainWindow", "Search..."))
        self.addbutt.setText(_translate("MainWindow", "Add"))
        self.editbutt.setText(_translate("MainWindow", "Edit"))
        self.removebutt.setText(_translate("MainWindow", "Remove"))






