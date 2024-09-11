#!/usr/bin/python3
"""The website api"""

from flask import Flask
from api.v1.views import Api_skill

app = Flask(__name__)
app.register_blueprint(Api_skill)

if __name__ == '__main__':
    """To run  the app instance"""

    app.run(host='0.0.0.0', port='5000', threaded=True)
