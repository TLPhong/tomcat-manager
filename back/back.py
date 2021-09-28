from flask import Flask, send_from_directory
from flask_cors import CORS

app = Flask(
    import_name="Tomcat manager",
    static_url_path="/",
    static_folder="public",
)
CORS(app)


@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
