from flask import render_template, request, redirect, url_for, session, make_response
from . import app
from datetime import timedelta

@app.route("/login",  methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form["login"]
        session["username"] = username
        return redirect(url_for("get_profile"))
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



@app.route('/set_cookie')
def set_cookie():
    response = make_response('Кука встановлена')
    response.set_cookie('username', 'student', max_age=timedelta(seconds=60))
    response.set_cookie('color', '', max_age=timedelta(seconds=60))
    return response

@app.route('/get_cookie')
def get_cookie():
    username = request.cookies.get('username')
    return f'Користувач: {username}'

@app.route('/delete_cookie')
def delete_cookie():
    response = make_response('Кука видалена')
    #response.set_cookie('username', '', expires=0) # response.set_cookie('username', '', max_age=0)
    response.delete_cookie('color')
    return response




@app.route('/')   # URL '/' to be handled by main() route handler
def index():
    return "indesx page"


@app.route('/homepage') 
def home():
    """View for the Home page of your website."""
    user_agent = str(request.user_agent)[:10]
    return render_template("home.html", 
                           agent=user_agent)

@app.route('/hi/')
@app.route('/hi/<string:name>')  # /hi/ivan?age=30
def greetings(name=None):
    if  name is None:
        name = ""
    name = name.upper()
    age = request.args.get("age", 0, type=int)

    return render_template("hi.html", 
                           name=name,
                           age=age)



@app.route('/admin')
def admin():
    to_url = url_for("greetings", name="administrator", _external=True)    # --> "http://localhost:8080/hi/administrator"
    print(to_url)
    return redirect(to_url)