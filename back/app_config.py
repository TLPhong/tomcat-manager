from flask import Flask
from flask_cors import CORS
from local_config import config

app = Flask(
    import_name="Tomcat manager",
    static_url_path="/",
    static_folder="public",
)

cors = config["Server"]["cors"]  # Can be list string or regex
CORS(app, resources={r"/api/*": {"origins": cors}})
