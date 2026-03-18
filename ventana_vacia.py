import sys
from PyQt6.QtWidgets import QApplication, QWidget

class ventanavacia(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializarUI()
    
    def inicializarUI(self):
        self.setGeometry(100,100,250,250)
        self.setWindowTitle("Calculadora")
        self.show()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    ventana=ventanavacia()
    sys.exit(app.exec())