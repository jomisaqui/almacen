from sub_windows import CustomSubWindow
from PyQt6.QtWidgets import QGridLayout, QLabel, QWidget, QPushButton, QHBoxLayout, QLineEdit, QTableView, QHeaderView
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from controllers.proveedores_controllers import ProveedorController

class ConsultaProveedores(CustomSubWindow):
    def __init__(self, title: str):
        super().__init__(title)

        # Inicializar controlador
        self.controlador = None

        # Crear un layout de cuadrícula
        grid_layout = QGridLayout()

        # Añadir etiquetas y campos de texto
        self.buscar_input = QLineEdit()      
        

        # Añadir layout horizontal para buscar
        h_layout = QHBoxLayout()
        h_layout.addWidget(QLabel('Buscar:'))
        h_layout.addWidget(self.buscar_input)
        grid_layout.addLayout(h_layout, 0, 0, 1, 1)
        
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

    
    def filtrar_proveedores(self):
        termino = self.buscar_input.text()
        self.controlador.buscar_proveedores(termino)
