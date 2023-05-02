from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from sqlalchemy.sql import func
from flask import render_template

# Instantiate Flask Application
app = Flask(__name__)

# Connect Application with SQLAlchemy Database
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class user(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100))
    bio = db.Column(db.Text)
    create_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return '<User %r>' % self.username

class post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text)
    author_id = db.Column(db.Integer) # foreign key to user.user_id
    category_id = db.Column(db.Integer) #foreing key to category.category_id
    # published_at = db.Column()
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

class category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())

class comment(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer) # foreign key to user.user_id
    content = db.Column(db.Text)
    post_id = db.Column(db.Integer) # foreign key to post.post_id
    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())


# TODO: Modularize routes into routes.py
# from app import routes
@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/about")
def what_up():
    return render_template("about.html")

@app.route("/login")
def login():
    return render_template('login.html')