from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_Name = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_Name}'
    db.init_app(app) #initializing db with app

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Answer

    with app.app_context():
        db.create_all()

    # create_databse(app)

    return app

# def create_databse(app): #check to see if database exists, if not, create it
#     if not path.exists('website/' + DB_Name):
#         db.create_all(app=app)
#         print('Created Database!')