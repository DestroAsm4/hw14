import sqlite3
from flask import Flask
from main.views import main

app = Flask('__name__')

app.config['JSON_AS_ASCII'] = False


app.register_blueprint(main)

if __name__ == '__main__':
    app.run(debug=True)