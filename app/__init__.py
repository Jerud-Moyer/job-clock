import os
from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    print("Database URL:", os.getenv('DATABASE_URL'))
    app = Flask(__name__, static_folder='../dist', static_url_path='/')
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

    db.init_app(app)
    migrate = Migrate(app, db)

    from .api import api

    app.register_blueprint(api, url_prefix='/api')
    @app.route('/', defaults={'path': ''})
    @app.route('/<string:path>')
    @app.route('/<path:path>', methods=['GET']) # might need to revisit this? Could interfere with API routes
    # I think we will have to register API routes here?

    def catch_all(path):
        return send_from_directory(app.static_folder, 'index.html')

    app.config.from_pyfile('config.py', silent=True)

    try:
      os.makedirs(app.instance_path)
    except OSError:
        pass

    return app