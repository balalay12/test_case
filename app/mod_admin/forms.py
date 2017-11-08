from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, FloatField, IntegerField, DateField
from wtforms.validators import DataRequired, URL, Length


class EventForm(FlaskForm):
    class Meta:
        csrf = False

    name = StringField(validators=[
        DataRequired(message='Name is required'),
        Length(max=32, message='Name length cant be more then 32 symbols')
    ])
    organizator = StringField(validators=[
        DataRequired(message='Organizer is required'),
        Length(max=32, message='Organizer length cant be more then 32 symbols')
    ])
    logo = FileField(validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only')
    ])
    icon = StringField(validators=[
        DataRequired(message='Icon is required'),
    ])
    description = StringField(validators=[
        DataRequired(message='Description is required'),
        Length(max=128, message='Description length cant be more then 128 symbols')
    ])
    what = StringField(validators=[
        DataRequired(message='"What" field is required'),
        Length(max=32, message='"What" length cant be more then 32 symbols')
    ])
    where = StringField(validators=[
        DataRequired(message='"Where" field is required'),
        Length(max=32, message='"Where" length cant be more then 32 symbols')
    ])
    when = StringField(validators=[
        DataRequired(message='"When" is required'),
        Length(max=32, message='"When" length cant be more then 32 symbols')
    ])
    lat = FloatField(validators=[
        DataRequired(message='lat is required'),
    ])
    lng = FloatField(validators=[
        DataRequired(message='lng is required'),
    ])
    number = IntegerField(validators=[
        DataRequired(message='Number is required'),
    ])
    url = StringField(validators=[
        DataRequired(message='URL is required'),
        URL()
    ])


class CampaignForm(FlaskForm):
    class Meta:
        csrf = False

    name = StringField(validators=[
        DataRequired(message='Name is required')
    ])
    event = StringField(validators=[
        DataRequired(message='Name is required')
    ])
    target_from = IntegerField(validators=[
        DataRequired(message='Number is required'),
    ])
    target_to = IntegerField(validators=[
        DataRequired(message='Number is required'),
    ])
    sex = StringField(validators=[
        DataRequired(message='Name is required')
    ])
    radius = FloatField(validators=[
        DataRequired(message='radius is required'),
    ])
    date = DateField(validators=[DataRequired(), ])
    lat = FloatField(validators=[
        DataRequired(message='lat is required'),
    ])
    lng = FloatField(validators=[
        DataRequired(message='lng is required'),
    ])
