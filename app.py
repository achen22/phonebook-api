from flask import Flask, request
from flask_restx import Resource, Api
from database.models import db
import settings

app = Flask(__name__)
api = Api(app)

# configure database
app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(app)

@api.route('/hello/')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

if __name__ == '__main__':
    app.run(debug=True)
