import os
from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import arviz as az
import json

# Get the absolute path of the project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

app = Flask(__name__)
CORS(app)

# Use the project root to define absolute paths to your data files
PROCESSED_DATA_PATH = os.path.join(PROJECT_ROOT, "data", "processed", "brent_oil_clean.csv")
EVENTS_DATA_PATH = os.path.join(PROJECT_ROOT, "data", "processed", "events_data.csv")
TRACE_PATH = os.path.join(PROJECT_ROOT, "data", "processed", "changepoint_trace.nc")

def load_data():
    try:
        df = pd.read_csv(PROCESSED_DATA_PATH)
        df['Date'] = pd.to_datetime(df['Date'])
        events_df = pd.read_csv(EVENTS_DATA_PATH)
        events_df['Date'] = pd.to_datetime(events_df['Date'])
        trace = az.from_netcdf(TRACE_PATH)
        return df, events_df, trace
    except FileNotFoundError as e:
        print(f"Error: A required file was not found. Please ensure all data processing and modeling steps are complete. {e}")
        return None, None, None

df_data, df_events, model_trace = load_data()

@app.route('/api/data/prices', methods=['GET'])
def get_price_data():
    if df_data is None: return jsonify({"error": "Data not available."}), 500
    price_data = df_data[['Date', 'Price']].copy()
    price_data['Date'] = price_data['Date'].dt.strftime('%Y-%m-%d')
    return jsonify(price_data.to_dict(orient='records'))

@app.route('/api/data/events', methods=['GET'])
def get_event_data():
    if df_events is None: return jsonify({"error": "Event data not available."}), 500
    # Select the new columns for the frontend
    events_data = df_events[['Date', 'Event Description', 'Type']].copy()
    events_data['Date'] = events_data['Date'].dt.strftime('%Y-%m-%d')
    return jsonify(events_data.to_dict(orient='records'))

@app.route('/api/model/changepoint', methods=['GET'])
def get_changepoint_results():
    if model_trace is None: return jsonify({"error": "Model results not available."}), 500
    
    tau_samples = model_trace.posterior["tau"].values.flatten()
    most_probable_tau = int(pd.Series(tau_samples).mode().iloc[0])
    most_probable_date = df_data['Date'].iloc[most_probable_tau].strftime('%Y-%m-%d')
    
    sigma_1_mean = model_trace.posterior["sigma_1"].values.mean()
    sigma_2_mean = model_trace.posterior["sigma_2"].values.mean()
    
    results = {
        "most_probable_date": most_probable_date,
        "sigma_1_mean": sigma_1_mean.item(),  # Ensure it's a standard Python type
        "sigma_2_mean": sigma_2_mean.item()
    }
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port=5000)