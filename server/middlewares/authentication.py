#authentication.py
from flask import Flask, request, jsonify
from flask_restful import Api, Resource
import jwt
import os

app = Flask(__name__)
api = Api(app)

# Define a SECRET_KEY in your app configuration.
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

class authentication(Resource):
    def post(self):
        try:
            data = request.get_json()
            token = data.get('token', None)

            if not token:
                return jsonify({
                    'statusCode': 400,
                    'message': 'Bad Request',
                }), 400

            secret_key = app.config['SECRET_KEY']
            decoded_token = jwt.decode(token, secret_key)

            return '', 200

        except jwt.ExpiredSignatureError as expired_error:
            return jsonify({
                'statusCode': 401,
                'message': 'Your token is expired',
                'error': str(expired_error),
            }), 401

        except jwt.DecodeError as decode_error:
            return jsonify({
                'statusCode': 401,
                'message': 'Invalid token',
                'error': str(decode_error),
            }), 401

        except Exception as error:
            return jsonify({
                'statusCode': 500,
                'message': 'Internal Server Error',
                'error': str(error),
            }), 500

api.add_resource(authentication, '/authenticate')

if __name__ == '__main__':
    app.run(debug=True)
