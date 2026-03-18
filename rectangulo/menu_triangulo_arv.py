import sys
from PyQt6.QtWidgets import (QApplication,QLabel,QWidget, QLineEdit,QPushButton,QMessageBox,QCheckBox)
from PyQt6.QtGui import (QFont, QPixmap)
from calculo_lado_triangulo import lado
from calculo_area_triangulo import area
from calculo_perimetro_triangulo import Perimetro


class menu_triangulo(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()
    
    def inicializar_ui(self):
        self.setGeometry(100,100,350,180)
        self.setWindowTitle("Menú del triangulo")
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        self.is_trianguleado=False

#Crear label y agregarle sus caracteristicas
        text1_label = QLabel(self)
        text1_label.setText("Bienvenido al menú del triangulo, ¿Que desea calcular?")
        text1_label.setFont(QFont('Arial',10))
        text1_label.move(10,10)

#Crear botones y colocarle sus caracteristicas
        calcular_lado_button = QPushButton(self)
        calcular_lado_button.setText('Calculo de un lado')
        calcular_lado_button.resize(320,24)
        calcular_lado_button.move(20,40)
        calcular_lado_button.clicked.connect(self.abrir_lado)

        calcular_perimetro_button = QPushButton(self)
        calcular_perimetro_button.setText('Calculo del perímetro')
        calcular_perimetro_button.resize(320,24)
        calcular_perimetro_button.move(20,70)
        calcular_perimetro_button.clicked.connect(self.abrir_perimetro)

        calcular_area_button = QPushButton(self)
        calcular_area_button.setText('Calculo del área')
        calcular_area_button.resize(320,24)
        calcular_area_button.move(20,100)
        calcular_area_button.clicked.connect(self.abrir_area)

        atras_button = QPushButton(self)
        atras_button.setText('Atras')
        atras_button.resize(120,24)
        atras_button.move(20,130)
        atras_button.clicked.connect(self.volver_main)

    def abrir_lado(self):
        self.abrir_lado_form = lado()
        self.abrir_lado_form.show()    

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
    menu = menu_triangulo()
    sys.exit(app.exec())