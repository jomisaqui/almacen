from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from conexion import ConexionDB  # Asegúrate de que el nombre del módulo de conexión sea correcto

Base = declarative_base()

class Proveedor(Base):
    __tablename__ = 'proveedores'
    
    id = Column(Integer, primary_key=True)
    ruc = Column(String(11), unique=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    telefono = Column(String(15))
    email = Column(String(100))
    direccion = Column(String(200))
    
    # Muestra todos los atributos de la clase
    def __repr__(self):
        return f"<Proveedor {', '.join(f'{key}={value}' for key, value in vars(self).items() if key != '_sa_instance_state')}>"

    # Muestra solo los atributos id y el nombre
    #def __repr__(self):
        #return f"<Proveedor(id={self.id}, nombre={self.nombre})>"

class Producto(Base):
    __tablename__ = 'productos'
    
    id = Column(Integer, primary_key=True)
    codigo = Column(String(20), unique=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    #proveedor_id = Column(Integer, ForeignKey('proveedores.id'), nullable=False)

    #proveedor = relationship("Proveedor", back_populates="productos")

    def __repr__(self):
        return f"<Producto(id={self.id}, nombre={self.nombre}, precio={self.precio})>"

#Proveedor.productos = relationship("Producto", order_by=Producto.id, back_populates="proveedor")

def crear_tablas():
    conexion = ConexionDB()
    conexion.conectar()
    try:
        # Crea todas las tablas si no existen
        Base.metadata.create_all(conexion.engine)
        print("Tablas creadas o ya existentes.")
    except Exception as e:
        print(f"Error al crear tablas: {e}")
    finally:
        conexion.cerrar()

if __name__ == "__main__":
    crear_tablas()
