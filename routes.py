from flask import Flask, render_template, redirect, request, session, url_for
from models import db, User
from forms import SignupForm, LoginForm
app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"]  = "postgresql://localhost/volunteerflask"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


app.secret_key = 'development-key'
@app.route("/")
def index():
	return render_template("index.html")


@app.route("/about")
def about():
	return redirect("http://www.orangesfoodpantry.org/about_us")


@app.route("/signup", methods = ['GET', 'POST'])
def signup():
	if 'email' in session:
		return redirect(url_for('home'))

	form = SignupForm()

	if request.method == 'POST':
		if form.validate() == False:
			return render_template('signup.html', form=form)
		else:
			newuser = User(form.first_name.data, form.last_name.data, 
						   form.email.data, form.password.data, 
						   form.address.data, form.zipcode.data, 
						   form.volunteergroup.data)
			db.session.add(newuser)
			db.session.commit()
			
			session['email'] = newuser.email

			return redirect(url_for('home'))

	elif request.method == 'GET':
		return render_template("signup.html", form=form)

@app.route('/home')
def home():
	if 'email' not in session:
		return redirect(url_for('login'))
	return render_template("home.html")


@app.route('/login', methods = ['GET', 'POST'])
def login():
	if 'email' in session:
		return url_for('home')
	form = LoginForm()

	if request.method == 'POST':
		if form.validate == False:
			return render_template("login.html" , form = form)
		else:
			email = form.email.data
			password = form.password.data

			user = User.query.filter_by(email=email).first()
			if user is not None and user.check_password(password):
				session['email'] = form.email.data
				return redirect(url_for('home'))
			else:
				return redirect(url_for('login'))

	elif request.method == 'GET': 
		return render_template("login.html", form= form)

@app.route('/logout')
def logout():
	session.pop('email', None)
	return redirect(url_for('index'))
if __name__ == '__main__':
	app.run(debug=True)