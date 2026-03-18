import sys
from PyQt6.QtWidgets import (QApplication,QLabel,QWidget, QLineEdit,QPushButton,QMessageBox,QCheckBox)
from PyQt6.QtGui import (QFont, QPixmap)
from menu_rectangulo_arv import menu_rectangulo
from menu_triangulo_arv import menu_triangulo

class menu_principal(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()
    
    def inicializar_ui(self):
        self.setGeometry(100,100,500,410)
        self.setWindowTitle("Calculadora: Menú principal")
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        self.is_rectanguleado=False

#Crear label y agregarle sus caracteristicas
        text1_label = QLabel(self)
        text1_label.setText("Bienvenido al menú de la calculadora geometrica, ¿Que desea calcular?")
        text1_label.setFont(QFont('Arial',10))
        text1_label.move(35,10)

#Crear botones y colocarle sus caracteristicas
        calcular_rectangulo_button = QPushButton(self)
        calcular_rectangulo_button.setText('Calculo del rectángulo')
        calcular_rectangulo_button.resize(320,24)
        calcular_rectangulo_button.move(90,40)
        calcular_rectangulo_button.clicked.connect(self.abrir_rectangulo)

        calcular_triangulo_button = QPushButton(self)
        calcular_triangulo_button.setText('Calculo del triángulo')
        calcular_triangulo_button.resize(320,24)
        calcular_triangulo_button.move(90,70)
        calcular_triangulo_button.clicked.connect(self.abrir_triangulo)

        calcular_circulo_button = QPushButton(self)
        calcular_circulo_button.setText('Calculo del círculo')
        calcular_circulo_button.resize(320,24)
        calcular_circulo_button.move(90,100)
        calcular_circulo_button.clicked.connect(self.abrir_circulo)

        calcular_trapecio_button = QPushButton(self)
        calcular_trapecio_button.setText('Calculo del trapecio')
        calcular_trapecio_button.resize(320,24)
        calcular_trapecio_button.move(90,130)
        calcular_trapecio_button.clicked.connect(self.abrir_trapecio)

        calcular_cubo_button = QPushButton(self)
        calcular_cubo_button.setText('Calculo del cubo')
        calcular_cubo_button.resize(320,24)
        calcular_cubo_button.move(90,160)
        calcular_cubo_button.clicked.connect(self.abrir_cubo)

        calcular_prisma_button = QPushButton(self)
        calcular_prisma_button.setText('Calculo del prisma rectangular')
        calcular_prisma_button.resize(320,24)
        calcular_prisma_button.move(90,190)
        calcular_prisma_button.clicked.connect(self.abrir_prisma)     

        calcular_cilindro_button = QPushButton(self)
        calcular_cilindro_button.setText('Calculo del cilindro')
        calcular_cilindro_button.resize(320,24)
        calcular_cilindro_button.move(90,220)
        calcular_cilindro_button.clicked.connect(self.abrir_cilindro)

        calcular_cono_button = QPushButton(self)
        calcular_cono_button.setText('Calculo del cono')
        calcular_cono_button.resize(320,24)
        calcular_cono_button.move(90,250)
        calcular_cono_button.clicked.connect(self.abrir_cono)

        calcular_esfera_button = QPushButton(self)
        calcular_esfera_button.setText('Calculo de la esfera')
        calcular_esfera_button.resize(320,24)
        calcular_esfera_button.move(90,280)
        calcular_esfera_button.clicked.connect(self.abrir_esfera) 

        calcular_triangulo_rectangulo_button = QPushButton(self)
        calcular_triangulo_rectangulo_button.setText('Calculo del triangulo rectangulo')
        calcular_triangulo_rectangulo_button.resize(320,24)
        calcular_triangulo_rectangulo_button.move(90,310)
        calcular_triangulo_rectangulo_button.clicked.connect(self.abrir_triangulo_rectangulo)   

        salir_button = QPushButton(self)
        salir_button.setText('Salir')
        salir_button.resize(120,24)
        salir_button.move(20,360)
        salir_button.clicked.connect(self.iniciar_salir)

    def abrir_rectangulo(self):
        self.hide()
        self.abrir_rectangulo_form = menu_rectangulo()
        self.abrir_rectangulo_form.show()
    
    def abrir_triangulo(self):
        self.hide()
        self.abrir_triangulo_form = menu_triangulo()
        self.abrir_triangulo_form.show()
        

    def abrir_circulo(self):
        pass

    def abrir_trapecio(self):
        pass

    def abrir_cubo(self):
        pass

    def abrir_prisma(self):
        pass

    def abrir_cilindro(self):
        pass

    def abrir_cono(self):
        pass

    def abrir_esfera(self):
        pass

    def abrir_triangulo_rectangulo(self):
        pass


    def iniciar_salir(self):
        pass


if __name__=='__main__':
    app= QApplication(sys.argv)
    menu = menu_principal()
    sys.exit(app.exec())