"""
model_training.py
-----------------
Train and evaluate ML models for phishing URL detection.
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
from feature_extraction import build_feature_dataframe

def load_data(csv_path):
    df = pd.read_csv(csv_path)
    X = build_feature_dataframe(df['url'])
    y = df['label'].map({'legitimate': 0, 'phishing': 1})
    return X, y

def train_and_evaluate(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    models = {
        'LogisticRegression': LogisticRegression(max_iter=1000),
        'RandomForest': RandomForestClassifier(n_estimators=100),
        'XGBoost': XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    }
    results = {}
    for name, model in models.items():
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        results[name] = {
            'model': model,
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred),
            'recall': recall_score(y_test, y_pred),
            'f1': f1_score(y_test, y_pred)
        }
    return results

def save_best_model(results, path='best_model.pkl'):
    best = max(results.items(), key=lambda x: x[1]['f1'])
    joblib.dump(best[1]['model'], path)
    return best[0], path

if __name__ == "__main__":
    X, y = load_data('data/urls.csv')
    results = train_and_evaluate(X, y)
    for name, res in results.items():
        print(f"{name}: Accuracy={res['accuracy']:.2f}, Precision={res['precision']:.2f}, Recall={res['recall']:.2f}, F1={res['f1']:.2f}")
    best_name, model_path = save_best_model(results)
    print(f"Best model: {best_name}, saved to {model_path}")
