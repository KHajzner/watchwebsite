from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired


class NewMovieForm(FlaskForm):
    title = StringField(validators=[DataRequired()])
    startYear = IntegerField()
    runtime = IntegerField()
    watchStatus = SelectField(u'Status', choices=['Plan to watch', 'Watching', 'Completed', 'Abandoned'], default="Plan to watch")
    ageRestriction = SelectField(u'Restrictions', choices=['G', 'PG-13', 'R', 'NC-17'])
    rating = IntegerField()
    submit = SubmitField()

