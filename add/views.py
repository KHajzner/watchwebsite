from flask import Blueprint, render_template, flash, redirect, url_for

from add.forms import NewMovieForm
from app import db
from models import Movie

add_blueprint = Blueprint('add', __name__, template_folder='templates')


@add_blueprint.route('/add', methods=['GET', 'POST'])
def add():
    newMovie = NewMovieForm()
    if newMovie.validate_on_submit():
        movie = Movie.query.filter_by(title=newMovie.title.data).first()

        if movie:
            flash('Movie already exists')
            return render_template("add.html", newMovie=newMovie)

        new_movie = Movie(title=newMovie.title.data,
                          startYear=newMovie.startYear.data,
                          runtime=newMovie.startYear.data,
                          watchStatus=newMovie.watchStatus.data,
                          ageRestriction=newMovie.ageRestriction.data,
                          rating=newMovie.rating.data
                          )
        db.session.add(new_movie)
        db.session.commit()

        return redirect(url_for("movies"))
    return render_template('add.html', form=newMovie)
