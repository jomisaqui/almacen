from sub_windows import CustomSubWindow
from PyQt6.QtWidgets import QGridLayout, QLabel, QWidget, QPushButton, QHBoxLayout, QLineEdit, QTableView, QHeaderView
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from controllers.proveedores_controllers import ProveedorController

class NuevoProveedor(CustomSubWindow):
    def __init__(self, title: str):
        super().__init__(title)

        # Inicializar controlador
        self.controlador = None

        # Crear un layout de cuadrícula
        grid_layout = QGridLayout()

        # Añadir etiquetas y campos de texto
        self.ruc_input = QLineEdit()
        self.razon_social_input = QLineEdit()
        self.telefono_input = QLineEdit()
        self.email_input = QLineEdit()
        self.direccion_input = QLineEdit()
        self.buscar_input = QLineEdit()

        # Añadir widgets al grid layout
        grid_layout.addWidget(QLabel('RUC:'), 0, 0)
        grid_layout.addWidget(self.ruc_input, 0, 1)
        grid_layout.addWidget(QLabel('RAZON SOCIAL:'), 0, 2)
        grid_layout.addWidget(self.razon_social_input, 0, 3)

        grid_layout.addWidget(QLabel('CEL./ TELEFONO:'), 1, 0)
        grid_layout.addWidget(self.telefono_input, 1, 1)
        grid_layout.addWidget(QLabel('CORREO ELECTRONICO:'), 1, 2)
        grid_layout.addWidget(self.email_input, 1, 3)

        grid_layout.addWidget(QLabel('DIRECCION:'), 2, 0)
        grid_layout.addWidget(self.direccion_input, 2, 1)

        # Botón para enviar
        
        self.submit_button = QPushButton('Agregar Proveedor')
        self.submit_button.clicked.connect(self.agregar_proveedor)  # Conectar el botón al método
        grid_layout.addWidget(self.submit_button, 3, 0, 1, 4)
        
        
        
        

        # Añadir layout horizontal para buscar
        h_layout = QHBoxLayout()
        h_layout.addWidget(QLabel('Buscar:'))
        h_layout.addWidget(self.buscar_input)
        grid_layout.addLayout(h_layout, 4, 0, 1, 0)
        
        self.buscar_input.textChanged.connect(self.filtrar_proveedores)

        # Crear y añadir QTableView al layout
        self.table_view = QTableView()
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['RUC', 'NOMBRE', 'TELEFONO', 'EMAIL'])
        self.table_view.setModel(self.model)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.model.setRowCount(0)

        # Crear una instancia de ProveedorController
        self.controlador = ProveedorController(self)  # Pasamos self como vista

        # Obtener datos de proveedores desde el controlador
        proveedores = self.controlador.cargar_proveedores()

        # Mostrar proveedores en la tabla
        self.mostrar_proveedores(proveedores)

        grid_layout.addWidget(self.table_view, 5, 0, 1, 4)

        container = QWidget()
        container.setLayout(grid_layout)
        self.setWidget(container)

    def mostrar_proveedores(self, proveedores):
        # Limpiar la tabla antes de agregar nuevos proveedores
        self.model.setRowCount(0)

        # Añadir datos a la tabla
        for proveedor in proveedores:
            ruc_item = QStandardItem(proveedor.ruc)
            nombre_item = QStandardItem(proveedor.nombre)
            telefono_item = QStandardItem(proveedor.telefono)
            email_item = QStandardItem(proveedor.email if proveedor.email else 'N/A')
            self.model.appendRow([ruc_item, nombre_item, telefono_item, email_item])
    
    def agregar_proveedor(self):
        # Recoger los datos de los campos de entrada
        ruc = self.ruc_input.text()
        nombre = self.razon_social_input.text()
        telefono = self.telefono_input.text()
        email = self.email_input.text()
        direccion = self.direccion_input.text()

        # Llamar al método agregar_proveedor del controlador
        self.controlador.agregar_proveedor(ruc, nombre, telefono, email, direccion)

        # Limpiar los campos después de agregar
        self.ruc_input.clear()
        self.razon_social_input.clear()
        self.telefono_input.clear()
        self.email_input.clear()
        self.direccion_input.clear()
    def filtrar_proveedores(self):
        termino = self.buscar_input.text()
        self.controlador.buscar_proveedores(termino)
