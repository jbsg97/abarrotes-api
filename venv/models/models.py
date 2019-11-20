from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect
from extension import db


class Products(db.Model):
    __tablename__ = 'productos'
    id_producto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String, unique=True, nullable=False)
    precio = db.Column(db.Float, unique=True, nullable=False)
    stock = db.Column(db.Integer, unique=True, nullable=False)
    descripcion = db.Column(db.String, unique=True, nullable=False)

    def __init__(self, nombre, precio, stock, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.descripcion = descripcion

    
    def to_json(self):
        return {c.key: getattr(self, c.key)
                for c in inspect(self).mapper.column_attrs}

class Workers(db.Model):
    __tablename__ = 'empleados'
    id_empleado = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String, unique=True, nullable=False)
    apellidos = db.Column(db.String, unique=True, nullable=False)
    puesto = db.Column(db.String, unique=True, nullable=False)

    def __init__(self, nombres, apellidos, puesto):
        self.nombres = nombres
        self.apellidos = apellidos
        self.puesto = puesto

    
    def to_json(self):
        return {c.key: getattr(self, c.key)
                for c in inspect(self).mapper.column_attrs}