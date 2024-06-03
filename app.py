from flask import Flask

from blueprints import Bapi_v1
from extensions import db,migrate,ma

app = Flask(__name__)
app.config.from_object('config')

# Extensions Initialize
db.init_app(app)
migrate.init_app(app,db)
ma.init_app(app)


# Blueprints

# API V_1
app.register_blueprint(blueprint=Bapi_v1)



if __name__ == '__main__':
    app.run(debug=app.config.get('DEBUG'))