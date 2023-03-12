from flask import Flask, render_template, url_for

app = Flask(__name__)

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
