from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QMdiArea
from PyQt6.QtGui import QAction, QIcon
from typing import Dict, Type
import time, os
from sub_windows import CustomSubWindow

from views.consulta_proveedores import ConsultaProveedores
from views.nuevo_proveedor import NuevoProveedor
from controllers.proveedores_controllers import ProveedorController

start_time = time.time()

SUBWINDOW_CLASSES: Dict[str, Type[CustomSubWindow]] = {
    "proveedores": NuevoProveedor,
    "consulta_proveedores": ConsultaProveedores,
}

MENU_STRUCTURE: Dict[str, Dict[str, str]] = {
    "Proveedores": {
        "Nuevo Proveedor": "proveedores",
        "Consultas de Proveedores": "consulta_proveedores",
    },
    "Menú 2": {
        "Submenú 2-1": "textedit",
        "Submenú 2-2": "label",
    },
    "Menú 3": {
        "Submenú 3-1": "textedit",
        "Submenú 3-2": "label",
    },
}

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Almacen MuniCallayuc")
        icon_path = os.path.join(os.path.dirname(__file__), "resources", "icons", "icon.png")
        self.setWindowIcon(QIcon(icon_path))
        self.showMaximized()
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)
        self.open_subwindows = set()

        self.create_menus()

    def create_menus(self):
        menubar = self.menuBar()
        for menu_title, submenus in MENU_STRUCTURE.items():
            menu = menubar.addMenu(menu_title)
            for submenu_title, subwindow_type in submenus.items():
                action = QAction(submenu_title, self)
                action.triggered.connect(lambda checked, title=submenu_title, type=subwindow_type: self.open_subwindow(title, type))
                menu.addAction(action)

    def open_subwindow(self, title: str, subwindow_type: str):
        if title in self.open_subwindows:
            self.raise_subwindow(title)
            return
        
        sub_window = self.create_subwindow(title, subwindow_type)
        if sub_window:
            self.open_subwindows.add(title)
            self.mdi.addSubWindow(sub_window)
            sub_window.show()
            sub_window.destroyed.connect(lambda: self.open_subwindows.remove(title))

            # Crear el controlador si es necesario
            '''if isinstance(sub_window, ConsultaProveedores):
                ProveedorController(sub_window)'''

    def raise_subwindow(self, title: str):
        for sub in self.mdi.subWindowList():
            if sub.windowTitle() == title:
                sub.raise_()
                break

    def create_subwindow(self, title: str, subwindow_type: str) -> CustomSubWindow:
        subwindow_class = SUBWINDOW_CLASSES.get(subwindow_type)
        if subwindow_class:
            return subwindow_class(title)
        return None

end_time = time.time()

print(f"Tiempo de ejecución: {end_time - start_time} segundos")
