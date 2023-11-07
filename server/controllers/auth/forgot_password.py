#forgot.password.py
from flask import Flask, request
from flask_restful import Resource
from models.userModel import UserDetails
from flask_mail import Mail, Message
from itsdangerous import URLSafeTimedSerializer
import os

app = Flask(__name__)
mail = Mail(app)

class forgot_password(Resource):
    def post(self):
        try:
            email = request.json['email']
            user = UserDetails.find_one({'email': email})
            if user:
                s = URLSafeTimedSerializer(os.environ.get('SECRET_KEY'))
                token = s.dumps(user['_id'], salt=os.environ.get('SECURITY_PASSWORD_SALT'))
                url = f"{os.environ.get('BASE_URL')}/forgot-password-page/{user['_id']}/{token}"

                msg = Message("Hello ✔",
                              sender="ajowi.beryl@gmail.com",
                              recipients=[user['email']])
                msg.body = "Reset link"
                msg.html = f"""<div style=" border:3px solid blue; padding : 20px;"><span>Password Reset Link : - </span> <a href={url}> Click
                          here !!!</a>
                      <div>
                          <h4>
                              Note :-
                              <ul>
                                  <li>This link only valid in 10 minitues</li>
                              </ul>
                          </h4>
                      </div>
                  </div>"""
                mail.send(msg)

                return {'statusCode': 200, 'message': 'Password Reset link sent in your mail'}
            else:
                return {'statusCode': 401, 'message': 'Please enter valid email address'}
        except Exception as error:
            return {'statusCode': 500, 'message': 'Internal Server Error', 'error': str(error)}
