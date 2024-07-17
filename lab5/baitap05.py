import sys

from PySide6.QtWidgets import (
    QApplication, QDialog, QMainWindow, QPushButton, QLineEdit, QLabel, QVBoxLayout, QFormLayout, QWidget, QHBoxLayout,
    QGraphicsDropShadowEffect
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QFont, QIcon

class CustomDialog(QDialog):

    



    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Custom Dialog")
        self.setStyleSheet("QDialog { background-color: #f5f5f5; border-radius: 10px;}")  # Rounded corners

        # Shadow effect
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setColor(QColor(0, 0, 0, 120))  # Darker shadow
        shadow.setOffset(0, 3)
        self.setGraphicsEffect(shadow)

        name_label = QLabel("Tài Khoản:")
        self.name_edit = QLineEdit()
        age_label = QLabel(" Mật Khẩu:")
        self.age_edit = QLineEdit()

        form_layout = QFormLayout()
        form_layout.setSpacing(15)
        form_layout.addRow(name_label, self.name_edit)
        form_layout.addRow(age_label, self.age_edit)

        cancel_button = QPushButton("Hủy")
        cancel_button.setStyleSheet("background-color: #f44336; color: white; padding: 8px 15px;")
        cancel_button.clicked.connect(self.reject)

        ok_button = QPushButton("OK")
        ok_button.setIcon(QIcon.fromTheme("dialog-ok"))
        ok_button.setStyleSheet("background-color: #4CAF50; color: white; padding: 8px 15px;")
        ok_button.clicked.connect(self.accept)

        button_layout = QHBoxLayout()
        button_layout.addStretch(1)
        button_layout.addWidget(cancel_button)
        button_layout.addWidget(ok_button)

        main_layout = QVBoxLayout()
        main_layout.addLayout(form_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)


class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Dialog")

        

        # Tạo nút có màu và biểu tượng
        modal_button = QPushButton("Đăng Nhập")
        modal_button.setIcon(QIcon.fromTheme("dialog-information"))
        modal_button.setStyleSheet("background-color: #FF9800; color: white;")
        modal_button.clicked.connect(self.show_modal_dialog)
        
        modeless_button = QPushButton("Đăng Ký")
        modeless_button.setIcon(QIcon.fromTheme("dialog-warning"))
        modeless_button.setStyleSheet("background-color: #FF9800; color: white;")
        modeless_button.clicked.connect(self.show_modeless_dialog)

        quit_button = QPushButton("Thoát")
        quit_button.setStyleSheet("background-color: #FF9800; color: white;")
        quit_button.clicked.connect(QApplication.instance().quit)

        layout = QVBoxLayout()
        layout.addWidget(modal_button)
        layout.addWidget(modeless_button)
        layout.addWidget(quit_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


    def show_modal_dialog(self):
        dialog = CustomDialog(self)
        result = dialog.exec()

        if result == QDialog.Accepted:
                name = dialog.name_edit.text()
                age = dialog.age_edit.text()
                print(f"Name: {name}, Age: {age}")

    def show_modeless_dialog(self):
        dialog = CustomDialog(self)
        dialog.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())