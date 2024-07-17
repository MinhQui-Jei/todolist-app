import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView, QGraphicsScene, QGraphicsTextItem, QInputDialog
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

class ImageViewerApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Viewer with Annotations")
        self.setGeometry(100, 100, 500, 400)
        self.initUI()
        
        self.view.mousePressEvent = self.mousePressEventCustom

    def initUI(self):
        self.scene = QGraphicsScene()
        self.view = QGraphicsView(self.scene)
        self.view.setSceneRect(-120, -120, 800, 800)
        self.setCentralWidget(self.view)

        self.image = QPixmap("cat.png")  # Load your image here
        self.scene.addPixmap(self.image)

        self.annotation_mode = False

    def drawAnnotation(self, pos, text):
        if self.annotation_mode:
            text_item = QGraphicsTextItem(text)
            text_item.setDefaultTextColor(Qt.red)
            text_item.setFont(QFont("Arial", 12))
            text_item.setPos(pos)
            self.scene.addItem(text_item)

    def mousePressEventCustom(self, event):
        if event.button() == Qt.LeftButton:
            annotation_text, ok = QInputDialog.getText(self, "Annotation", "Input text:")
            if ok and annotation_text:
                self.annotation_mode = True
                self.annotation_text = annotation_text
                self.annotation_start = event.pos()
                
                self.drawAnnotation(event.pos(), self.annotation_text)

def main():
    app = QApplication(sys.argv)
    window = ImageViewerApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()