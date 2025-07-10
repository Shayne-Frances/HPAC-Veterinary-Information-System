from PyQt5.QtWidgets import QDialog
from Warning.deleteconfirmation import Ui_Dialog
from PyQt5.QtMultimedia import QSoundEffect
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QPixmap, QIcon

class DeleteCon(QDialog):
    def __init__(self, table_name="stafftb"):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.skip_dialog = False
        
        self.setWin(table_name)

        self.setImage(table_name)

        self.ui.yesbutt.clicked.connect(self.confirm)
        self.ui.nobutt.clicked.connect(self.reject)

        self.playsound()


    def setWin (self, table_name):
        if table_name == "stafftb":
                self.setWindowIcon(QIcon("Pictures/Staff.png"))
                self.setWindowTitle("Delete Staff?")

        elif table_name == "clientb":
                self.setWindowIcon(QIcon("Pictures/Client.png"))
                self.setWindowTitle("Delete Client?")

        elif table_name == "patienttb":
                self.setWindowIcon(QIcon("Pictures/Patient.png"))
                self.setWindowTitle("Delete Patient?")

        elif table_name == "inventorytb":
                self.setWindowIcon(QIcon("Pictures/Inventory.png"))
                self.setWindowTitle("Delete Inventory?")

        elif table_name == "suppliertb":
                self.setWindowIcon(QIcon("Pictures/Supplier.png"))
                self.setWindowTitle("Delete supplier?")

        else:
                self.setWindowIcon(QIcon("Pictures/logowin.png"))
                self.setWindowTitle("Delete?")

    def playsound(self):
        self.sound = QSoundEffect()
        self.sound.setSource(QUrl.fromLocalFile("Sounds/dognotif.wav"))
        self.sound.setVolume(0.6)
        self.sound.play()

    def confirm(self):
        self.skip_dialog = self.ui.checkBox.isChecked()
        self.accept()

    def setImage(self, table_name):
        if table_name == "stafftb":
            self.ui.label_2.setPixmap(QPixmap("Pictures/Staff.png"))
            self.ui.label.setText("Are you sure you want to delete this staff? ૮₍˶ ╥ ‸ ╥ ⑅₎ა\nYou'll have to say bye-bye to them forever!")

        elif table_name == "clientb":
            self.ui.label_2.setPixmap(QPixmap("Pictures/Client.png"))
            self.ui.label.setText("Are you sure you want to delete this client? ₍⸝⸝⸝ ᵕ ﻌ ᵕ⸝⸝⸝₎ \n Their furry friends might miss them!")

        elif table_name == "patienttb":
            self.ui.label_2.setPixmap(QPixmap("Pictures/Patient.png"))
            self.ui.label.setText("Are you sure you want to delete this patient? ૮₍｡ • ﻌ •｡₎ა \n That's one less tail to wag...")
        
        elif table_name == "inventorytb":
            self.ui.label_2.setPixmap(QPixmap("Pictures/Inventory.png"))
            self.ui.label.setText("Are you sure you want to delete this inventory item?ฅ/ᐠᓀ ﻌ ᓂマ \n It'll be gone like it never existed!")
        
        elif table_name == "suppliertb":
            self.ui.label_2.setPixmap(QPixmap("Pictures/Supplier.png"))
            self.ui.label.setText("Are you sure you want to delete this supplier? ( •̥́ ˍ •̀ू ) \n No more deliveries from them...")