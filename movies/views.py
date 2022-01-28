import copy

from flask import Blueprint, render_template, flash, redirect, url_for

import movies.forms
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
    return render_template('movies.html', watching=watching, toWatch=toWatch, completed=completed,
                       abandoned=abandoned)


@movies_blueprint.route('/<int:id>/update', methods=['GET', 'POST'])
def update_movie(id):
    form = EditMovie()
    movie = Movie.query.filter_by(id=id).first()
    if form.validate_on_submit():
        Movie.query.filter_by(id=id).update({"title": form.title.data})
        Movie.query.filter_by(id=id).update({"startYear": form.startYear.data})
        Movie.query.filter_by(id=id).update({"runtime": form.runtime.data})
        Movie.query.filter_by(id=id).update({"watchStatus": form.watchStatus.data})
        Movie.query.filter_by(id=id).update({"ageRestriction": form.ageRestriction.data})
        Movie.query.filter_by(id=id).update({"rating": form.rating.data})
        # Movie.query.fitter_by(id=id).update({"genre": form.genres.data})

        db.session.commit()
        return movies()
    movie_copy = copy.deepcopy(movie)

    form.title.data = movie_copy.title
    form.startYear.data = movie_copy.startYear
    form.runtime.data = movie_copy.runtime
    form.watchStatus.data = movie_copy.watchStatus
    form.ageRestriction.data = movie_copy.ageRestriction
    form.rating.data = movie_copy.rating
    return render_template('update_movie.html', form=form)


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