from PySide6.QtWidgets import (
QApplication,
QLabel,
QMainWindow,
QPushButton,
QVBoxLayout,
QWidget,
)
from main import MainWindow
class InputParams(QWidget):
    def __init__(self):
        super().__init__()

        self.button = QPushButton("Push for Window")
        self.button.clicked.connect(self.show_new_window)
        self.setCentralWidget(self.button)

    def show_new_window(self, checked):
        w = MainWindow()
        w.show()