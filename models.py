from app import db

class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, unique=True)
    startYear = db.Column(db.Integer, nullable=False)
    endYear = db.Column(db.Integer, nullable=True)

    def __init__(self, title, startYear, endYear):
        self.title = title
        self.password = startYear
        self.endYear = endYear

def init_db():
    db.drop_all()
    db.create_all()