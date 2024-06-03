from flask_restful import Resource

from models.MPartidos import MPartidos
from schemas.serializers import SchemaPartidos


class Partidos(Resource):
    def get(self):
        partidos = MPartidos.query.all()    

        schema = SchemaPartidos(many=True)

        return {'partidos':schema.dump(partidos)}


