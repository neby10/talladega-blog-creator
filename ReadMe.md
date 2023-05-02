Name: Nick Eby
Created: May 2, 2023

# Project Name: Python Flask Blog

## Description:
This is a fully functional blog web application using Flask.
The application allows users to create an account, log in, create, edit, and delete blog posts, and view posts from other users.
I will also implemented features such as pagination, search, and authentication with password hashing.

## Skills Learned:

Flask web framework
Python web development
SQL database (SQLite or PostgreSQL) and ORM (SQLAlchemy)
User authentication and authorization
Password hashing and security best practices
HTML, CSS, and Bootstrap for front-end development

## Estimate Time:
55 hours



A Python interactive shell will be opened. This special shell runs commands in the context of your Flask application, so that the Flask-SQLAlchemy functions you’ll call are connected to your application.
$ flask shell
>>> from app import db, User, Post, Category, Comment
>>> db.create_all()



Requirements
-Admin
    -Post, Edit, Delete Content on a User's Page
    -Access All Items in Admin Toolbar
    -Control Site-wide Settings
-Users
    -Create Account
    -Log In
    -Post log content
    -Edit Blog Content
    -Delete Blog Content
    -View Other User's Posts

Features: pagination, search, authentication

Action Plan:

1. Set up the Flask environment and create the project structure.
Install Flask and required packages using pip
Create a new Flask application with a basic file structure
Test the Flask app by running it and verifying that it works
2. Design and create the database schema
Decide on the database schema and relationships between tables
Implement the schema using SQLAlchemy ORM
Test the database by creating, reading, updating, and deleting data
3. Implement user authentication and authorization
Create a user model and views for registration, login, and logout
Add password hashing using Werkzeug security
Implement authentication and authorization using Flask-Login
4. Build the blog functionality
Create the blog post model and views for creating, editing, deleting, and viewing posts
Implement pagination and search functionality
Create a template for displaying posts and their details
5. Add styling and front-end functionality
Use HTML, CSS, and Bootstrap to style and format the website
Add features such as forms, buttons, and modals to improve user experience
6. Test and deploy the application
Test the application thoroughly to ensure it works correctly and securely
Deploy the application to a hosting platform such as Heroku or AWS
Monitor the application and fix any issues that arise
7. Add additional features (optional)
Allow users to upload images to their posts
Implement comments and likes functionality
Add support for multiple users roles (admin, moderator, etc.)

Python, Flask, skills in SQL databases, user authentication and authorization, front-end development, and deploying web applications