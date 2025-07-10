from PyQt5 import QtWidgets, QtGui
from PyQt5.QtGui import QIcon
import sys
from HPACIS import HPAC_ui
import globalsession




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    app.setWindowIcon(QIcon("Pictures/logowin.png"))

    MainWindow = QtWidgets.QMainWindow() 
    ui = HPAC_ui()
    ui.setupUi(MainWindow)
    
    MainWindow.show()
    sys.exit(app.exec_())