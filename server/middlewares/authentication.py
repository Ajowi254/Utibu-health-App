#authentication.py
from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)

# Define a SECRET_KEY in your app configuration.
app.config['SECRET_KEY'] = 'MYDUKA'

@app.route('/authenticate', methods=['POST'])
def authentication():
    if request.method != 'POST':
        return jsonify({
            'statusCode': 405,
            'message': 'Method Not Allowed',
        }), 405

    try:
        data = request.get_json()
        token = data.get('token', None)

        if not token:
            return jsonify({
                'statusCode': 400,
                'message': 'Bad Request',
            }), 400

        decoded_token = jwt.decode(token, app.config['SECRET_KEY'])

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

if __name__ == '__main__':
    app.run(debug=True)

