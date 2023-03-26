# """WSGI entry"""
from application import create_app
from ankra import get_logger

logging = get_logger()

# import app
app = create_app()

if __name__ == '__main__':
    app.run()
