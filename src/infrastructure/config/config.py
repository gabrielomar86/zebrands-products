class Config:
    SECRET_KEY = 'SUPER SECRET KEY'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test2.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    
    FLASK_APP='zebrand_product.py'
    FLASK_DEBUG=1
    FLASK_ENV='development'