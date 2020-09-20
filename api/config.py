import os
rootpath=os.path.abspath(os.path.dirname(__file__))
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY=os.environ.get('SECRET_KEY')
    

class Development(Config):
    SQLALCHEMY_DATABASE_URI='sqlite:///'+os.path.join(rootpath,'store.sqlite')
    DEBUG=True
    FLASK_ENV=os.environ.get('FLASK_ENV')

    
class Production(Config):
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')
    DEBUG=False
    LOG_TO_STDOUT=True
    
    
configs={'development':Development,"production":Production}
    