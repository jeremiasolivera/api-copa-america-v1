from flask_restful import Resource
from sqlalchemy import desc
from models.Mestadios import MEstadios
from schemas.serializers import SchemaEstadios
from flask import request


class Estadios(Resource):
    def get(self):

        estado_args = request.args.get('estado')
        nombre_args = request.args.get('nombre')
        sorts = request.args.get('sort')
        estadios = MEstadios.query

        if estado_args:
            estadios = estadios.filter(MEstadios.estado.ilike(f"%{estado_args}%"))
            if estadios.count() == 0:
                return {'msg', 'No se encontró ningún estadio en el estado ingresado'}, 404

        if nombre_args:
            estadios = estadios.filter(MEstadios.nombre.ilike(f"{nombre_args}%"))
            if estadios.count() == 0:
                return {'msg': 'No se ha encontado ningún estadios'}, 404
        

        if sorts:
            for sort in sorts.split(","):
                desending = sort[0] == '-'
                if desending:
                    field = getattr(MEstadios, sort[1:])
                    print(field)
                    estadios = estadios.order_by(desc(field))
                else:
                    field = getattr(MEstadios, sort)
                    estadios = estadios.order_by(field)


        estadios = estadios.all()

        schema = SchemaEstadios(many=True)

        return {'estadios': schema.dump(estadios)}, 200

class EstadiosResources(Resource):
    def get(self,e_id):
        estadio = MEstadios.query.get_or_404(e_id)

        schema = SchemaEstadios()


        return {'estadio': schema.dump(estadio)}, 200