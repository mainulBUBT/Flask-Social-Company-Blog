#Blog/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

###########################################
############## DATABASE SETUP #############
###########################################

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'Helloguys'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask_blogs'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

###########################################


###########################################
############## LOGIN CONFIGS #############
###########################################

login_manager = LoginManager()

login_manager.init_app(app)
login_manager.login_view = 'users_login'

###########################################
from Blog.core.views import core
from Blog.blog_posts.views import blog_posts
from Blog.users.views import users

app.register_blueprint(core)
app.register_blueprint(blog_posts)
app.register_blueprint(users)