from flask import Flask
from flask_jwt_extended import JWTManager
from flask_pymongo import PyMongo
from config import Config
from routes.auth_routes import auth_bp
from routes.event_routes import event_bp
from routes.registration_routes import registration_bp

app = Flask(__name__)
app.config.from_object(Config)
jwt = JWTManager(app)
mongo = PyMongo(app)

app.mongo = mongo

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(event_bp, url_prefix='/events')
app.register_blueprint(registration_bp, url_prefix='/register')

if __name__ == '__main__':
    app.run(debug=True)