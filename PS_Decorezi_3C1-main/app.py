import os

from flask import Flask

from models import db


def create_app():
    app = Flask(__name__, static_folder="views", static_url_path="")
    os.makedirs(app.instance_path, exist_ok=True)
    database_path = os.path.join(app.instance_path, "decorize.db").replace(os.sep, "/")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{database_path}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    @app.get("/")
    def index():
        return app.send_static_file("index.html")

    with app.app_context():
        db.create_all()

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)