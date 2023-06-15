from __main__ import app
from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy(app)


class Preceptor(db.Model):
    __tablaname__="preceptor"
    id=db.Column(db.Integer,primary_key=True)
    nombre=db.Colum(db.String(20),nullable=False)
    apellido=db.Column(db.String(20),nullable=False)
    correo=db.Column(db.String(50),nullable=False,unique=True)
    clave=db.Column(db.String(50),nullable=False)
    
class Curso(db.Model):
    __tablaname__="curso"
    id=db.Column(db.Integer,primary_key=True)
    anio=db.Column(db.Integer)
    division=db.Column(db.Integer(20))
    idPreceptor=db.Column(db.Integer(20),db.ForeingKey("preceptor.id"))
class Estudiante:
    __tablename__="estudiante"
    id=db.Column(db.Integer(20),primary_key=True)
    nombre=db.Colum(db.String(20),nullable=False)
    apellido=db.Colum(db.String(20),nullable=False)
    dni=db.Column(db.Integer(20),unique=True)
    idCurso=db.Column(db.Integer(20),db.ForeingKey("curso.id"))
    idPadre=db.Column(db.Integer(20),db.ForeingKey("padre.id"))
    
class Asistencia:
    __tablename__="asistencia"
    id=db.Column(db.Integer(20),primary_key=True)
    fecha=db.Column(db.DateTime)
    codigoClase=db.Column(db.Integer(20))
    aisitio=db.Column(db.Boolean,nullable=False)
    justificacion=db.Colum(db.String(100),nullable=True)
    idEstudiante=db.Column(db.Integer(20),db.ForeingKey("estudiante.id"))
    
    
class Padre:
    __tablename__="padre"
    id=db.Column(db.Integer(20),primary_key=True)
    nombre=db.Colum(db.String(20),nullable=False)
    apellido=db.Colum(db.String(20),nullable=False)
    correo=db.Column(db.String(50),nullable=False,unique=True)
    clave=db.Column(db.String(50),nullable=False)
    
    

    
    
    
    
    
    
    
    