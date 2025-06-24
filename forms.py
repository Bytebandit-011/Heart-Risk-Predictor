import pandas as pd
from flask_wtf import FlaskForm
from wtforms import (
    IntegerField,
    SubmitField  
)
from wtforms.validators import DataRequired

train = pd.read_csv('data/heart1.csv')
X_data = train.drop(columns=['target'])

class InputForm(FlaskForm):
    sex = IntegerField(
        label="Sex",
        validators=[DataRequired()]
    )
     
    age = IntegerField(
        label="Age",
        validators=[DataRequired()]
    )

    cp = IntegerField(
        label="ChestPain",
        validators=[DataRequired()]
    )
    
    chol = IntegerField(
        label="Cholestrol",
        validators=[DataRequired()]
    )

    fbs = IntegerField(
        label="FastBloodSugar",
        validators=[DataRequired()]
    )

    trestbps = IntegerField(
        label="TrestBPS",
        validators=[DataRequired()]
    )

    restecg = IntegerField(
        label="Resting Electrocardiographic Results ",
        validators=[DataRequired()]
    )

    thalach = IntegerField(
        label="Maximum Heart Rate Achieved",
        validators=[DataRequired()]
    )

    exang = IntegerField(
        label=" Exercise-Induced Angina",
        validators=[DataRequired()]
    )

    oldpeak = IntegerField(
        label="ST Depression Induced by Exercise Relative to Rest",
        validators=[DataRequired()]
    )

    slope = IntegerField(
        label="Slope of the Peak Exercise ST Segment",
        validators=[DataRequired()]
    )

    ca = IntegerField(
        label=" Number of Major Vessels Colored by Fluoroscopy",
        validators=[DataRequired()]
    )

    thal = IntegerField(
        label="Thalassemia",
        validators=[DataRequired()]
    )


    submit = SubmitField("Predict")