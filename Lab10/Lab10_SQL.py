<<<<<<< HEAD
# Import modules and classes
import sys
# Import QT core modules
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
# Import class
from MyWindow10 import Ui_MainWindow
=======
# =================================================================
# Registration Number: 24403
# Name: Artem Kondratenko
# =================================================================

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from MyWindow import Ui_MainWindow
>>>>>>> main
import MySQLdb as mdb

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.db = None

        self.setupUi(self)
        self.show()
<<<<<<< HEAD
=======
        
>>>>>>> main
        self.ButtonExit.clicked.connect(self.close_UI)
        self.ButtonConnect.clicked.connect(self.DB_Connect)
        self.ButtonFetch.clicked.connect(self.Fetch)
        self.ButtonInsert.clicked.connect(self.Insert)

<<<<<<< HEAD
    # Exit Menu Item
=======
>>>>>>> main
    def close_UI(self):
        self.close()

    def DB_Connect(self):
        try:
<<<<<<< HEAD
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
=======
            self.db = mdb.connect(
                host="localhost",
                user="root",
                passwd="",
                db="Lab10"
            )
            QMessageBox.information(self, "Connect", "Database connected successfully")

        except mdb.Error as e:
            QMessageBox.critical(self, "Connect", f"Failed to connect to db:\n{e}")
            sys.exit(1)

    def Fetch(self):
        if self.db is None:
            QMessageBox.warning(self, "Warning", "Please connect to the database first.")
            return

        try:
            cursor = self.db.cursor()
            
            cursor.execute("SELECT LastName FROM EMPLOYEE")
            
            rows = cursor.fetchall()

            self.listWidget.clear()

            for row in rows:
                surname = row[0]
                self.listWidget.addItem(surname)

            cursor.close()

        except mdb.Error as e:
            QMessageBox.critical(self, "Database Error", f"Failed to fetch records:\n{e}")

    def Insert(self):
        if self.db is None:
            QMessageBox.warning(self, "Warning", "Please connect to the database first.")
            return

        try:
            cursor = self.db.cursor()
            
            query = "INSERT INTO Lab10.EMPLOYEE (EmployeeId, LastName, FirstName) VALUES (10000, 'Kondratenko', 'Artem')"
            
            cursor.execute(query)
            
            self.db.commit()
            
            QMessageBox.information(self, "Success", "Record inserted successfully!\nClick 'Fetch' to see the update.")
            cursor.close()

        except mdb.Error as e:
            self.db.rollback()
            QMessageBox.critical(self, "Database Error", f"Insertion failed:\n{e}")
>>>>>>> main


if __name__ == "__main__":
    app = QApplication(sys.argv)
<<<<<<< HEAD
    # Create a Qt widget, which will be our window.
    window = MainWindow()
    # Start the event loop.
=======
    window = MainWindow()
>>>>>>> main
    app.exec_()