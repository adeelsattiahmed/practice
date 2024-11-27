from flask_wtf import FlaskForm
import pandas as pd
from wtforms import (
    SelectField,
    StringField,
    DateField,
    TimeField,
    IntegerField,
    SubmitField
)

from wtforms.validators import(
    data_required
)


train=pd.read_csv('data/train.csv')
val=pd.read_csv('data/val.csv')

data=pd.concat([train,val],axis=0)






class input_from(FlaskForm):
    airline=SelectField(
        label='Airline',
        choices=data['airline'].unique().tolist(),
        validators=[data_required()]
        )
    date_of_journey=DateField(
        label="Date of journey",
        validators=[data_required()]
    )
    source=SelectField(
        label="Source ",
        choices=data.source.unique().tolist(),
        validators=[data_required()]
    )
    
    destination=SelectField(
        label="Destination",
        choices=data.destination.unique().tolist(),
        validators=[data_required()]
    )
    
    dep_time=TimeField(
        label="Depaurture Time",
        validators=[data_required()]
    )
    arrival_time=TimeField(
        label="Arrival Time",
        validators=[data_required()]
    )
    duration=IntegerField(
        label='Time Duration',
        validators=[data_required()]
    )
    total_stops=IntegerField(
        label='Total Stops',
        validators=[data_required()]
    )
    additional_info=SelectField(
        label="Additonal information ",
        choices=data.additional_info.unique().tolist(),
        validators=[data_required()]
    )
    submit=SubmitField(
        label="Predict Now"
    )