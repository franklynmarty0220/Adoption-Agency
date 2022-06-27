from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, TextAreaField,SelectField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional

class AddPetForm(FlaskForm):
    """From to add Pet"""
    name = StringField(
        "Pet Name", validators=[InputRequired(message="Please enter Pet")]
    )

    speicies = SelectField(
        "Type of Pet", choices = [("cat", "cat"),("dog", "dog"),("bird","bird")]

    )

    photo_url = StringField(
        "Photo", validators=[Optional(), URL()]
    )

    age = IntegerField(
        "Age", validators=[Optional(), NumberRange(min=0,max=25)] 
    )

    notes = TextAreaField(
        "Comments", validators=[Optional(),Length(min=15,max=160)]
    )

class EditPetForm(FlaskForm):
    """Form to edit existing Pet"""

    photo_url = StringField("Photo Url", validators=[Optional(), URL()])

    notes = TextAreaField("Comments", validators=[Optional(),Length(min=15,max=160)])

    availablity = BooleanField("Availablity", validators[InputRequired(message="Is it still available")])

