import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class usuario(Base):
    __tablename__ = 'usuario'
    id_usuario = Column(Integer, primary_key=True)
    nombre = Column(String(30), nullable=False)
    apellidos = Column(String(60), nullable=False)
    contraseña = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)
    fecha_suscripcion = Column(String(10), nullable=False)
    usuario = relationship('usuario',backref='favoritos', lazy=True)

class planetas(Base):
    __tablename__ = 'planetas'
    id_planeta = Column(Integer, primary_key=True)
    nombre = Column(String(30), nullable=False)
    planetas = relationship('planetas',backref='favoritos', lazy=True)

class personajes(Base):
    __tablename__ = 'personajes'
    id_personaje = Column(Integer, primary_key=True)
    nombre = Column(String(30), nullable=False)
    personajes = relationship('personajes',backref='favoritos', lazy=True)

class favoritos(Base):
    __tablename__ = 'favoritos'
    id_favoritos = Column(Integer, primary_key=True)
    fk_usuario = Column(Integer, ForeignKey('usuario.id_usuario'))
    fk_planeta = Column(Integer, ForeignKey('planetas.id_planeta'))
    fk_personaje = Column(Integer, ForeignKey('personajes.id_personaje'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')