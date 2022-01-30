import copy

from flask import Blueprint, render_template, flash, redirect, url_for

from app import db
from models import Movie, TVShow, Genre
from tvshows.forms import NewTVShowForm, EditTVShowForm

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

    newTVShow = EditTVShowForm()

    if newTVShow.validate_on_submit():

        tvshow = TVShow.query.filter_by(title=newTVShow.title.data).first()

# TODO: flash message doesn't work
        if tvshow:
            flash('Movie already exists')
            return render_template("newTVShow.html", newTVShows=newTVShow, form2=newTVShow)

        new_tvshow = TVShow(title=newTVShow.title.data,
                            startYear=newTVShow.startYear.data,
                            endYear=newTVShow.endYear.data,
                            current_episode=newTVShow.current_episode.data,
                            current_season=newTVShow.current_season.data,
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


@tvshow_blueprint.route('/<int:id>/tv_update', methods=['GET', 'POST'])
def update_tvshow(id):
    form = EditTVShowForm()
    tvshow = TVShow.query.filter_by(id=id).first()
    if form.validate_on_submit():
        TVShow.query.filter_by(id=id).update({"title": form.title.data})
        TVShow.query.filter_by(id=id).update({"startYear": form.startYear.data})
        TVShow.query.filter_by(id=id).update({"endYear": form.endYear.data})
        TVShow.query.filter_by(id=id).update({"current_episode": form.current_episode.data})
        TVShow.query.filter_by(id=id).update({"episodes": form.episodes.data})
        TVShow.query.filter_by(id=id).update({"current_season": form.current_season.data})
        TVShow.query.filter_by(id=id).update({"seasons": form.seasons.data})
        TVShow.query.filter_by(id=id).update({"watchStatus": form.watchStatus.data})
        TVShow.query.filter_by(id=id).update({"ageRestriction": form.ageRestriction.data})
        TVShow.query.filter_by(id=id).update({"rating": form.rating.data})

        return tvshows()

    tvshow_copy = copy.deepcopy(tvshow)

    form.title.data = tvshow_copy.title
    form.startYear.data = tvshow_copy.startYear
    form.current_episode.data = tvshow_copy.current_episode
    form.episodes.data = tvshow_copy.episodes
    form.current_season.data = tvshow_copy.current_season
    form.seasons.data = tvshow_copy.seasons
    form.watchStatus.data = tvshow_copy.watchStatus
    form.ageRestriction.data = tvshow_copy.ageRestriction
    form.rating.data = tvshow_copy.rating
    return render_template('update_tvshow.html', form=form)

