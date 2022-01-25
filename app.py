# IMPORTS
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

# CONFIG
app = Flask(__name__)
app.config['SECRET_KEY'] = 'LongAndRandomSecretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/movies')
def movies():  # put application's code here
    return render_template('movies.html')

@app.route('/tvshows')
def tvshows():  # put application's code here
    return render_template('tvshows.html')

@app.route('/search')
def search():  # put application's code here
    return render_template('search.html')


if __name__ == '__main__':

    from add.views import add_blueprint

    app.register_blueprint(add_blueprint)

    app.run()
