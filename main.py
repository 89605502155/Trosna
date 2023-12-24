from layout_colorwidget import Color
from models_and_their_params import models_and_their_params
from calculate_risk import calculate_risk
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
        new_model=models_and_their_params(model=select_model)
        empty_dict=new_model.get_empty_model()
        if select_model=='третья' or select_model=='четвёртая' or select_model=='пятая':
            self.get_numbers_to_input(len(empty_dict.keys()),list(empty_dict.keys()),select_model,empty_dict)

    def get_numbers_to_input(self,count,model_name_list,select_model,empty_dict):
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
            button_box.accepted.connect(lambda: self.generate_float_list(dialog,inputs,
                                                                         select_model,
                                                                         empty_dict,model_name_list))
            button_box.rejected.connect(dialog.reject)

            layout.addWidget(button_box)
            dialog.setLayout(layout)
            dialog.exec()

    def generate_float_list(self,dialog,inputs,select_model,empty_dict,model_name_list):
        column_count = self.table.columnCount()
        num=[]
        print("empty_dict",empty_dict)
        for i in inputs:
            try:
                num.append(float(i.text()))
            except ValueError:
                num.append(0.0)
        for i in range(len(num)):
            empty_dict[model_name_list[i]]=num[i]
        self.all_data_dict[column_count] = empty_dict
        print(self.all_data_dict)
        dialog.accept()
        model = calculate_risk()
        response=model.main(variant=select_model,params=empty_dict)
        print(response)
        self.add_column(response)


    def add_column(self,response):
        column_count = self.table.columnCount()
        self.table.setColumnCount(column_count + 1)
        new_column_name = f'Участок {column_count}'
        self.table.setHorizontalHeaderItem(column_count, QTableWidgetItem(new_column_name))

        print("ffff",self.selected_string)
        print(response)
        for row, (key, value) in enumerate(response.items()):
            if value > 100:
                self.table.setItem(row, column_count, QTableWidgetItem(f'{key}: {value:,.2f}'))
            elif value >= 0.01:
                self.table.setItem(row, column_count, QTableWidgetItem(f'{key}: {value:,.4f}'))
            else:
                self.table.setItem(row, column_count, QTableWidgetItem(f'{key}: {value:,.4e}'))
            # self.table.setItem(row, column_count, QTableWidgetItem(f'{key}: {value:,.7f}'))
        self.table.resizeColumnsToContents()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()