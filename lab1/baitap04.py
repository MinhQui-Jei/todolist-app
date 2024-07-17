#MSSV : 2100003619
#Tên : Lê Minh Quí
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QDialog, QLabel
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dialog Box Example")
        self.setGeometry(100, 100, 400, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        dialog_button = QPushButton("Show Dialog")
        layout.addWidget(dialog_button)

        central_widget.setLayout(layout)

        dialog_button.clicked.connect(self.show_dialog)

    def show_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Dialog Box")
        
        label = QLabel("This is a message in the dialog box.")
        dialog_layout = QVBoxLayout()
        dialog_layout.addWidget(label)

        dialog.setLayout(dialog_layout)
        dialog.exec_()

def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
