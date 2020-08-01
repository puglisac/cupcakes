from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class CupcakeForm(FlaskForm):
    """for adding pets"""
    flavor=StringField("Flavor", validators=[InputRequired()])
    Image=StringField("Image", validators=[Optional(), URL()], default="https://tinyurl.com/demo-cupcake")
    Rating=FloatField("Rating", validators=[InputRequired()])
    Size=StringField("Size", validators=[InputRequired()])