from flask import Flask

from my_blog.user.view import user
from my_blog.article.view import article

def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprint(app)
    return app


def register_blueprint(app: Flask):
    app.register_blueprint(user)
    app.register_blueprint(article)
