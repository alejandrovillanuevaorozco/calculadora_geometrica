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
        self.setWindowTitle("Calculo del perímetro")
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        self.is_rectanguleado=False

#Crear label y agregarle sus caracteristicas
        catetoa_label = QLabel(self)
        catetoa_label.setText("Medida del Cateto A: ")
        catetoa_label.setFont(QFont('Arial',10))
        catetoa_label.move(20,54)

#Crear el input del label anterior
        self.catetoa_input=QLineEdit(self)
        self.catetoa_input.resize(50,24)
        self.catetoa_input.move(145,50)
        self.catetoa_input.setValidator(QDoubleValidator(0, 9999, 2))

        catetob_label = QLabel(self)
        catetob_label.setText("Medida del Cateto B: ")
        catetob_label.setFont(QFont('Arial',10))
        catetob_label.move(20,86)

        self.catetob_input=QLineEdit(self)
        self.catetob_input.resize(50,24)
        self.catetob_input.move(145,82)
        self.catetob_input.setValidator(QDoubleValidator(0, 9999, 2))

#Crear botones y colocarle sus caracteristicas
        calcular_button = QPushButton(self)
        calcular_button.setText('Calcular')
        calcular_button.resize(220,24)
        calcular_button.move(65,140)
        calcular_button.clicked.connect(self.calcular_hipotenusa)

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

    def calcular_hipotenusa(self):
        if not self.catetoa_input.text().strip() or not self.catetob_input.text().strip():
            QMessageBox.warning(self, "Error", "¡Llena todos los campos!")# ← Validar que no sea vacio
            return
        self.catetoa = float(self.catetoa_input.text())   # ← Guarda en self.largo
        self.catetob = float(self.catetob_input.text())   # ← Guarda en self.ancho
        if self.catetoa > 0 and self.catetob > 0:
            hipotenusa = ((self.catetoa**2)+(self.catetob**2))
            hipotenusa = hipotenusa**0.5
            perimetro=self.catetoa+self.catetob+hipotenusa
            QMessageBox.information(self, 
            "✅ Resultados", 
            f"Cateto A: {self.catetoa}\nCateto B: {self.catetob}\nPerímetro: {perimetro:.2f}")
        else:
            QMessageBox.warning(self, "Error", "Cateto a y Cateto b deben ser > 0")

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