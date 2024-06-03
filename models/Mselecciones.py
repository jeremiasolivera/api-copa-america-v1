from extensions import db

class MSelecciones(db.Model):
    __tablename__ = "selecciones"
    id_seleccion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(80), unique=True,nullable=False)
    grupo = db.Column(db.Integer,nullable=False)
    cant_copas = db.Column(db.Integer,nullable=False)
    maximo_anotador = db.Column(db.String(80), unique=True)
    participaciones = db.Column(db.Integer,nullable=False)
    region = db.Column(db.String(80),nullable=False)
    bandera_img = db.Column(db.String,unique=True,nullable=False)
    escudo_img = db.Column(db.String, unique=True)
    equipo_img = db.Column(db.String, unique=True)
    posicion_final = db.Column(db.String, nullable=True)
    camiseta_titular = db.Column(db.String, unique=True,nullable=False)
    camiseta_suplente = db.Column(db.String, unique=True,nullable=True)



class MVideosSelecciones(db.Model):
    __tablename__ = "videos_selecciones"
    id_video_seleccion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(80),nullable=False)
    descripcion = db.Column(db.Text)
    url_video = db.Column(db.String, unique=True, nullable=False)


