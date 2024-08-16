import os

from flask import Flask, render_template

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import components
    app.register_blueprint(components.bp)

    @app.route('/')
    def home():
        return render_template('index.html')

    return app
