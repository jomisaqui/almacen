from PyQt6.QtWidgets import QTextEdit
from sub_windows import CustomSubWindow
from PyQt6.QtWidgets import QGridLayout, QLabel, QWidget, QVBoxLayout

class NuevoProveedor(CustomSubWindow):
    def __init__(self, title: str):
        super().__init__(title)
        layout = QGridLayout()
        
        widget1 = QLabel("Widget 1")
        widget2 = QLabel("Widget 2")
        widget3 = QLabel("Widget 3")
        
        layout.addWidget(widget1, 0, 0)  # Fila 0, Columna 0
        layout.addWidget(widget2, 0, 1)  # Fila 0, Columna 1
        layout.addWidget(widget3, 1, 0, 1, 2)
        
        container = QWidget()
        container.setLayout(layout)
        self.setWidget(container)
