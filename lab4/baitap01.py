import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
from PyQt5.QtCore import Qt, QEvent

class MouseEventsApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mouse Events Example")
        self.setGeometry(100, 100, 400, 200)
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.mouse_label = QLabel("Mouse Events:", self.central_widget)
        self.mouse_label.setGeometry(10, 10, 300, 30)

        # Cài đặt bộ lọc sự kiện để bắt các sự kiện chuột
        self.installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == QEvent.MouseMove:
            x = event.x()
            y = event.y()
            # Cập nhật nhãn theo dõi với vị trí chuột hiện tại
            self.mouse_tracker_label.setText(f"Mouse moved to ({x}, {y})")
        elif event.type() == QEvent.MouseButtonPress:
            button=""
            if event.button() == Qt.LeftButton:
                button = "Left"
            elif event.button() == Qt.RightButton:
                button = "Right"
            elif event.button() == Qt.MiddleButton:
                button = "Middle"

            self.mouse_event_label.setText(f"{button} button clicked")
        return super().eventFilter(obj, event)

def main():
    app = QApplication(sys.argv)
    window = MouseEventsApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()