from PyQt5.QtWidgets import QDialog
from Warning.updateconfirmation import Ui_Dialog
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtCore import QUrl
from Pictures import Hpac_rc
from PyQt5.QtGui import QPixmap, QIcon

class UpdateCon(QDialog):
    def __init__(self, table_name):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.skip_dialog = False

        self.setWin (table_name)

        self.setImage(table_name)

        self.ui.yesbutt.clicked.connect(self.confirm)
        self.ui.nobutt.clicked.connect(self.reject)

        self.playsound()

    def setWin (self, table_name):
        if table_name == "stafftb":
                self.setWindowIcon(QIcon("Pictures/Staff.png"))
                self.setWindowTitle("Update Staff?")

        elif table_name == "clientb":
                self.setWindowIcon(QIcon("Pictures/Client.png"))
                self.setWindowTitle("Update Client?")

        elif table_name == "patienttb":
                self.setWindowIcon(QIcon("Pictures/Patient.png"))
                self.setWindowTitle("Update Patient?")

        elif table_name == "inventorytb":
                self.setWindowIcon(QIcon("Pictures/Inventory.png"))
                self.setWindowTitle("Update Inventory?")

        elif table_name == "suppliertb":
                self.setWindowIcon(QIcon("Pictures/Supplier.png"))
                self.setWindowTitle("Update supplier?")

        else:
                self.setWindowIcon(QIcon("Pictures/logowin.png"))
                self.setWindowTitle("Update?")

    def playsound(self):
        self.sound = QSoundEffect()
        self.sound.setSource(QUrl.fromLocalFile("Sounds/catnotif.wav"))
        self.sound.setVolume(0.8)
        self.sound.play()

    def confirm(self):
        self.skip_dialog = self.ui.checkBox.isChecked()
        self.accept()

    def setImage(self, table_name):
        if table_name == "stafftb":
            self.ui.label_2.setPixmap(QPixmap("Pictures/Staff.png"))
        elif table_name == "clientb":
            self.ui.label_2.setPixmap(QPixmap("Pictures/Client.png"))
            self.ui.label.setText("Are you sure you want to update this client's information?                                   Changes cannot be undone unless you edit it again! （• ˕ •マ")
        elif table_name == "patienttb":
            self.ui.label_2.setPixmap(QPixmap("Pictures/Patient.png"))
            self.ui.label.setText("Are you sure you want to update this patient's information?                                   Changes cannot be undone unless you edit it again! （• ˕ •マ")
        elif table_name == "inventorytb":
            self.ui.label_2.setPixmap(QPixmap("Pictures/Inventory.png"))
            self.ui.label.setText("Are you sure you want to update this inventory's information?                                   Changes cannot be undone unless you edit it again! （• ˕ •マ")
        elif table_name == "suppliertb":
            self.ui.label_2.setPixmap(QPixmap("Pictures/Supplier.png"))
            self.ui.label.setText("Are you sure you want to update this supplier's information?                                   Changes cannot be undone unless you edit it again! （• ˕ •マ")
        else:
            self.ui.label_2.setPixmap(QPixmap("Pictures/Staff.png"))