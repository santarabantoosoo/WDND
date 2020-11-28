"""Form class declaration."""
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    DateField,
    PasswordField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import URL, DataRequired, Email, EqualTo, Length


class ContactForm(FlaskForm):
    """Contact form."""

    name = StringField("Name", [DataRequired()])
    email = StringField(
        "Email", [Email(message="Not a valid email address."), DataRequired()]
    )
    body = TextAreaField(
        "Message", [DataRequired(), Length(min=4, message="Your message is too short.")]
    )
    submit = SubmitField("Submit")

# TODO implement the signup form 