import sqlite3
import os
from Fdatabase import FdataBase
from flask import Flask, render_template, url_for, g, flash, request, abort


DATABASE = "/tmp/BD1.db"
DEBUG = True
SECRET_KEY = "8349cbfbab0fc7349ecd4642d279490f72875c48"

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(DATABASE=os.path.join(app.root_path, "flsk.db"))

# from BD1.main import create_db
# from DZ.dz_51.main import create_db


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


@app.route("/")
@app.route("/index")
def index():
    db = get_db()
    dbase = FdataBase(db)
    return render_template("index.html", title="Каталог курсов", menu=dbase.get_menu(), posts=dbase.get_well_announce())


@app.route("/add", methods=["POST", "GET"])
def add():
    db = get_db()
    dbase = FdataBase(db)
    if request.method == "POST":
        if len(request.form["name"]) > 4 and len(request.form["post"]) > 10:
            res = dbase.add_price(request.form["name"], request.form["price"], request.form["post"])
            if not res:
                flash("Ошибка добавления курса", category="error")
            else:
                flash("Курс добавлен успешно", category="success")
        else:
            flash("Ошибка добавления курса", category="error")
    return render_template("catalog.html", title="Добавить курс", menu=dbase.get_menu())


@app.route("/information")
def info():
    db = get_db()
    dbase = FdataBase(db)
    return render_template("information.html", title="Информация", menu=dbase.get_menu())


@app.route("/well/<int:id_well>")
def show_well(id_well):
    db = get_db()
    dbase = FdataBase(db)
    title, price, txt = dbase.get_well(id_well)
    if not title:
        abort(404)

    return render_template("well.html", title=title, price=price, txt=txt, menu=dbase.get_menu())


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "link_db"):
        g.link_db.close()


if __name__ == '__main__':
    app.run(debug=True)
