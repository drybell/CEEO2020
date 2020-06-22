from flask import Flask
app = Flask(__name__)

@app_route("/")
def home_view():
	return ("<h1> Test Home Page </h1>")