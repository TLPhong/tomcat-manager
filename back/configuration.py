from flask import Flask
from flask_cors import CORS

app = Flask(
    import_name="Tomcat manager",
    static_url_path="/",
    static_folder="public",
)

CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5000"}})
