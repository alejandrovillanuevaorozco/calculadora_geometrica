import sys
from PyQt6.QtWidgets import (QApplication,QLabel,QWidget, QLineEdit,QPushButton,QMessageBox,QCheckBox)
from PyQt6.QtGui import (QFont, QPixmap)
from calculo_perimetro_rectangulo import Perimetro
from calculo_area_rectangulo import area


class menu_rectangulo(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()
    
    def inicializar_ui(self):
        self.setGeometry(100,100,350,180)
        self.setWindowTitle("Menú del rectangulo")
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        self.is_rectanguleado=False

#Crear label y agregarle sus caracteristicas
        text1_label = QLabel(self)
        text1_label.setText("Bienvenido al menú del rectangulo, ¿Que desea calcular?")
        text1_label.setFont(QFont('Arial',10))
        text1_label.move(10,10)

#Crear botones y colocarle sus caracteristicas
        calcular_perimetro_button = QPushButton(self)
        calcular_perimetro_button.setText('Calculo del perímetro')
        calcular_perimetro_button.resize(320,24)
        calcular_perimetro_button.move(20,40)
        calcular_perimetro_button.clicked.connect(self.abrir_perimetro)

        calcular_area_button = QPushButton(self)
        calcular_area_button.setText('Calculo del área')
        calcular_area_button.resize(320,24)
        calcular_area_button.move(20,70)
        calcular_area_button.clicked.connect(self.abrir_area)

        atras_button = QPushButton(self)
        atras_button.setText('Atras')
        atras_button.resize(120,24)
        atras_button.move(20,130)
        atras_button.clicked.connect(self.volver_main)

    def abrir_perimetro(self):
        self.abrir_perimetro_form = Perimetro()
        self.abrir_perimetro_form.show()
    
    def abrir_area(self):
        self.abrir_area_form = area()
        self.abrir_area_form.show()

    def volver_main(self):
        from main import menu_principal
        self.hide()
        self.abrir_main_form = menu_principal()
        self.abrir_main_form.show()


if __name__=='__main__':
    app= QApplication(sys.argv)
    menu = menu_rectangulo()
    sys.exit(app.exec())