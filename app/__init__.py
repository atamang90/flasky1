from flask import Flask
# Translator from Flask to SQL
from flask sqlachechemy import SQLAlchemy

from flask migrate import Migrate

def create_app():
    # __name__ stores the name of the module we're in
    app = Flask(__name__)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/flasky_development'

    # Creating our Database through our Instance of SQLAlchemy
    # Create Instances of Imports
    # Give us access to the database operations

    db = SQLAchemy()

    #Migrations Representations

    migrate = Migrate()
    # Coonects db to migrate to our Flask app
    db.init_app(app)
    migrate.init_app(app,db)

    from .routes.dogs import dogs_bp
    app.register_blueprint(dogs_bp)

    return app