from flask import Flask
def create_app():
    app = Flask(__name__)

    from .routes.sentiment import sentiment_bp
    from .routes.user import user_bp

    app.register_blueprint(sentiment_bp)
    app.register_blueprint(user_bp)

    return app
