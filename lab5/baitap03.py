import sys
from PySide6.QtWidgets import QApplication, QWidget, QSlider, QHBoxLayout, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor

class BurningWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Burning Widget")

        # Create QSlider and set properties
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(75)
        self.slider.setMaximum(675)
        self.slider.setValue(300)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(75)
        self.slider.setSingleStep(1)

        # Customize QSlider appearance (keep your original CSS code)
        self.slider.setStyleSheet("""
            ... (Your CSS code here) ...
        """)

        # Create QLabel for value display and set initial text
        self.value_label = QLabel(str(self.slider.value()))
        self.value_label.setAlignment(Qt.AlignCenter)

        # Connect slider's valueChanged signal to update label function
        self.slider.valueChanged.connect(self.update_value_label)

        # Create layout and add slider and label
        layout = QHBoxLayout()
        layout.addWidget(self.slider)
        layout.addWidget(self.value_label)  # Add QLabel to layout
        self.setLayout(layout)

    def update_value_label(self, value):
        # Update label content when slider value changes
        self.value_label.setText(str(value))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BurningWidget()
    window.show()
    sys.exit(app.exec_())
