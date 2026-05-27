# =================================================================
# Registration Number: 24403
# Name: Artem Kondratenko
# =================================================================

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox

from MyWindow import Ui_MainWindow
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

    def close_UI(self):
        self.close()

    def DB_Connect(self):
        try:
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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec_()