import numpy as np
import pandas as pd
from flask import Flask, request, render_template
import joblib

app = Flask(__name__)
model = joblib.load("Students_mark_predictor_model.pkl")

df = pd.DataFrame()

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
    global df

    input_features = [int(x) for x in request.form.values()]
    features_value = np.array(input_features)

    if input_features[0] < 0 or input_features[0]>24:
        return render_template('index.html',prediction_text = 'Please enter valid hourse between 1-24 if using this app from Earth')

    output = model.predict([features_value])[0][0].round(2)

    df = pd.concat([df,pd.DataFrame({'Study Hours':input_features,'Predicted Output':[output]})],ignore_index=True)
    print(df)
    df.to_csv('smp_data_from_app.csv')

    return render_template('index.html',prediction_text = 'You will get [{}%] marks, if you study for [{}] hours per day'.format(output,int(features_value[0])))


if __name__ == "__main__":
    app.run()