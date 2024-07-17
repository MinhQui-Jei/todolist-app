import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QFont, QPixmap

class TodayDateWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Ngày Hôm Nay')

        layout = QVBoxLayout()

        # Hiển thị ngày
        self.date_label = QLabel(self)
        self.date_label.setAlignment(Qt.AlignCenter)
        self.date_label.setFont(QFont('Arial', 20))

        # Hiển thị biểu tượng (icon)
        self.icon_label = QLabel(self)
        icon_pixmap = QPixmap('f2.png')  # Thay đổi đường dẫn đến biểu tượng của bạn
        self.icon_label.setPixmap(icon_pixmap)
        self.icon_label.setAlignment(Qt.AlignCenter)

        # Nút thoát
        self.exit_button = QPushButton('Thoát', self)
        self.exit_button.clicked.connect(self.close)

        layout.addWidget(self.date_label)
        layout.addWidget(self.icon_label)
        layout.addWidget(self.exit_button)
        self.setLayout(layout)

        self.showTodayDate()

    def showTodayDate(self):
        # Hiển thị ngày hôm nay
        today_date = QDate.currentDate()
        self.date_label.setText(today_date.toString('dddd - dd/MM/yyyy'))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = TodayDateWidget()
    sys.exit(app.exec_())