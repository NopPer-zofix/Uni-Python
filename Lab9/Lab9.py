# Import modules and classes
import sys
# Import QT core modules
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
# Import class
from MyWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.LabelAnswer.setText("Calculating...")
        self.ButtonPush.clicked.connect(self.calc_result)
        self.ButtonExit.clicked.connect(self.close_UI)

    def calc_result(self):
        # ADD CODE HERE TO CALCULATE THE RESULT
        result = 0
        self.LabelAnswer.setText(str(result))

    # Exit Menu Item
    def close_UI(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # Create a Qt widget, which will be our window.
    window = MainWindow()
    # Start the event loop.
    app.exec_()