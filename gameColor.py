from flask import Flask, flash, redirect, render_template, request, session, url_for



app = Flask(__name__, static_url_path="", static_folder="")




@app.route("/", methods=['GET'])
def index():
	
	return render_template("index.html", showLoginReg = True)


@app.route("/game", methods=['GET'])
def game():

	return render_template("gameColor.html", showRGB = True)


@app.route("/login", methods=["GET", "POST"])
def login():

	return render_template("login.html")





