from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask import Flask
from flask_migrate import Migrate
from .config import configs
db=SQLAlchemy()
migrate=Migrate()
cors=CORS()
def create_app(env='development'):
    app=Flask(__name__)
    app.config.from_object(configs[env])
    migrate.init_app(app,db)
    db.init_app(app)
    cors.init_app(app)
    from .products import products
    app.register_blueprint(products,url_prefix='/products')
    return app
    
