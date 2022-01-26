from flask import Blueprint, render_template, flash, redirect, url_for

from app import db
from models import Movie, TVShow
from tvshows.forms import NewTVShowForm

tvshow_blueprint = Blueprint('tvshows', __name__, template_folder='templates')


@tvshow_blueprint.route('/tvshows', methods=['GET', 'POST'])
def tvshows():
    watching = TVShow.query.filter_by(watchStatus="Watching").all()
    toWatch = TVShow.query.filter_by(watchStatus="Plan to watch").all()
    completed = TVShow.query.filter_by(watchStatus="Completed").all()
    abandoned = TVShow.query.filter_by(watchStatus="Abandoned").all()

    return render_template('tvshows.html', watching=watching, toWatch=toWatch, completed=completed, abandoned=abandoned)


@tvshow_blueprint.route('/new_tvshow', methods=['GET', 'POST'])
def add_tvshow():

    newTVShow = NewTVShowForm()

    if newTVShow.validate_on_submit():

        tvshow = TVShow.query.filter_by(title=newTVShow.title.data).first()

#TODO: flash message doesn't work
        if tvshow:
            flash('Movie already exists')
            return render_template("newTVShow.html", newTVShows=newTVShow, form2=newTVShow)

        new_tvshow = TVShow(title=newTVShow.title.data,
                           startYear=newTVShow.startYear.data,
                           endYear=newTVShow.endYear.data,
                           seasons=newTVShow.seasons.data,
                           episodes=newTVShow.episodes.data,
                           watchStatus=newTVShow.watchStatus.data,
                           ageRestriction=newTVShow.ageRestriction.data,
                           rating=newTVShow.rating.data
                           )
        db.session.add(new_tvshow)
        db.session.commit()

        return redirect(url_for("tvshows.tvshows"))
    return render_template('newTVShow.html', form2=newTVShow)
