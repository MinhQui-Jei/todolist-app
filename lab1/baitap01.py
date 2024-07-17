#MSSV : 2100003619
#Tên : Lê Minh Quí
import sys
from PyQt5.QtWidgets import QApplication , QMainWindow 

def main():

    app = QApplication(sys.argv)
    main_window = QMainWindow()

    main_window.setWindowTitle("Blank Window using QyQt")
    main_window.setGeometry(100,100,400,300)

    main_window.show()

    sys.exit(app.exec_())
if __name__=="__main__":
    main()
