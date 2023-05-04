import os
from flask import Flask, request, url_for, redirect, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user


# Instantiate Flask Application
app = Flask(__name__)

# Connect Application with SQLAlchemy Database
basedir = os.path.abspath(os.path.dirname(__file__))

# Login Manager contains code that lets application and Flask-Login work together
# login_manager = LoginManager()
# Configure it to app
# login_manager.init_app(app)

# TODO: CHANGE SECRET KEY AND KEEP IT VERY SECRET!!!
# secret key used for Flask-Login sessions
app.config['SECRET_KEY'] = "secret-key-really-secret"
# sets config variable to sqlite base directory
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
# disables an unnecessary feature of SQLAlchemy that tracks modifications to objects and generates warnings
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
    

class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100))
    bio = db.Column(db.Text)
    create_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return '<User %r>' % self.username

    @property
    def is_authenticated(self):
        return True
    
    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.user_id)

class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text)
    author_id = db.Column(db.Integer) # foreign key to user.user_id
    category_id = db.Column(db.Integer) # foreign key to category.category_id
    create_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

class Comment(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer) # foreign key to user.user_id
    content = db.Column(db.Text)
    post_id = db.Column(db.Integer) # foreign key to post.post_id
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())


# User(username="user1", email="user1@gmail.com", password="password1", bio="check this bio")
# User(username="user2", email="user2@gmail.com", password="password2", bio="insert bio here")
# User(username="user3", email="user3@gmail.com", password="password3", bio="heres anotha one")
# User(username="user4", email="user4@gmail.com", password="password4", bio="bio 4")
# User(username="user5", email="user5@gmail.com", password="password5", bio="what up bitches")

# Create login manager to handle authentication and session management
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# TODO: Modularize routes into routes.py # from app import routes

@app.route("/")
def index():
    # If logged in, pass in user to render_template function
    return render_template("index.html")

@app.route("/delete_user/<int:user_id>", methods=["POST"])
def delete_user(user_id):
    if request.method == "POST":
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('index'))
    # users = User.query.all()
    # return render_template("admin.html", users=users)

@app.route("/<int:user_id>/")
def user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("user.html", user=user)


@app.route("/create", methods=("GET", "POST"))
def create():
    # if submitted a create user request, create user and return to home
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        bio = request.form['bio']
        user = User(username=username, email=email, password=password, bio=bio)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template("create.html")

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            login_user(user, remember=True)
            return redirect(url_for('index'))
        # else:
        #     flash("Invalid username or password.")
    return render_template("login.html")

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))

# admin is used to create users, delete users, edit user info, delete user posts, delete user post comments
@app.route("/admin")
def admin():
    users = User.query.all()
    return render_template("admin.html", users=users)
