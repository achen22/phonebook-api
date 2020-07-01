from flask_restx import reqparse, inputs

date_range = reqparse.RequestParser()
date_range.add_argument('from', type=int, help='Only contacts updated after this timestamp will be returned.')
date_range.add_argument('to', type=int, help='Only contacts updated before this timestamp will be returned.')

new_contact = reqparse.RequestParser()
new_contact.add_argument('name', location='json', required=True)
new_contact.add_argument('email', location='json')
new_contact.add_argument('phone', location='json')
new_contact.add_argument('dob', location='json', type=inputs.date)

existing_contact = new_contact.copy()
existing_contact.add_argument('id', location='json', type=int, required=True)
