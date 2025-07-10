from PyQt5.QtWidgets import QDialog
from Warning.duplicate import Ui_Dialog
from PyQt5.QtGui import QPixmap, QIcon



class DupCon(QDialog):
    def __init__(self, full_name, existing_id, table_name, owner=""):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.setWin (full_name, owner, existing_id, table_name)

        self.ui.yesbutt.clicked.connect(self.accept)
        self.ui.nobutt.clicked.connect(self.reject)

    
    def setWin (self, full_name, owner, existing_id, table_name):

        if table_name == "stafftb":
                self.setWindowIcon(QIcon("Pictures/Staff.png"))
                self.setWindowTitle("Duplicate Staff?")
                self.ui.label_2.setPixmap(QPixmap("Pictures/Staff.png"))
                self.ui.second.setText(f"{full_name} : {existing_id}")
                self.ui.third.setText("Proceed to add staff entry?")
        
        elif table_name == "clientb":
                self.setWindowIcon(QIcon("Pictures/Client.png"))
                self.setWindowTitle("Duplicate Client?")
                self.ui.label_2.setPixmap(QPixmap("Pictures/Client.png"))
                self.ui.second.setText(f"{full_name} : {existing_id}")
                self.ui.third.setText("Proceed to add client entry?")

        elif table_name == "patienttb":
                self.setWindowIcon(QIcon("Pictures/Patient.png"))
                self.setWindowTitle("Duplicate Patient?")
                self.ui.label_2.setPixmap(QPixmap("Pictures/Patient.png"))
                self.ui.second.setText(f"{full_name}, {owner} : {existing_id}")
                self.ui.third.setText("Proceed to add patient entry?")
        
        elif table_name == "inventorytb":
                self.setWindowIcon(QIcon("Pictures/Inventory.png"))
                self.setWindowTitle("Duplicate Inventory?")
                self.ui.label_2.setPixmap(QPixmap("Pictures/Patient.png"))
                self.ui.second.setText(f"{full_name} : {existing_id}")
                self.ui.third.setText("Proceed to add inventory entry?")
        
        elif table_name == "suppliertb":
                self.setWindowIcon(QIcon("Pictures/Supplier.png"))
                self.setWindowTitle("Duplicate supplier?")
                self.ui.label_2.setPixmap(QPixmap("Pictures/Supplier.png"))
                self.ui.second.setText(f"{full_name} : {existing_id}")
                self.ui.third.setText("Proceed to add supplier entry?")
        else:
                self.setWindowIcon(QIcon("Pictures/logowin.png"))
                self.setWindowTitle("Duplicate?")
                self.ui.label_2.setPixmap(QPixmap("Pictures/logo.png"))
                self.ui.second.setText(f"{full_name} : {existing_id}")
                self.ui.third.setText("Proceed to add entry?")