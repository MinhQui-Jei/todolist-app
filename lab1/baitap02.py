#MSSV : 2100003619
#Tên : Lê Minh Quí
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class TextDisplayApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text Display Application")
        self.setGeometry(100, 100, 400, 200)  # (x, y, width, height)

        # Create a central widget for the main window
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Create widgets (QLineEdit, QPushButton, and QLabel)
        self.text_edit = QLineEdit()
        self.display_button = QPushButton("Click here to display Text")
        self.result_label = QLabel("")

        # Create a vertical layout
        layout = QVBoxLayout()

        layout.addWidget(self.text_edit)
        layout.addWidget(self.display_button)
        layout.addWidget(self.result_label)

        central_widget.setLayout(layout)

        # Connect the button click to the function that updates the label
        self.display_button.clicked.connect(self.display_text)

    def display_text(self):

        entered_text = self.text_edit.text()
        self.result_label.setText(f"Input Text: {entered_text}")

def main():
    app = QApplication(sys.argv)
    window = TextDisplayApp()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()
