#Lê Minh Quí
#MSSV : 2100003619

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit
from PyQt5.QtCore import Qt

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        # Set the window properties (title and initial size)
        self.setWindowTitle("Máy Tính Của Mqui")
        self.setGeometry(100, 100, 400, 400) # (x, y, width, height)

        # Create a central widget for the main window
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create a QLineEdit widget for input and result display
        self.input_display = QLineEdit()
        self.input_display.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.input_display.setReadOnly(True)

        # Create a layout for buttons
        button_layout = QVBoxLayout()


        number_buttons_layout = QVBoxLayout()

        # Tạo các nút số từ 1 đến 9
        for i in range(1, 10):
            number_button = QPushButton(str(i))
            number_button.clicked.connect(lambda checked, ch=i: self.on_number_button_click(ch))
            number_buttons_layout.addWidget(number_button)

# Tạo các nút đặc biệt (0, ., =)
        zero_button = QPushButton("0")
        zero_button.clicked.connect(lambda: self.on_number_button_click(0))

        dot_button = QPushButton(".")
        dot_button.clicked.connect(self.on_dot_button_click)

        equals_button = QPushButton("=")
        equals_button.clicked.connect(self.calculate_result)

# Tạo các nút phép toán (+, -, *, /)

        operator_buttons_layout = QVBoxLayout()
        operators = ["+", "-", "*", "/"]
        for operator in operators:
            operator_button = QPushButton(operator)
            operator_button.clicked.connect(lambda checked, ch=operator: self.on_operator_button_click(ch))
            operator_buttons_layout.addWidget(operator_button)
        # Tạo layout cho các nút số và nút đặc biệt
            number_special_buttons_layout = QHBoxLayout()
            number_special_buttons_layout.addLayout(number_buttons_layout)
            number_special_buttons_layout.addWidget(zero_button)
            number_special_buttons_layout.addWidget(dot_button)
            number_special_buttons_layout.addWidget(equals_button)

            # Tạo layout cho tất cả các nút
            button_layout.addLayout(number_special_buttons_layout)
            button_layout.addLayout(operator_buttons_layout)

            # Tạo layout dọc cho toàn bộ máy tính
            main_layout = QVBoxLayout()
            main_layout.addWidget(self.input_display)
            main_layout.addLayout(button_layout)

            # Thiết lập layout cho widget trung tâm
            central_widget.setLayout(main_layout)

            # Khởi tạo biểu thức nhập vào
            self.input_expression = ""
            
    # Thêm chữ số được nhấn vào biểu thức nhập
    def on_number_button_click(self, digit):
        self.input_expression += str(digit)
        self.update_input_display()

    def on_dot_button_click(self):
        # Thêm dấu chấm thập phân vào biểu thức nhập
        if "." not in self.input_expression:
            self.input_expression += "."
            self.update_input_display()

    def on_operator_button_click(self, operator):
        # Thêm toán tử được nhấn vào biểu thức nhập
        if self.input_expression and self.input_expression[-1] != operator:
            self.input_expression += operator
            self.update_input_display()

    def calculate_result(self):
        try:
            # Tính toán kết quả của biểu thức nhập
            result = eval(self.input_expression)
            self.input_expression = str(result)
            self.update_input_display()
        except Exception as e:
                self.input_expression = "Error"
                self.update_input_display()
    def update_input_display(self):
    # Hiển thị biểu thức nhập hiện tại trong trường nhập
            self.input_display.setText(self.input_expression)

def main():
    # Tạo một ứng dụng PyQt
    app = QApplication(sys.argv)
    # Tạo một thể hiện của lớp CalculatorApp
    window = CalculatorApp()
    # Hiển thị cửa sổ
    window.show()
    # Chạy vòng lặp sự kiện của ứng dụng
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


