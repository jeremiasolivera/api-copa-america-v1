from flask import Flask,redirect

from blueprints import Bapi_v1
from extensions import db,migrate,ma

app = Flask(__name__)
app.config.from_object('config')

# Extensions Initialize
db.init_app(app)
migrate.init_app(app,db)
ma.init_app(app)


# Blueprints
#postgres://apicopaamerica_user:JEYce4osoGX9T8jfvgiwwbM3Q1BMjr3j@dpg-cpeug75ds78s73fnifug-a.ohio-postgres.render.com/apicopaamerica
# API V_1
app.register_blueprint(blueprint=Bapi_v1)

@app.route('/')
def index():
    return redirect('/api/v1/selecciones')



if __name__ == '__main__':
    app.run(debug=app.config.get('DEBUG'))