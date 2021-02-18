from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, SelectField, SubmitField, PasswordField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired, InputRequired, Length, NumberRange, URL, ValidationError
from grocery_app.models import ItemCategory, GroceryStore, GroceryItem, User

class GroceryStoreForm(FlaskForm):
    """Form for adding/updating a GroceryStore."""

    title = StringField('Title', validators=[DataRequired(), Length(min=3, max=80)])
    address = StringField('Address', validators=[DataRequired(), Length(min=3, max=80)])
    submit = SubmitField('Submit')
    # - title - StringField
    # - address - StringField
    # - submit button

class GroceryItemForm(FlaskForm):
    """Form for adding/updating a GroceryItem."""

    name = StringField('Name', validators=[DataRequired(), Length(min=3, max=80)])
    price = FloatField('Price', validators=[InputRequired(), NumberRange(min=0)])
    category = SelectField('Category', choices=ItemCategory.choices())
    photo_url = StringField('Photo', validators=[URL()])
    store = QuerySelectField('Store', query_factory=lambda: GroceryStore.query)
    submit = SubmitField('Submit')
    # - name - StringField
    # - price - FloatField
    # - category - SelectField (specify the 'choices' param)
    # - photo_url - StringField (use a URL validator)
    # - store - QuerySelectField (specify the `query_factory` param)
    # - submit button

class SignUpForm(FlaskForm):
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField('User Name',
        validators=[DataRequired(), Length(min=3, max=50)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
