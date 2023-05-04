from flask import Flask, request, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy.sql import func

# Instantiate Flask Application
app = Flask(__name__)

# Connect Application with SQLAlchemy Database
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100))
    bio = db.Column(db.Text)
    create_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return '<User %r>' % self.username

class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text)
    author_id = db.Column(db.Integer) # foreign key to user.user_id
    category_id = db.Column(db.Integer) #foreing key to category.category_id
    # published_at = db.Column()
    create_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

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


# TODO: Modularize routes into routes.py
# from app import routes
@app.route("/")
def index():
    users = User.query.all()
    return render_template("index.html", users=users)

@app.route("/admin", methods=("GET", "POST", "DELETE"))
def admin():
    users = User.query.all()
    # if admin clicks delete user
        # user should be deleted from database
    return render_template("admin.html", users=users)

@app.route("/<int:user_id>/")
def user(user_id):
    user = User.query.get_or_404(user_id)
    return render_template("user.html", user=user)

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/create", methods=("GET", "POST"))
def create():
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
