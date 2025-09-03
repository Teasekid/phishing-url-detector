"""
phishing_detector.py
-------------------
Loads the trained model and predicts phishing/legitimate for a given URL.
"""
import joblib
from feature_extraction import extract_features
import pandas as pd

def load_model(path='best_model.pkl'):
    return joblib.load(path)

def predict_url(url, model):
    features = extract_features(url)
    X = pd.DataFrame([features])
    pred = model.predict(X)[0]
    return 'Phishing' if pred == 1 else 'Legitimate'
