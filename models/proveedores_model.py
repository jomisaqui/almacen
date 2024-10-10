from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from conexion import ConexionDB
from crear_tablas import Proveedor

class ProveedorModel:
    def __init__(self):
        self.conexion = ConexionDB()
        self.conexion.conectar()
        self.session = sessionmaker(bind=self.conexion.engine)

    def obtener_proveedores(self):
        try:
            sesion = self.session()
            proveedores = sesion.query(Proveedor).all()
            sesion.close()
            return proveedores
        except SQLAlchemyError as e:
            print(f"Error al obtener proveedores: {e}")
            return None

    def agregar_proveedor(self, ruc, nombre, telefono=None, email=None, direccion=None):
        try:
            sesion = self.session()
            proveedor = Proveedor(ruc=ruc, nombre=nombre, telefono=telefono, email=email, direccion=direccion)
            sesion.add(proveedor)
            sesion.commit()
            sesion.close()
            return True
        except SQLAlchemyError as e:
            print(f"Error al agregar proveedor: {e}")
            return False

    def obtener_proveedor(self, id):
        try:
            sesion = self.session()
            proveedor = sesion.get(Proveedor, id)
            sesion.close()
            return proveedor
        except SQLAlchemyError as e:
            print(f"Error al obtener proveedor: {e}")
            return None
    
    
    def actualizar_proveedor(self, id, ruc, nombre, telefono=None, email=None, direccion=None):
        try:
            sesion = self.session()
            proveedor = sesion.get(Proveedor, id)
            proveedor.ruc = ruc
            proveedor.nombre = nombre
            proveedor.telefono = telefono
            proveedor.email = email
            proveedor.direccion = direccion
            sesion.commit()
            sesion.close()
            return True
        except SQLAlchemyError as e:
            print(f"Error al actualizar proveedor: {e}")
            return False
        
    def buscar_proveedores(self, termino):
        try:
            sesion = self.session()
            proveedores = sesion.query(Proveedor).filter(
                (Proveedor.ruc.like(f"%{termino}%")) | 
                (Proveedor.nombre.like(f"%{termino}%"))
            ).all()
            sesion.close()
            return proveedores
        except SQLAlchemyError as e:
            print(f"Error al buscar proveedores: {e}")
            return None


    def eliminar_proveedor(self, id):
        try:
            sesion = self.session()
            proveedor = sesion.query(Proveedor).get(id)
            sesion.delete(proveedor)
            sesion.commit()
            sesion.close()
            return True
        except SQLAlchemyError as e:
            print(f"Error al eliminar proveedor: {e}")
            return False

    def cerrar_conexion(self):
        self.conexion.cerrar()

