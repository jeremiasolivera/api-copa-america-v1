from extensions import ma
from marshmallow import fields

#Modelos
from models.Mselecciones import MSelecciones, MVideosSelecciones
from models.Mestadios import MEstadios
from models.MPartidos import MPartidos


class SchemaSelecciones(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = MSelecciones
        exclude = ["id_seleccion"]
        load_instance = True




class SchemaEstadios(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = MEstadios
        exclude = ["id_estadio"]



class SchemaPartidos(ma.SQLAlchemyAutoSchema):
        equipo_local = fields.Nested(SchemaSelecciones, many=False,only=["nombre","bandera_img","escudo_img","camiseta_titular"])
        equipo_visitante = fields.Nested(SchemaSelecciones, many=False,only=["nombre","bandera_img","escudo_img","camiseta_suplente"])
       

        class Meta:
            model = MPartidos
            exclude = ["id_partidos"]


class SchemaVideosSelecciones(ma.SQLAlchemyAutoSchema):
     class Meta:
          model = MVideosSelecciones
          exclude = ["id_video_seleccion"]