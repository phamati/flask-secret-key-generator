import os, sys

path = os.getcwd()

if path not in sys.path:
   sys.path.insert(0, path)

from flaskr import create_app
    
if __name__ == '__main__':
    app = create_app()
    app.run()