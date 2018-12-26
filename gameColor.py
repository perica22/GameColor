from flask import Flask, flash, redirect, render_template, request, session, url_for


app = Flask(__name__)


#@app.route("/", methods=['GET'])
#def hello():
	
 #   return render_template("index.html")


@app.route("/game", methods=['GET'])
def hello():

    return render_template("gameColor.html")


#@app.route("/login", methods=["GET", "POST"])
#def login():

#	return render_template("login.html")