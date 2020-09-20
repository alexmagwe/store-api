import os
rootpath=os.path.abspath(os.path.dirname(__file__))
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY=os.environ.get('SECRET_KEY')

class Development(Config):
    SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(rootpath,'store.sqlite')
    DEBUG=True
    
class Production(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')
    FLASK_ENV='production'
    
    
configs={'development':Development,"production":Production}
    