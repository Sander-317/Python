from flask import Flask, render_template, redirect, url_for

__winc_id__ = "9263bbfddbeb4a0397de231a1e33240a"
__human_name__ = "templates"

app = Flask(__name__)

test_list = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    0,
]


@app.route("/")
def index():
    return render_template("index.html", title="Index")
    # return "This is an empty Flask project that you need to work on."


@app.route("/home")
def home():
    # return redirect("http://localhost/", code=302)
    # return redirect("/", code=302)
    return redirect("http://127.0.0.1:8001/", code=302)
    # redirect(url_for("http://127.0.0.1:8001/"), code=302)


@app.route("/about")
def about():
    return render_template(
        "about.html",
        title="About",
    )
    # return render_template("base.html", title="About", content="about.html")
    # return render_template("base.html", title="About")


@app.route("/test_page")
def test_page():
    return render_template("test_page.html", title="Test_page")


# @app.route("/test_page")
# def test_page(test_list):
#     return render_template("test_page.html", title="test_page", test_list=test_list)
