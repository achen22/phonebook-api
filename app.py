from flask import Flask, render_template, request
from flask_restx import Resource, Api, fields
from database.models import db, Contact
import settings
from datetime import datetime, date
import api.parsers as parsers

app = Flask(__name__)
api = Api(app, title='Phonebook API', prefix='/api')
ns = api.namespace('Contact', description='Operations related to contacts')

# configure database
app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
db.init_app(app)

# models
contact_model = api.model('Contact', {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
    'phone': fields.String,
    'dob': fields.Date
})

def marshal(contact):
    return api.marshal(contact, contact_model)

@app.route('/test')
def test():
    contacts = Contact.query.all()
    return render_template('test.html', contacts=contacts)

@ns.route('/')
class ContactApi(Resource):
    @api.marshal_list_with(contact_model)
    @api.expect(parsers.since)
    def get(self):
        """
        Returns list of phonebook contacts.
        """
        args = parsers.since.parse_args(request)
        last_updated_at = args['since']

        if last_updated_at:
            timestamp = datetime.fromtimestamp(last_updated_at)
            return Contact.query.filter(Contact.updated_at > timestamp).all()
        return Contact.query.all()
    
    @api.response(201, 'Contact successfully created', contact_model)
    @api.response(400, 'Contact name cannot be empty')
    @api.expect(contact_model)
    def post(self):
        """
        Creates a new phonebook contact.
        """
        args = parsers.new_contact.parse_args(request)
        if not args['name']:
            return {'errors': {'name': 'Non-empty string required'}}, 400
        contact = Contact(**args)
        db.session.add(contact)
        db.session.commit()
        return marshal(contact), 201

@ns.route('/<int:id>')
@api.response(404, 'Contact not found')
class SingleContactApi(Resource):
    @api.response(200, 'Success.', contact_model)
    def get(self, id):
        """
        Returns a phonebook contact.
        """
        contact = Contact.query.get(id)
        if not contact:
            return {'errors': {'id': 'No contact with this id'}}, 404
        return marshal(contact)

    @api.response(204, 'Contact successfully updated')    
    @api.response(400, 'Request contains an error')
    @api.expect(contact_model)
    def put(self, id):
        """
        Updates a phonebook contact.
        """
        if request.json.get('id') != id:
            return {'errors': {'id': 'Does not match path id'}}, 400
        contact = Contact.query.get(id)
        if not contact:
            return {'errors': {'id': 'No contact with this id'}}, 404
        args = parsers.existing_contact.parse_args(request)
        if not args['name']:
            return {'errors': {'name': 'Non-empty string required'}}, 400
        contact.name = args['name']
        contact.email = args['email']
        contact.phone = args['phone']
        contact.dob = args['dob']
        db.session.commit()
        return None, 204

    @api.response(200, 'Contact successfully deleted', contact_model)
    def delete(self, id):
        """
        Deletes a phonebook contact.
        """
        contact = Contact.query.get(id)
        if not contact:
            return {'errors': {'id': 'No contact with this id'}}, 404
        db.session.delete(contact)
        db.session.commit()
        return marshal(contact), 200

if __name__ == '__main__':
    app.run(debug=True)
