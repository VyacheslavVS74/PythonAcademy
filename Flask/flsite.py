import sqlite3
import os
from flask import Flask, render_template, url_for, request, flash, session, redirect, abort, g
from FDateBase import FDateBase


# конфигурация
DATABASE = "/tmp/flsk.db"
DEBUG = True
SECRET_KEY = "229916f901f0846a3273ea6008136f2b32e8df5c"

app = Flask(__name__)
# app.config['SECRET_KEY'] = "ssdfsdgfdgjkdjfhg734587567348ghbnfdjhg3874gdfskl"
app.config.from_object(__name__)

app.config.update(DATABASE=os.path.join(app.root_path, "flsk.db"))


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
    if not hasattr(g, "link_db"):
        g.link_db = connect_db()
    return g.link_db


menu = [{"name": "Главная", "url": "index"},
        {"name": "О нас", "url": "about"},
        {"name": "Обратная связь", "url": "contact"}
        ]


@app.route("/")
@app.route("/index")
def index():
    db = get_db()
    dbase = FDateBase(db)
    # print(url_for('index'))
    return render_template("index.html", title="Главная", menu=dbase.get_menu(), posts=dbase.get_posts_announce())


@app.route("/add_post", methods=["POST", "GET"])
def add_post():
    db = get_db()
    dbase = FDateBase(db)
    if request.method == "POST":
        if len(request.form["name"]) > 4 and len(request.form["post"]) > 10:
            res = dbase.add_post(request.form["name"], request.form["post"])
            if not res:
                flash("Ошибка добавления статьи", category="error")
            else:
                flash("Статья добавлена успешно", category="success")
        else:
            flash("Ошибка добавления статьи", category="error")

    return render_template("add_post.html", title="Добавление статьи", menu=dbase.get_menu())


@app.route("/post/<int:id_post>")
def show_post(id_post):
    db = get_db()
    dbase = FDateBase(db)
    title, post = dbase.get_post(id_post)
    if not title:
        abort(404)

    return render_template("post.html", title=title, post=post, menu=dbase.get_menu())


@app.route("/about")
def about():
    print(url_for('about'))
    return render_template('about.html', title="О нас", menu=menu)


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        if len(request.form["username"]) > 2:
            flash("Сообщение отправлено успешно!", category='success')
        else:
            flash("Ошибка отправки!", category='error')

        # context = {
        #     "username": request.form["username"],
        #     "email": request.form["email"],
        #     "message": request.form["message"]
        # }
        return render_template("contact.html", title="Обратная связь", menu=menu)  # **context,
        # print(request.form["username"])
        # print(request.form)
    return render_template("contact.html", title="Обратная связь", menu=menu)


@app.route("/profile/<username>")  # int, float, path - можно использовать /
def profile(username):
    if "userLogged" not in session or session["userLogged"] != username:
        abort(401)
    return f"Пользователь: {username}"


@app.route("/login", methods=["POST", "GET"])
def login():
    if "userLogged" in session:
        return redirect(url_for("profile", username=session["userLogged"]))
    elif request.method == "POST" and request.form["username"] == "admin" and request.form["psw"] == "123456":
        session["userLogged"] = request.form["username"]
        return redirect(url_for("profile", username=session["userLogged"]))
    return render_template("login.html", title="Авторизация", menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("page404.html", title="Страница не найдена", menu=menu)


@app.teardown_appcontext
def close_db(error):
    if hasattr(g, "link_db"):
        g.link_db.close()


if __name__ == "__main__":
    app.run(debug=True)

# 09.03.2023 ========================================================

#  flash()  импортировать
# get_flashed_messages()

# import os
# os.urandom(20).hex()

# from Flask.flsite import create_db
