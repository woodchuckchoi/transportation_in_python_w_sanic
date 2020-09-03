# custom
from be.app import app

if __name__ == '__main__':
    app.run(app.config.SERVERHOST, app.config.SERVERPORT)