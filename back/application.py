from flask import send_from_directory, request
import
import logging

import app_config
# Facades
from local_config import config
from facades.Users import Users as _Users

users = _Users(config)

# Apps
app = app_config.app


@app.route('/')
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/api/users", methods=["GET"])
@app.route("/api/users/<username>", methods=["PUT", "DELETE"])
def users(username=""):
    logging.info(f"{request.method} {request.path}")
    status_code = None
    body = ""

    if request.method == "GET":
        print("Listing request...")
        user_list = users.list()
        if user_list:
            body
    elif request.method == "PUT":
        print(f"Saving user {username} ...")
        response.status = 200
    elif request.method == "DELETE":
        print(f"Deleting user {username} ...")
        response.status = 200
    else:
        print("Unsupported methods")
        response.status = 405  # Method not allowed

    return response


if __name__ == '__main__':
    app.run()
