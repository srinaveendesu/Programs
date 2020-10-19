from flask import Flask
from flask_restful import Resource,Api
import socket

app = Flask(__name__)
api = Api(app)

class Welcome(Resource):
    def get(self):
        hostname = socket.gethostname()

        return {'message': f'Welcome to microservice Demo! from {hostname}'}

api.add_resource(Welcome, '/')

if __name__ == '__main__':
    app.run(debug=True,port=5051,host="0.0.0.0")