# -*- coding: utf-8 -*-
from app import app
from livereload import Server


if __name__ == '__main__':

    app.debug = True

    server = Server(app.wsgi_app)
    # server.serve(port=5501, debug=True)
    server.serve(port=35729, debug=True)
    # server.serve(port=35729, debug=True)
