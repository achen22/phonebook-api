from flask import Flask, render_template
from flask_restx import Resource, Api
from database.models import db, Contact
import settings

app = Flask(__name__)
api = Api(app)

# configure database
app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(app)

@app.route('/test')
def test():
    contacts = Contact.query.all()
    return render_template('test.html', contacts=contacts)

@api.route('/hello/')
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

if __name__ == '__main__':
    app.run(debug=True)
