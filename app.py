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

@app.route('/search')
def search():  # put application's code here
    return render_template('search.html')


if __name__ == '__main__':

    from tvshows.views import tvshow_blueprint
    from movies.views import movies_blueprint

    app.register_blueprint(tvshow_blueprint)
    app.register_blueprint(movies_blueprint)

    app.run()
