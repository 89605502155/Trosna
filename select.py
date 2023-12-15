from PySide6.QtWidgets import (QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QVBoxLayout,
                               QWidget, QDialog, QLabel, QLineEdit, QDialogButtonBox, QVBoxLayout,
                               )

class TableExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Таблица с PySide6")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Колонка 1', 'Колонка 2', 'Колонка 3'])

        self.layout.addWidget(self.table)

        self.add_column_button = QPushButton("Добавить колонку")
        self.add_column_button.clicked.connect(self.get_numbers_to_input)
        self.layout.addWidget(self.add_column_button)


    def get_numbers_to_input(self):
        try:
            count = 3
        except ValueError:
            return

        if count > 0:
            dialog = QDialog(self)
            dialog.setWindowTitle("Введите числа")

            layout = QVBoxLayout()
            self.inputs = []

            for i in range(count):
                label = QLabel(f"Число {i + 1}:")
                input_line = QLineEdit()
                layout.addWidget(label)
                layout.addWidget(input_line)
                self.inputs.append(input_line)

            button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
            button_box.accepted.connect(lambda: self.add_column_with_numbers(dialog))
            button_box.rejected.connect(dialog.reject)

            layout.addWidget(button_box)
            dialog.setLayout(layout)
            dialog.exec()

    def add_column_with_numbers(self, dialog):
        numbers_list = [input_line.text().strip() for input_line in self.inputs]

        column_count = self.table.columnCount()
        self.table.setColumnCount(column_count + 1)
        new_column_name = f'Колонка {column_count + 1}'
        self.table.setHorizontalHeaderItem(column_count, QTableWidgetItem(new_column_name))

        row_count = max(len(numbers_list), self.table.rowCount())
        self.table.setRowCount(row_count)

        for index, number in enumerate(numbers_list):
            item = QTableWidgetItem(number)
            self.table.setItem(index, column_count, item)

        dialog.accept()

# if __name__ == "__main__":
#     app = QApplication([])
#     window = TableExample()
#     window.show()
#     app.exec()
