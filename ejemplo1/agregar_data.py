from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from crear_base import Saludo
# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///demobase.db')


Session = sessionmaker(bind=engine)
session = Session()

# se crea un objeto de tipo
# Saludo

miSaludo = Saludo()
miSaludo.mensaje = "Hola mundo desde SqlAlchemy y SQLite"

# se agrega el objeto miSaludo
# a la entidad Saludo a la sesión
# a la espera de un commit
# para agregar un registro a la base de 
# datos demobase.db
session.add(miSaludo)

# se confirma las transacciones
session.commit()
