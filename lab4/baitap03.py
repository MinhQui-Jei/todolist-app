import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QTime, QTimer, Qt
from PyQt5.QtGui import QFont,QPainter ,QColor


class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 100)
        self.setWindowTitle("Đồng Hồ Số")

        self.timer =QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)

        self.current_time = QTime.currentTime()
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Cấu hình font và màu sắc cho hiển thị đồng hồ số
        font = QFont('Arial', 30, QFont.Bold)
        painter.setFont(font)
        painter.setPen(QColor(0, 120, 100))  # Màu đen

        # Định dạng và hiển thị thời gian hiện tại
        time_str = self.current_time.toString('hh:mm:ss')
        painter.drawText(event.rect(), Qt.AlignCenter, time_str)

    def updateTime(self):
        # Cập nhật hiển thị văn bản của widget thời gian hiện tại
        self.current_time = QTime.currentTime()
        self.update()

def main():
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()