from flask import Flask, send_from_directory
from flask_cors import CORS
from api import api

app = Flask(__name__, static_folder='../dist', static_url_path='/')
app.register_blueprint(api, url_prefix='/api')
@app.route('/', defaults={'path': ''})
@app.route('/<string:path>')
@app.route('/<path:path>', methods=['GET']) # might need to revisit this? Could interfere with API routes
# I think we will have to register API routes here?

def catch_all(path):
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run()
