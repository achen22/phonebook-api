from flask_restx import reqparse, inputs

since = reqparse.RequestParser()
since.add_argument('since', type=int, help='Only contacts updated after this timestamp will be returned.')

new_contact = reqparse.RequestParser()
new_contact.add_argument('name', required=True)
new_contact.add_argument('email')
new_contact.add_argument('phone')
new_contact.add_argument('dob', type=inputs.date)

existing_contact = new_contact.copy()
existing_contact.replace_argument('name', required=False)
