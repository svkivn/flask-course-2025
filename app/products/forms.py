from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DecimalField
from wtforms.validators import DataRequired, Length, NumberRange

class PostForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(min=2)])
    content = TextAreaField(
        "Content", 
        render_kw={"rows": 5, "cols": 40}, 
        validators=[DataRequired()]
        )
    price = DecimalField(
        "Enter price",
        places=2,  # кількість десяткових знаків
        rounding=None,  # або, наприклад, ROUND_HALF_UP
        validators=[DataRequired(), NumberRange(min=0, message="Price must be positive!")],
    ) 
    submit =SubmitField("Add Product")
