from flask import Flask, send_from_directory

app = Flask(
    import_name="Tomcat manager",
    static_url_path="/",
    static_folder="public"
)


@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
