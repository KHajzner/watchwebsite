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


class DeleteGenre(FlaskForm):
    name2 = StringField(validators=[DataRequired()])
    submit2 = SubmitField()


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/genres', methods=['GET', 'POST'])
def genres():
    from models import Genre
    form = NewGenre()

    form2 = DeleteGenre()
    genres = Genre.query.all()
    if form.submit.data and form.validate():
        genre = Genre.query.filter_by(name=form.name.data).first()
        if not genre:
            genre = Genre(name=form.name.data)
            db.session.add(genre)
            db.session.commit()
        return redirect(url_for('genres', genres=genres, form=form, form2=form2))

    # TODO: genre deletion doesn't commit to the database
    if form2.submit2.data and form2.validate():
        Genre.query.filter_by(name=form2.name2.data).delete()
        db.session.commit()
        return redirect(url_for('genres', genres=genres, form=form, form2=form2))

    return render_template('genres.html', genres=genres, form=form, form2=form2)


if __name__ == '__main__':
    from tvshows.views import tvshow_blueprint
    from movies.views import movies_blueprint

    app.register_blueprint(tvshow_blueprint)
    app.register_blueprint(movies_blueprint)

    app.run()
