from flask import Flask, flash, redirect, render_template, request, session, url_for
from validate import RegistrationForm



app = Flask(__name__, static_url_path="", static_folder="")
app.config["SECRET_KEY"] = "perica"


user = {}



@app.route("/", methods=['GET'])
def index():
	
	return render_template("index.html", showLoginReg = True)


@app.route("/game", methods=['GET'])
def game():

	return render_template("gameColor.html", showRGB = True)


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        pass


    else:
	   return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    form = RegistrationForm(request.form)

    if request.method == "POST":

        if form.validate() == False:
            flash("bad data")
            
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




def apology(message, code=400):
    """Renders message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code
