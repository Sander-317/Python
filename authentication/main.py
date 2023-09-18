import os

from flask import Flask, redirect, render_template, request, session, url_for
from helpers import get_users, hash_password

__winc_id__ = "8fd255f5fe5e40dcb1995184eaa26116"
__human_name__ = "authentication"

app = Flask(__name__)

app.secret_key = os.urandom(16)


@app.route("/home")
def redirect_index():
    return redirect(url_for("index"))


@app.route("/")
def index():
    return render_template("index.html", title="Index")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/lon")
def lon():
    return render_template("lon.html", title="League of Nations")


@app.route("/login", methods=["GET", "POST"])
def login():
    # YOUR SOLUTION HERE
    error = request.args.get("error", default="False")

    if error == True:
        return render_template("login.html", title="login", error=True)

    if request.method == "POST":
        if (
            request.form["username"] in get_users()
            and hash_password(request.form["password"])
            == get_users()[request.form["username"]]
        ):
            session["username"] = request.form["username"]
            session["logged_in"] = True

            return redirect(
                url_for(
                    "dashboard",
                )
            )

        else:
            return render_template("login.html", title="login", error=True)

    else:
        return render_template("login.html", title="login", error=False)


@app.route("/dashboard")
def dashboard():
    # YOUR SOLUTION HERE
    if session == {}:
        return render_template("access_denied.html", title="Access Denied")
    else:
        return render_template(
            "dashboard.html", title="Dashboard", username=session.get("username")
        )


@app.route("/logout", methods=["GET", "POST"])
def logout():
    # YOUR SOLUTION HERE
    session.pop("username", None)
    session.pop("logged_in", None)
    return redirect(url_for("index"))
