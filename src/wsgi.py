import logging
# """WSGI entry"""
from application import create_app

# import app
app = create_app()

if __name__ == '__main__':
    app.run()
