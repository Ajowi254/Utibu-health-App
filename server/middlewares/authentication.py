#authentication.py
from flask import Flask, request, jsonify
import jwt

app = Flask(__name__)

@app.route('/authenticate', methods=['POST'])
def authentication():
    token = request.json.get('token', None)
    if token:
        try:
            decode = jwt.decode(token, app.config['SECRET_KEY'])
            return '', 200
        except Exception as error:
            return jsonify({
                'statusCode': 401,
                'message': 'Your token is expired',
                'error': str(error),
            }), 401
    else:
        return jsonify({
            'statusCode': 401,
            'message': 'Unauthorized'
        }), 401

if __name__ == '__main__':
    app.run(debug=True)
