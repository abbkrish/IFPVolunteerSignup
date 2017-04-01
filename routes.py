from flask import Flask, render_template, redirect


app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")


@app.route("/about")
def about():
	return redirect("http://www.orangesfoodpantry.org/about_us")


@app.route("/signup")
def signup():
	return render_template("signup.html")

if __name__ == '__main__':
	app.run(debug=True)