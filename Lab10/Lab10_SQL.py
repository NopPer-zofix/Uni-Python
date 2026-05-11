# Import modules and classes
import sys
# Import QT core modules
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
# Import class
from MyWindow10 import Ui_MainWindow
import MySQLdb as mdb

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.db = None

        self.setupUi(self)
        self.show()
        self.ButtonExit.clicked.connect(self.close_UI)
        self.ButtonConnect.clicked.connect(self.DB_Connect)
        self.ButtonFetch.clicked.connect(self.Fetch)
        self.ButtonInsert.clicked.connect(self.Insert)

    # Exit Menu Item
    def close_UI(self):
        self.close()

    def DB_Connect(self):
        try:
            # todo use the right command to connect to the MySql chinook database
            # todo remember to update your password with the one you used at the MySql chinook database creation
            QMessageBox.about(self, "Connect", "Database connected successfully")

        except mdb.error as e:
            QMessageBox.about(self, "Connect", "Failed to connect to db")
            sys.exit(1)

    def Fetch(self):
        # todo fetch a list with the surnames of the employees using the MySql command:
        # "SELECT LastName FROM EMPLOYEE"

        _translate = QtCore.QCoreApplication.translate

        # TODO parse the retrieved list and update the list in the UI

    def Insert(self):
        nothing = None
        # todo insert your name into the employees table using the MySql command:
        # "INSERT INTO chinook.employee (EmployeeId, LastName, FirstName) VALUES (10000, 'MySurname', 'MyName')"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Create a Qt widget, which will be our window.
    window = MainWindow()
    # Start the event loop.
    app.exec_()