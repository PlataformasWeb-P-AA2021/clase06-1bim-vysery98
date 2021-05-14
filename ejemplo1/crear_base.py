from sqlalchemy import create_engine

# se genera en enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine('sqlite:///demobase.db', echo=True)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy import Column, Integer, String

class Saludo(Base):
    __tablename__ = 'saludo'
    
    id = Column(Integer, primary_key=True)
    mensaje = Column(String)

class Saludo2(Base):
    __tablename__ = 'saludo2'
    id = Column(Integer, primary_key=True)
    mensaje = Column(String)
    mensaje2 = Column(String)

class Saludo3(Base):
    __tablename__ = 'saludo3'
    id = Column(Integer, primary_key=True)
    mensaje = Column(String)
    mensaje2 = Column(String)



Base.metadata.create_all(engine)


