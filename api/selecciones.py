from flask_restful import Resource
from sqlalchemy import desc
from schemas.serializers import SchemaSelecciones, SchemaVideosSelecciones
from flask import jsonify,request

# Model
from models.Mselecciones import MSelecciones, MVideosSelecciones

class Selecciones(Resource):
    def get(self):

        s_name_filter = request.args.get("nombre")
        s_region_filter = request.args.get("region")
        s_grupo_filter = request.args.get("grupo")
        sorts = request.args.get('sort')
        selecciones_query = MSelecciones.query


        if s_name_filter:
            selecciones_query = selecciones_query.filter(MSelecciones.nombre.ilike(f"{s_name_filter}%"))
            if selecciones_query.count() == 0:
                return {'msg':'La selección no se ha encontrado.'}, 404

        if s_region_filter:
            selecciones_query = selecciones_query.filter(MSelecciones.region.ilike(f"%{s_region_filter}"))
            if selecciones_query.count() == 0:
                return {'msg':'La región no es válida.'}, 404

        if s_grupo_filter:
            selecciones_query = selecciones_query.filter(MSelecciones.grupo == s_grupo_filter)
            if selecciones_query.count() == 0:
                return {'msg':'Sólo hay 4 grupos.'}, 404
            
        if sorts:
            for sort in sorts.split(","):
                desending = sort[0] == "-"             # ?nombre   sort = nombre
                if desending:
                    field = getattr(MSelecciones, sort[1:])  # nombre field = MSelecciones.nombre
                    selecciones_query = selecciones_query.order_by(desc(field))
                else:
                    field = getattr(MSelecciones, sort)
                    selecciones_query = selecciones_query.order_by(field)

        selecciones = selecciones_query.all()
        schema = SchemaSelecciones(many=True)
        return {'results':schema.dump(selecciones)}, 200


class SeleccionesResource(Resource):
    def get(self,s_id):
        seleccion = MSelecciones.query.get_or_404(s_id)
        schema = SchemaSelecciones()

        return {'partidos':schema.dump(seleccion)}, 200


class SeleccionesVideos(Resource):
    def get(self):
        
        titulo_args = request.args.get('titulo')
        videos = MVideosSelecciones.query

        if titulo_args:
            videos = videos.filter(MVideosSelecciones.titulo.ilike(f"%{titulo_args}%"))
            if videos.count() == 0:
                return {'msg': 'Video no encontrado'}, 404
            

        
        videos = videos.all()    
        schema_videos = SchemaVideosSelecciones(many=True)


        return {'msg': 'videos de selecciones', 'results': schema_videos.dump(videos)}