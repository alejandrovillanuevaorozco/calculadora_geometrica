import sys
from PyQt6.QtWidgets import (QApplication,QLabel,QWidget, QLineEdit,QPushButton,QMessageBox,QCheckBox)
from PyQt6.QtGui import (QFont, QPixmap, QDoubleValidator)
from resultado_perimetro_rectangulo import calcular_rectangulo_view

class Perimetro(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()
    
    def inicializar_ui(self):
        self.setGeometry(100,100,350,250)
        self.setWindowTitle("Calculo del perimetro del rectangulo")
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        self.is_rectanguleado=False

#Crear label y agregarle sus caracteristicas
        largo_label = QLabel(self)
        largo_label.setText("Largo del rectangulo:")
        largo_label.setFont(QFont('Arial',10))
        largo_label.move(20,54)

#Crear el input del label anterior
        self.largo_input=QLineEdit(self)
        self.largo_input.resize(50,24)
        self.largo_input.move(145,50)
        self.largo_input.setValidator(QDoubleValidator(0, 9999, 2))

        ancho_label = QLabel(self)
        ancho_label.setText("Ancho del rectangulo:")
        ancho_label.setFont(QFont('Arial',10))
        ancho_label.move(20,86)

        self.ancho_input=QLineEdit(self)
        self.ancho_input.resize(50,24)
        self.ancho_input.move(145,82)
        self.ancho_input.setValidator(QDoubleValidator(0, 9999, 2))

#Crear botones y colocarle sus caracteristicas
        calcular_button = QPushButton(self)
        calcular_button.setText('Calcular')
        calcular_button.resize(220,24)
        calcular_button.move(65,140)
        calcular_button.clicked.connect(self.calcular_perimetro_rectangulo)

        menu_principal_button = QPushButton(self)
        menu_principal_button.setText('Menú principal')
        menu_principal_button.resize(120,24)
        menu_principal_button.move(210,200)
        menu_principal_button.clicked.connect(self.volver_main)

        atras_button = QPushButton(self)
        atras_button.setText('Atras')
        atras_button.resize(120,24)
        atras_button.move(20,200)
        atras_button.clicked.connect(self.volver_atras)

    def calcular_perimetro_rectangulo(self):

        if not self.largo_input.text().strip() or not self.ancho_input.text().strip():
            QMessageBox.warning(self, "Error", "¡Llena todos los campos!")# ← Validar que no sea vacio
            return
        self.largo = float(self.largo_input.text())   # ← Guarda en self.largo
        self.ancho = float(self.ancho_input.text())   # ← Guarda en self.ancho
        if self.largo > 0 and self.ancho > 0:
            perimetro = 2 * (self.largo + self.ancho)
            area = self.largo * self.ancho
            QMessageBox.information(self, 
            "✅ Resultados", 
            f"Largo: {self.largo}\nAncho: {self.ancho}\nPerímetro: {perimetro:.2f}")
        else:
            QMessageBox.warning(self, "Error", "Largo y ancho deben ser > 0")


    def volver_main(self):
        from main import menu_principal
        self.hide()
        self.abrir_main_form = menu_principal()
        self.abrir_main_form.show()

    def volver_atras(self):
        from menu_rectangulo_arv import menu_rectangulo
        self.hide()
        self.abrir_main_form = menu_rectangulo()
        self.abrir_main_form.show()


        




if __name__=='__main__':
    app= QApplication(sys.argv)
    peri = Perimetro()
    sys.exit(app.exec())