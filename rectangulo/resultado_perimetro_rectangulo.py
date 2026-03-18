from PyQt6.QtWidgets import (QDialog,QLabel, QLineEdit,QPushButton,QMessageBox)
from PyQt6.QtGui import (QFont, QPixmap)


class calcular_rectangulo_view(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)
        self.generar_formulario()
    
    def generar_formulario(self):
        self.setGeometry(100,100,350,250)
        self.setWindowTitle("Resultado: ")

#Crear label y agregarle sus caracteristicas
        largo_label = QLabel(self)
        largo_label.setText("Largo del rectangulo: ")
        largo_label.setFont(QFont('Arial',10))
        largo_label.move(20,54)

        ancho_label = QLabel(self)
        ancho_label.setText("Ancho del rectangulo: ")
        ancho_label.setFont(QFont('Arial',10))
        ancho_label.move(20,86)