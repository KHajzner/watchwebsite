from app import db


def init_db():
    db.drop_all()
    db.create_all()


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    startYear = db.Column(db.Integer, nullable=False)
    runtime = db.Column(db.Integer)
    watchStatus = db.Column(db.String(100))
    ageRestriction = db.Column(db.Integer)
    rating = db.Column(db.Integer)

    def __init__(self, title, startYear, runtime, watchStatus, ageRestriction, rating):
        self.title = title
        self.startYear = startYear
        self.runtime = runtime
        self.watchStatus = watchStatus
        self.ageRestriction = ageRestriction
        self.rating = rating


class TVShow(db.Model):
    __tablename__ = 'tvshows'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    startYear = db.Column(db.Integer, nullable=False)
    endYear = db.Column(db.Integer, nullable=True)
    current_season = db.Column(db.Integer)
    seasons = db.Column(db.Integer)
    current_episode = db.Column(db.Integer)
    episodes = db.Column(db.Integer)
    watchStatus = db.Column(db.String(100))
    ageRestriction = db.Column(db.Integer)
    rating = db.Column(db.Integer)

    def __init__(self, title, startYear, endYear, current_episode, current_season, seasons, episodes, watchStatus, ageRestriction, rating):
        self.title = title
        self.startYear = startYear
        self.endYear = endYear
        self.seasons = seasons
        self.episodes = episodes
        self.current_episode = current_episode
        self.current_season = current_season
        self.watchStatus = watchStatus
        self.ageRestriction = ageRestriction
        self.rating = rating


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)


movieGenres = db.Table('movieGenres',

                       db.Column('genre_id', db.Integer, db.ForeignKey(Genre.id), primary_key=True),
                       db.Column('movie_id', db.Integer, db.ForeignKey(Movie.id), primary_key=True)
                       )

tvShowsGenres = db.Table('tvShowGenres',
                         db.Column('genre_id', db.Integer, db.ForeignKey(Genre.id), primary_key=True),
                         db.Column('tvshow_id', db.Integer, db.ForeignKey(TVShow.id), primary_key=True)
                         )
