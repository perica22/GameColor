from flask import flash, redirect, render_template, request, url_for, session
from flask_login import current_user, login_user

from app import app
from app.validate import LoginForm, RegistrationForm
from app import db
from app.models import User



@app.route("/", methods=['GET'])
def index():
	
	return render_template("index.html", showLoginReg = True)


@app.route("/game", methods=['GET'])
def game():

	return render_template("gameColor.html", showRGB = True)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('game'))

    form = LoginForm(request.form)

    if request.method == "POST":
    
        if form.validate() == False:
            #flash("bad data")
            return render_template("login.html", form=form)
        else:            
            user = User.query.filter_by(username=form.username.data).first()
           
            print(user.check_password(form.password.data))

            if user.username == None or user.check_password(form.password.data) == False:
                flash('Invalid username or password')
                return redirect(url_for('login'))
                

            else:
                return redirect(url_for("game"))

    else:
        return render_template("login.html", form=form)

    

@app.route("/register", methods=["GET", "POST"])
def register():

    form = RegistrationForm(request.form)

    if request.method == "POST":

        if form.validate() == False:
            #flash("bad data")
            
            return render_template("register.html", form=form)

        else:

            #user = {"name":"", "email": ""...}
            username = request.form.get("username")
            email = request.form.get("email")
            password = request.form.get("password")

            user["name"] = username
            user["email"] = email
            user["password"] = password

            return redirect(url_for("game"))

    else:
        return render_template("register.html", form=form)


'''
TODO
1. database
2. login requered wraper
3. index page - between login and game page
4. score tracker
5. options on index page (use some navbars and similar from bootstrapdev) - option to change personal info
6. statistics page
'''
