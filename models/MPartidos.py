from extensions import db


class MPartidos(db.Model):
    __tablename__ = "partidos"
    id_partidos = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fecha = db.Column(db.String(80),nullable=False)
    dia = db.Column(db.Date,nullable=False)
    horario = db.Column(db.String(20),nullable=False)
    grupo = db.Column(db.String(20),nullable=False)

    equipo_local_id = db.Column(db.Integer, db.ForeignKey('selecciones.id_seleccion'), nullable=False)
    equipo_local = db.relationship('MSelecciones', foreign_keys=[equipo_local_id])
    
    # Relación con el equipo visitante.
    equipo_visitante_id = db.Column(db.Integer, db.ForeignKey('selecciones.id_seleccion'), nullable=False)
    equipo_visitante = db.relationship('MSelecciones', foreign_keys=[equipo_visitante_id])

    # Relacion estadio

    estadio_id = db.Column(db.Integer, db.ForeignKey("estadios.id_estadio"), nullable=False)
    estadio = db.relationship('MEstadios', foreign_keys=[estadio_id])