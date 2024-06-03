from extensions import db

class MEstadios(db.Model):
    __tablename__ = 'estadios'
    id_estadio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(80), unique=True,nullable=False)
    estado = db.Column(db.String(80),nullable=False)
    localizacion = db.Column(db.String(80),nullable=False)
    apertura = db.Column(db.Date,nullable=False)
    capacidad = db.Column(db.Integer,nullable=False)
    equipo_local = db.Column(db.String(80),nullable=False)
    img_estadio = db.Column(db.String(80), nullable=False, unique=True)