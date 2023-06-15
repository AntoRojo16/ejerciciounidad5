from datetime import datetime
from flask import Flask, request, reder_template
from flask_sqlalchemy import SQLAlchemy

from werkzeug.security import generate_password_hash, check_passwor_hash

app= Flask(__name__)
#app.confing.from_pyfile() 
from models import db
from models import Preceptor, Curso, Asistencia, Estudiante,Padre

if __name__=="__main__":
    db.create_all()
    app.run(debug=True)