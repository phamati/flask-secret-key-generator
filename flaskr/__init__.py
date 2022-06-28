import os, sys

path = os.getcwd()

if path not in sys.path:
   sys.path.insert(0, path)

from flask import Flask
from Utils import mail

import KeyGenerator

def create_app():
    
    app = Flask(__name__)
    
    #app.config.from_object('config.ProductionConfig')
    app.config.from_object('config.DevelopmentConfig')

    mail.init_app(app)


    app.register_blueprint(KeyGenerator.bp)
        
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    return app