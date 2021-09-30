from flask import send_from_directory, request, Response

import app_config

app = app_config.app


@app.route('/')
def index():
    return send_from_directory(app.static_folder, "index.html")


@app.route("/api/users", methods=["GET"])
@app.route("/api/users/<username>", methods=["PUT", "DELETE"])
def users(username=""):
    response = Response()

    if request.method == "GET":
        print("Listing request...")
        response.status = 200
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
