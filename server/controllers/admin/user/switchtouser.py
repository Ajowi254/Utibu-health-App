#switchtouser.py
from models.userModel import UserDetails
from flask import jsonify, request

def switch_to_user(id):
    try:
        e = request.json['e']
        doc = UserDetails.find_by_id(id)
        if doc['email'] == 'kirubam8878@gmail.com':
            return jsonify({
                'statusCode': 401,
                'message': 'Default Admin Account, So Role Does Not Update'
            })
        else:
            doc['isAdmin'] = e
            doc.save()
            return jsonify({
                'statusCode': 200,
                'message': 'Role updated successfully'
            })
    except Exception as error:
        return jsonify({
            'statusCode': 500,
            'message': 'Internal Server Error',
            'error': str(error)
        })
