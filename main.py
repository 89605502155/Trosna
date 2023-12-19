from layout_colorwidget import Color
from PySide6.QtWidgets import (
QApplication,
QMainWindow,
QLabel,
QLineEdit,
QVBoxLayout,
QWidget,
QSpinBox,
QDial,
QVBoxLayout,
QHBoxLayout,
QGridLayout,
QPushButton,
QStackedLayout,
QDialog,
QInputDialog,
QTableWidget,
QTableWidgetItem,
QDialogButtonBox,
)
#Пронина Ирина Анатольевна
from PySide6.QtCore import Qt
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.selected_string = {}
        self.setWindowTitle("Trosna")
        self.setGeometry(100, 100, 600, 400)
        self.all_data_dict={}
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.table = QTableWidget()
        self.table.setColumnCount(1)
        self.table.setRowCount(3)
        self.table.setHorizontalHeaderLabels(['Итог'])

        self.layout.addWidget(self.table)

        self.add_column_button = QPushButton("Добавить участок")
        self.add_column_button.clicked.connect(self.get_a_str_from_a_list)
        # self.add_column_button.clicked.connect(self.select_params)
        # self.add_column_button.clicked.connect(self.add_column)
        self.layout.addWidget(self.add_column_button)

    def get_a_str_from_a_list(self):
        title = "Select a string"
        label = "Выбери модель для обсчёта участка"
        items = ["первая", "вторая", "третья", "четвёртая","пятая"]
        initial_selection = 2  # orange, indexed from 0
        my_selected_str, ok = QInputDialog.getItem(
            self,
            title,
            label,
            items,
            current=initial_selection,
            editable=False,
        )

        if ok:
            column_count = self.table.columnCount()
            self.selected_string[column_count] = my_selected_str
            self.select_params(my_selected_str)

    def select_params(self,select_model):
        dialog = QDialog(self)
        dialog.setWindowTitle("Введите числа")
        layout = QVBoxLayout()
        third_model = {
            "Concentration": 0,
            "SF": 0,
            "Time": 0,
            "weight": 0,
            "consumption": 0,
            "population": 0
        }
        if select_model=='третья':
            self.get_numbers_to_input(len(third_model.keys()),list(third_model.keys()),select_model)

    def get_numbers_to_input(self,count,model_name_list,select_model):
        if count > 0:
            dialog = QDialog(self)
            dialog.setWindowTitle("Введите числа")
            print(model_name_list)
            layout = QVBoxLayout()
            inputs = []

            for i in range(count):
                label = QLabel(model_name_list[i])
                input_line = QLineEdit()
                layout.addWidget(label)
                layout.addWidget(input_line)
                inputs.append(input_line)
            button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
            button_box.accepted.connect(lambda: self.generate_float_list(dialog,inputs,select_model))
            button_box.rejected.connect(dialog.reject)

            layout.addWidget(button_box)
            dialog.setLayout(layout)
            dialog.exec()

    def generate_float_list(self,dialog,inputs,select_model):
        column_count = self.table.columnCount()
        num=[]
        for i in inputs:
            try:
                num.append(float(i.text()))
            except ValueError:
                num.append(0.0)
        self.all_data_dict[column_count] = num
        print(self.all_data_dict)
        dialog.accept()

    def add_column(self):
        column_count = self.table.columnCount()
        self.table.setColumnCount(column_count + 1)
        new_column_name = f'Участок {column_count}'
        self.table.setHorizontalHeaderItem(column_count, QTableWidgetItem(new_column_name))

        print(self.selected_string)

        for row in range(self.table.rowCount()):
            self.table.setItem(row, column_count, QTableWidgetItem(""))




if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()