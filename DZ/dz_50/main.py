import sqlite3
import os
from Fdatabase import FdataBase
from flask import Flask, render_template, url_for, g


DATABASE = "/tmp/BD1.db"
DEBUG = True
SECRET_KEY = "8349cbfbab0fc7349ecd4642d279490f72875c48"

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(DATABASE=os.path.join(app.root_path, "BD1.db"))

# from BD1.main import create_db


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


def get_db():
    if not hasattr(g, "link.db"):
        g.link_db = connect_db()
    return g.link_db


# menu = [{"name": "Главная", "url": "index"},
#         {"name": "О нас", "url": "about"},
#         {"name": "Отзывы", "url": "reviews"}]


@app.route("/")
@app.route("/index")
def index():
    db = get_db()
    dbase = FdataBase(db)
    return render_template("index.html", title="Главная", menu=dbase.get_menu())


@app.route("/about")
def about():
    db = get_db()
    dbase = FdataBase(db)
    return render_template("about.html", title="Обо мне", menu=dbase.get_menu())


@app.route("/reviews")
def reviews():
    db = get_db()
    dbase = FdataBase(db)
    return render_template("reviews.html", title="Отзывы", menu=dbase.get_menu())


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "link_db"):
        g.link_db.close()


if __name__ == '__main__':
    app.run(debug=True)
