from models.proveedores_model import ProveedorModel

class ProveedorController:
    def __init__(self, vista):
        self.vista = vista
        self.modelo = ProveedorModel()
        self.vista.set_controlador(self)
        self.cargar_proveedores()

    def cargar_proveedores(self):
        proveedores = self.modelo.obtener_proveedores()
        self.vista.mostrar_proveedores(proveedores)

    def agregar_proveedor(self, ruc, nombre, telefono=None, email=None, direccion=None):
        exito = self.modelo.agregar_proveedor(ruc, nombre, telefono, email, direccion)
        if exito:
            self.cargar_proveedores()
        else:
            print("Error al agregar proveedor")

    def actualizar_proveedor(self, id, ruc, nombre, telefono=None, email=None, direccion=None):
        exito = self.modelo.actualizar_proveedor(id, ruc, nombre, telefono, email, direccion)
        if exito:
            self.cargar_proveedores()
        else:
            print("Error al actualizar proveedor")

    def eliminar_proveedor(self, id):
        exito = self.modelo.eliminar_proveedor(id)
        if exito:
            self.cargar_proveedores()
        else:
            print("Error al eliminar proveedor")
