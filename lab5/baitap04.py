import sys
from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QInputDialog,
    QLineEdit,
    QFormLayout,
    QWidget,
    QMessageBox,
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

class CreativeInputDialogExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chat ")

        # Button with icon
        self.button = QPushButton(QIcon('microphone.png'), "Nhập dữ liệu", self)  
        self.button.clicked.connect(self.showDialog)

        self.line_edit = QLineEdit(self)

        layout = QFormLayout()
        layout.addWidget(self.button)
        layout.addWidget(self.line_edit)
        layout.addWidget(self.line_edit)
        self.setLayout(layout)

    def showDialog(self):
        text, ok = QInputDialog.getText(self, " Nhập vào đây!!", "What ???")
        age, age_ok = QInputDialog.getInt(self, " Nhập tuổi", "Tuổi:", 0, 0, 150)

        if ok and age_ok:
            if text:
                self.line_edit.setText(text)
                QMessageBox.information(self, "Thanks! ", f"Bạn ghi: {text}, {age} tuổi")
            else:
                QMessageBox.warning(self, "hahahah! ", "WTFFFFFFFFF!")
        else:
            QMessageBox.warning(self, "hahahah! ", "WTFFFFFFFFF!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CreativeInputDialogExample()
    ex.show()
    sys.exit(app.exec_())