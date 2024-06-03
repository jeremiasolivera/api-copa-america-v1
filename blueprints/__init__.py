from flask_restful import Api
from flask import Blueprint

# SELECCIONES
from api.selecciones import Selecciones,SeleccionesResource,SeleccionesVideos
# ESTADIOS 
from api.estadios import Estadios, EstadiosResources
# PARTIDOS
from api.partidos import Partidos



Bapi_v1 = Blueprint('selecciones', __name__,url_prefix='/api/v1')


api=Api(Bapi_v1)

# SELECCIONES URLS
api.add_resource(Selecciones, '/selecciones')
api.add_resource(SeleccionesResource, '/selecciones/<int:s_id>')
api.add_resource(SeleccionesVideos, '/selecciones/videos')


#ESTADIOS URLS
api.add_resource(Estadios, '/estadios')
api.add_resource(EstadiosResources, '/estadios/<int:e_id>')

#PARTIDOS URLS
api.add_resource(Partidos, '/partidos')