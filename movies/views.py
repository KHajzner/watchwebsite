from flask import Blueprint, render_template, flash, redirect, url_for

from app import db
from models import Movie
from movies.forms import NewMovieForm, EditMovie

movies_blueprint = Blueprint("movies", __name__, template_folder="templates")


@movies_blueprint.route('/movies', methods=['GET', 'POST'])
def movies():
    watching = Movie.query.filter_by(watchStatus="Watching").all()
    toWatch = Movie.query.filter_by(watchStatus="Plan to watch").all()
    completed = Movie.query.filter_by(watchStatus="Completed").all()
    abandoned = Movie.query.filter_by(watchStatus="Abandoned").all()
    form = EditMovie()
    return render_template('movies.html', form=form, watching=watching, toWatch=toWatch, completed=completed, abandoned=abandoned)


@movies_blueprint.route('/new_movie', methods=['GET', 'POST'])
def add_movie():
    newMovie = NewMovieForm()
    if newMovie.validate_on_submit():
        movie = Movie.query.filter_by(title=newMovie.title.data).first()

        if movie:
            flash('Movie already exists')
            return render_template("newMovie.html", newMovie=newMovie, form=newMovie)

        new_movie = Movie(title=newMovie.title.data,
                          startYear=newMovie.startYear.data,
                          runtime=newMovie.startYear.data,
                          watchStatus=newMovie.watchStatus.data,
                          ageRestriction=newMovie.ageRestriction.data,
                          rating=newMovie.rating.data
                          )
        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for("movies.movies"))
    return render_template('newMovie.html', form=newMovie)