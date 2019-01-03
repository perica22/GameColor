from flask import flash, redirect, render_template, request, url_for, session
from flask_login import current_user, login_user, logout_user, login_required

from app import app
from app.validate import LoginForm, RegistrationForm
from app import db
from app.models import User



@app.route("/", methods=['GET'])
def index():
	
	return render_template("index.html", showLoginReg = True)


@app.route("/game", methods=['GET'])
@login_required
def game():

	return render_template("gameColor.html", showRGB = True)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('game'))

    form = LoginForm()

    if request.method == "POST":

        if form.validate() == False:
            #flash("bad data")
            return render_template("login.html", form=form)
        else:
            user = User.query.filter_by(username=form.username.data).first()

        if not user or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        else:
            login_user(user)
            next_page = request.args.get('next')
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('game')
            print(next_page)
            return redirect(next_page)
        #return redirect(url_for("game"))

    else:
        return render_template("login.html", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():

    if current_user.is_authenticated:
        return redirect(url_for('game'))

    form = RegistrationForm()

    
    if request.method == "POST":

        if form.validate_on_submit():
            
            print("creating")
            
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            db.session.add(user)
            print(user)
            db.session.commit()
            
            return redirect(url_for("login"))

        else:
            return render_template("register.html", form=form)


    else:
       return render_template("register.html", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
'''
TODO

Finins register functions

1. database
2. login requered wraper
3. index page - between login and game page
4. score tracker
5. options on index page (use some navbars and similar from bootstrapdev) - option to change personal info
6. statistics page
'''
