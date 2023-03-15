from flask import Flask, render_template, url_for
import sqlite3
import os

DATABASE = "/tmp/flsk.db"
DEBUG = True
SECRET_KEY = "8349cbfbab0fc7349ecd4642d279490f72875c48"

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(DATABASE=os.path.join(app.root_path, "flsk.db"))

# from dz.main import create_db


def connect_db():
    con = sqlite3.connect(app.config["DATABASE"])
    con.row_factory = sqlite3.Row
    return con


def create_db():
    db = connect_db()
    with app.open_resource("sq_db.sql", "r") as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


menu = [{"name": "Главная", "url": "index"},
        {"name": "О нас", "url": "about"},
        {"name": "Отзывы", "url": "reviews"}]


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Главная", menu=menu)


@app.route("/about")
def about():
    return render_template("about.html", title="Обо мне", menu=menu)


@app.route("/reviews")
def reviews():
    return render_template("reviews.html", title="Отзывы", menu=menu)


if __name__ == '__main__':
    app.run(debug=True)
