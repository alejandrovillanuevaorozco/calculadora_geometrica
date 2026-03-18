import sys
from PyQt6.QtWidgets import (QApplication,QLabel,QWidget, QLineEdit,QPushButton,QMessageBox,QCheckBox)
from PyQt6.QtGui import (QFont, QPixmap,QDoubleValidator)

class area(QWidget):
    def __init__(self):
        super().__init__()
        self.inicializar_ui()
    
    def inicializar_ui(self):
        self.setGeometry(100,100,350,250)
        self.setWindowTitle("Calculo del área del triangulo")
        self.generar_formulario()
        self.show()

    def generar_formulario(self):
        self.is_trianguleado=False

#Crear label y agregarle sus caracteristicas
        base_label = QLabel(self)
        base_label.setText("Base del triangulo:")
        base_label.setFont(QFont('Arial',10))
        base_label.move(20,54)

#Crear el input del label anterior
        self.base_input=QLineEdit(self)
        self.base_input.resize(50,24)
        self.base_input.move(145,50)
        self.base_input.setValidator(QDoubleValidator(0, 9999, 2))

        altura_label = QLabel(self)
        altura_label.setText("Altura del triangulo:")
        altura_label.setFont(QFont('Arial',10))
        altura_label.move(20,86)

        self.altura_input=QLineEdit(self)
        self.altura_input.resize(50,24)
        self.altura_input.move(145,82)
        self.altura_input.setValidator(QDoubleValidator(0, 9999, 2))

#Crear botones y colocarle sus caracteristicas
        calcular_button = QPushButton(self)
        calcular_button.setText('Calcular')
        calcular_button.resize(220,24)
        calcular_button.move(65,140)
        calcular_button.clicked.connect(self.calcular_area_triangulo)

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

    def calcular_area_triangulo(self):
        if not self.base_input.text().strip() or not self.altura_input.text().strip():
            QMessageBox.warning(self, "Error", "¡Llena todos los campos!")# ← Validar que no sea vacio
            return
        self.base = float(self.base_input.text())   # ← Guarda en self.largo
        self.altura = float(self.altura_input.text())   # ← Guarda en self.ancho
        if self.base > 0 and self.altura > 0:
            area = (self.base*self.altura)/2
            QMessageBox.information(self, 
            "✅ Resultados", 
            f"Base: {self.base}\nAltura: {self.altura}\nÁrea: {area:.2f}")
        else:
            QMessageBox.warning(self, "Error", "Base y altura deben ser > 0")

    def volver_main(self):
        from main import menu_principal
        self.hide()
        self.abrir_main_form = menu_principal()
        self.abrir_main_form.show()

    def volver_atras(self):
        from menu_triangulo_arv import menu_triangulo
        self.hide()
        self.abrir_main_form = menu_triangulo()
        self.abrir_main_form.show()


        




if __name__=='__main__':
    app= QApplication(sys.argv)
    ar = area()
    sys.exit(app.exec())