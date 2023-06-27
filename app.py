from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
import requests
import json

app = Flask(__name__)
model = pickle.load(open("flight_rf.pkl", "rb"))

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "jhg9MUNARcHISJ8l_JnGSt6y7hdHYO__Z15SRfziwslQ"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}


@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@app.route("/predict", methods=["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        Journey_day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Journey_month = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").month)
        # print("Journey Date : ",Journey_day, Journey_month)

        # Departure
        Dep_hour = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").minute)
        # print("Departure : ",Dep_hour, Dep_min)

        # Arrival
        date_arr = request.form["Arrival_Time"]
        Arrival_hour = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(date_arr, format="%Y-%m-%dT%H:%M").minute)
        # print("Arrival : ", Arrival_hour, Arrival_min)

        # Duration
        dur_hour = abs(Arrival_hour - Dep_hour)
        dur_min = abs(Arrival_min - Dep_min)
        # print("Duration : ", dur_hour, dur_min)

        # Total Stops
        Total_stops = int(request.form["stops"])
        # print(Total_stops)

        # Airline
        # AIR ASIA = 0 (not in column)
        airline = request.form['airline']
        if(airline == 'Jet Airways'):
            Jet_Airways = 1
            IndiGo = 0
            Air_India = 0
            Multiple_carriers = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0
            Multiple_carriers_Premium_economy = 0
            Jet_Airways_Business = 0
            Vistara_Premium_economy = 0
            Trujet = 0
        # Rest of the airline options...

        # Source
        # Banglore = 0 (not in column)
        Source = request.form["Source"]
        if (Source == 'Delhi'):
            s_Delhi = 1
            s_Kolkata = 0
            s_Mumbai = 0
            s_Chennai = 0
        # Rest of the source options...

        # Destination
        # Banglore = 0 (not in column)
        Destination = request.form["Destination"]
        if (Destination == 'Cochin'):
            d_Cochin = 1
            d_Delhi = 0
            d_New_Delhi = 0
            d_Hyderabad = 0
            d_Kolkata = 0
        # Rest of the destination options...

        # Create input_data dictionary
        input_data = {
            "Journey_day": Journey_day,
            "Journey_month": Journey_month,
            "Dep_hour": Dep_hour,
            "Dep_min": Dep_min,
            "Arrival_hour": Arrival_hour,
            "Arrival_min": Arrival_min,
            "Duration_hour": dur_hour,
            "Duration_min": dur_min,
            "Total_Stops": Total_stops,
            "Jet_Airways": Jet_Airways,
            "IndiGo": IndiGo,
            "Air_India": Air_India,
            "Multiple_carriers": Multiple_carriers,
            "SpiceJet": SpiceJet,
            "Vistara": Vistara,
            "GoAir": GoAir,
            "Multiple_carriers_Premium_economy": Multiple_carriers_Premium_economy,
            "Jet_Airways_Business": Jet_Airways_Business,
            "Vistara_Premium_economy": Vistara_Premium_economy,
            "Trujet": Trujet,
            "s_Delhi": s_Delhi,
            "s_Kolkata": s_Kolkata,
            "s_Mumbai": s_Mumbai,
            "s_Chennai": s_Chennai,
            "d_Cochin": d_Cochin,
            "d_Delhi": d_Delhi,
            "d_New_Delhi": d_New_Delhi,
            "d_Hyderabad": d_Hyderabad,
            "d_Kolkata": d_Kolkata
        }

        # Convert input_data to JSON
        payload_scoring = {"input_data": [input_data]}

        # Make prediction request
        response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/7b33ce39-ea07-4b8a-a277-4cb9f55ffe2e/predictions?version=2021-05-01', json=payload_scoring, headers=header)

        # Extract prediction from response
        scoring_response = json.loads(response_scoring.text)
        prediction = scoring_response['predictions'][0]['values'][0][0]

        return render_template('home.html', prediction_text="Your Flight price is Rs. {}".format(prediction))

    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)
