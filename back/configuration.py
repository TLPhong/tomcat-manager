from flask import Flask
from flask_cors import CORS

app = Flask(
    import_name="Tomcat manager",
    static_url_path="/",
    static_folder="public",
)
CORS(app)
