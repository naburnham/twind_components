import os

from flask import Flask, redirect, url_for

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import home
    app.register_blueprint(home.bp)

    @app.route('/')
    def home():
        return redirect(url_for("home.index"))

    return app
