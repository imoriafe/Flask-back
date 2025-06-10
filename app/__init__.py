from flask import Flask
from app.routes.register import register_bp
from app.routes.user import user_bp
from app.routes.sentiment import sentiment_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(register_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(sentiment_bp)
    return app
