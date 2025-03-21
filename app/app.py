from flask import Flask, send_from_directory

app = Flask(__name__, static_folder='../dist', static_url_path='/')

# @app.route('/')
# def wut():
#   return '<p>WE DOIN WORK</p>'


# Catch all route to handle all routing for Vue 3, this will
# allow us to serve content and allow the vue-router to work properly
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>', methods=['GET']) # might need to revisit this? Could interfere with API routes
# I think we will have to register API routes here?
def catch_all(path):
    return send_from_directory(app.static_folder, 'index.html')

# @app.route('/')
# def index():
#   return send_from_directory(app.static_folder, 'index.html')   


if __name__ == '__main__':
    app.run()
