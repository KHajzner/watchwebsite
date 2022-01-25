from flask import Blueprint, render_template

from models import Movie

movies_blueprint = Blueprint("movies", __name__, template_folder="templates")


@movies_blueprint.route('/movies', methods=['GET', 'POST'])
def movies():
    watching = Movie.query.filter_by(watchStatus="Watching").all()
    toWatch = Movie.query.filter_by(watchStatus="Plan to watch").all()
    completed = Movie.query.filter_by(watchStatus="Completed").all()
    abandoned = Movie.query.filter_by(watchStatus="Abandoned").all()

    return render_template('movies.html', watching=watching, toWatch=toWatch, completed=completed, abandoned=abandoned)

