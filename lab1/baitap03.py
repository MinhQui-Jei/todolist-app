#MSSV : 2100003619
#Tên : Lê Minh Quí
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QWidget, QColorDialog, QFontDialog
import sys

class WidgetPropertiesApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Widget Properties")
        self.setGeometry(100, 100, 400, 200)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()
        self.button = QPushButton("Click to Customize!")
        layout.addWidget(self.button)

        central_widget.setLayout(layout)

        self.button.clicked.connect(self.customize_color)
        self.button.clicked.connect(self.customize_font)

    def customize_color(self):
        color_dialog = QColorDialog.getColor()
        if color_dialog.isValid():
            self.button.setStyleSheet(f"background-color: {color_dialog.name()};")

    def customize_font(self):
        font_dialog, ok = QFontDialog.getFont()
        if ok:
            self.button.setFont(font_dialog)

def main():
    app = QApplication(sys.argv)
    window = WidgetPropertiesApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
