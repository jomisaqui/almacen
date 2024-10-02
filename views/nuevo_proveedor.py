from PyQt6.QtWidgets import QFormLayout, QLineEdit, QPushButton
from sub_windows import CustomSubWindow
from PyQt6.QtWidgets import QGridLayout, QLabel, QWidget, QVBoxLayout

class NuevoProveedor(CustomSubWindow):
    def __init__(self, title: str):
        super().__init__(title)

        # Crear un layout de formulario
        form_layout = QFormLayout()

        # Añadir etiquetas y campos de texto
        name_input = QLineEdit()
        email_input = QLineEdit()

        form_layout.addRow(QLabel('Nombre:'), name_input)
        form_layout.addRow(QLabel('Email:'), email_input)

        # Botón para enviar
        submit_button = QPushButton('Enviar')
        form_layout.addRow(submit_button)

        container = QWidget()
        container.setLayout(form_layout)
        # Establecer el layout en el widget
        self.setWidget(container)