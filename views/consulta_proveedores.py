from sub_windows import CustomSubWindow
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QTableView, QHeaderView
from PyQt6.QtGui import QStandardItemModel, QStandardItem

class ConsultaProveedores(CustomSubWindow):
    def __init__(self, title: str):
        super().__init__(title)
       
        # Crear el QTableView
        self.table_view = QTableView()
        self.setup_table_view()
        
        # Crear el layout y añadir los widgets
        layout = QVBoxLayout()
        layout.addWidget(self.table_view)
        
        # Configurar el contenedor
        container = QWidget()
        container.setLayout(layout)
        self.setWidget(container)

    def set_controlador(self, controlador):
        self.controlador = controlador

    def setup_table_view(self):
        # Crear un modelo de datos para el QTableView
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['ID', 'RUC', 'NOMBE', 'TELEFONO', 'EMAIL'])
        self.table_view.setModel(self.model)
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def mostrar_proveedores(self, proveedores):
        self.model.setRowCount(0)  # Limpiar la tabla
        if proveedores:
            for proveedor in proveedores:
                id_item = QStandardItem(str(proveedor.id))
                ruc_item = QStandardItem(proveedor.ruc)
                nombre_item = QStandardItem(proveedor.nombre)
                telefono_item = QStandardItem(proveedor.telefono)                
                email_item = QStandardItem(proveedor.email if proveedor.email else 'N/A')
                
                self.model.appendRow([id_item, ruc_item, nombre_item, telefono_item, email_item])
        else:
            print("No se pudieron obtener los proveedores.")
