from flask import render_template, request, redirect, url_for, session, make_response
from . import app
from datetime import timedelta

@app.route('/')   # URL '/' to be handled by main() route handler
def index():
    return "index page"


@app.route("/login",  methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form["login"]
        session["username"] = username
        return redirect(url_for("get_profile"))
    # else:
    #     if "username" in session:
    #         return redirect(url_for("get_profile")) 
    return render_template("login.html")


@app.route("/profile")
def get_profile():
    if "username" in session:
        username_value = session["username"]
        return render_template("profile.html", username=username_value)
    return redirect(url_for("login"))



@app.route('/logout')
def logout():
    # Видалення користувача із сесії
    session.pop('username', None)
    return redirect(url_for('index'))



