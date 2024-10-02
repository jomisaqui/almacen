from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError, InterfaceError, SQLAlchemyError
from sqlalchemy import create_engine

Base = declarative_base()

class ConexionError(Exception):
    """Excepción personalizada para errores en la conexión a la base de datos."""
    def __init__(self, mensaje):
        super().__init__(mensaje)

class ConexionDB:
    def __init__(self):
        self.engine = None
        self.Session = None
    
    def conectar(self):
        user = 'sa'
        password = 'jm17sq78'
        host = 'localhost'
        database = 'db_almacen'
        
        try:
            if self.engine is None:
                print("Intentando conectar a la base de datos...")
                self.engine = create_engine(
                    f'mssql+pyodbc://{user}:{password}@{host}/{database}?driver=ODBC+Driver+17+for+SQL+Server'
                )
                self.Session = sessionmaker(bind=self.engine)
                # Intentar una operación simple para verificar la conexión
                with self.engine.connect() as connection:
                    connection.execute(text("SELECT 1"))
                print("Conexión exitosa.")
        except (OperationalError, InterfaceError) as e:
            error_message = str(e)
            print(f"Error operacional: {error_message}")
            if "Can't connect to MySQL server" in error_message:
                raise ConexionError("Host no encontrado")
            elif "Access denied for user" in error_message:
                raise ConexionError("Usuario o contraseña incorrecta")
            elif "Unknown database" in error_message:
                raise ConexionError("Base de datos no existe")
            else:
                raise ConexionError(f"Error al conectar a la base de datos: {error_message}")
        except SQLAlchemyError as e:
            error_message = str(e)
            print(f"Error al conectar a la base de datos: {error_message}")
            raise ConexionError(f"Error al conectar a la base de datos: {error_message}")
    
    def cerrar(self):
        if self.engine:
            self.engine.dispose()
            self.engine = None
            print("Conexión cerrada.")
        else:
            print("No hay conexión abierta para cerrar.")
