from PyQt6.QtWidgets import QMdiSubWindow, QMessageBox, QApplication
from PyQt6.QtGui import QIcon
import os

class CustomSubWindow(QMdiSubWindow):
    def __init__(self, title: str):
        super().__init__()
        self.setWindowTitle(title)
        icon_path = os.path.join(os.path.dirname(__file__), "resources", "icons", "icon.png")
        self.setWindowIcon(QIcon(icon_path))
        #self.setGeometry(100, 100, 800, 600)
        # Obtener dimensiones de la pantalla
        screen = QApplication.primaryScreen()
        screen_rect = screen.availableGeometry()

        # Calcular el tamaño deseado (50% del tamaño de la pantalla)
        width = int(screen_rect.width() * 1.0)  # 50% del ancho
        height = int(screen_rect.height() * 0.935)  # 50% de la altura

        # Establecer tamaño de la ventana
        self.resize(width, height)

        # Centrar la ventana en la pantalla
        self.setGeometry(
            (screen_rect.width() - width) // 2,
            (screen_rect.height() - height) // 2,
            width,
            height
        )


    def closeEvent(self, event):
        reply = QMessageBox.question(
            self, 'Confirmar Cierre',
            f"¿Estás seguro de que quieres cerrar la subventana '{self.windowTitle()}'?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            print(f"Subventana '{self.windowTitle()}' cerrada")
            #self.ProveedorModel.cerrar_conexion()
            self.deleteLater()  # Asegura que la subventana se elimine correctamente
            
        else:
            event.ignore()
