from flask import send_from_directory, request, jsonify
import logging

import app_config
# Facades
from local_config import config
from facades import Users

users_facade = Users(config)


# Apps
app = app_config.app


@app.route('/')
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/api/users", methods=["GET"])
@app.route("/api/users/<username>", methods=["PUT", "DELETE"])
def users(username=""):
    logging.info(f"{request.method} {request.path}")
    body_obj = {}

    if request.method == "GET":
        print("Listing request...")
        user_list = users_facade.list()
        if isinstance(user_list, list):
            status_code = 200
            body_obj = list(map(lambda user: user.serialize(), user_list))
        else:
            status_code = 500
            body_obj = {
                "message": "Listing user failed"
            }
    elif request.method == "PUT":
        print(f"Saving user {username} ...")
        status_code = 200
    elif request.method == "DELETE":
        print(f"Deleting user {username} ...")
        status_code = 200
    else:
        print("Unsupported methods")
        status_code = 405  # Method not allowed

    return jsonify(body_obj), status_code


if __name__ == '__main__':
    app.run()
