from flask import (
    Flask, render_template,
    url_for,
    redirect, flash
)

import pandas as pd
import joblib
from forms import input_from

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234'

model2 = joblib.load("Model.joblib")

# @app.route('/')
# def home():
#     return render_template('home.html', title='Home')

@app.route('/', methods=['GET', 'POST'])
def model():
    form = input_from()
    message = ""
    if form.validate_on_submit():
        try:
            df = pd.DataFrame({
                "airline": [form.airline.data],
                "date_of_journey": [form.date_of_journey.data.strftime('%Y-%m-%d')],
                "source": [form.source.data],
                "destination": [form.destination.data],
                "dep_time": [form.dep_time.data.strftime("%H:%M:%S")],  # Use colon separators for time
                "arrival_time": [form.arrival_time.data.strftime("%H:%M:%S")],  # Use colon separators for time
                "duration": [form.duration.data],
                "total_stops": [form.total_stops.data],
                "additional_info": [form.additional_info.data]
            })
            prediction = model2.predict(df)[0]
            message = f"The predicted price is {prediction:,.0f} pkr"
        except Exception as e:
            message = "An error occurred: " + str(e)
    else:
        message = "Please provide valid details"
    return render_template('index.html', title='Price Prediction of Airlines', form=form, output=message)

@app.route('/check')
def check():
    return render_template('a.html', title='Checking')

if __name__ == '__main__':
    app.run(debug=True)