# set the path
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from twbiblioteca import app

if __name__ == "__main__":
    app.run()