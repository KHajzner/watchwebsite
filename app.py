# IMPORTS
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

# CONFIG
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'LongAndRandomSecretKey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class NewGenre(FlaskForm):
    name = StringField(validators=[DataRequired()])
    submit = SubmitField()


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/genres', methods=['GET', 'POST'])
def genres():
    from models import Genre
    form = NewGenre()
    genres = Genre.query.all()
    if form.validate_on_submit():
        genre = Genre.query.filter_by(name=form.name.data).first()
        if not genre:
            genre = Genre(name=form.name.data)
            db.session.add(genre)
            db.session.commit()
        return redirect(url_for('genres', genres=genres, form=form))
    return render_template('genres.html', genres=genres, form=form)


if __name__ == '__main__':

    from tvshows.views import tvshow_blueprint
    from movies.views import movies_blueprint

    app.register_blueprint(tvshow_blueprint)
    app.register_blueprint(movies_blueprint)

    app.run()
