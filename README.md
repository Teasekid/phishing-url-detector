
# Phishing URL Detection System

A machine learning-based system to detect phishing URLs using Python and Streamlit.

## Features
- Collects and preprocesses phishing and legitimate URLs
- Extracts useful features from URLs
- Trains and evaluates multiple ML models
- Interactive Streamlit UI for real-time URL classification

## Usage Instructions

### 1. Install dependencies
```powershell
pip install -r requirements.txt
```

### 2. Generate or expand the dataset
To create or add more synthetic URLs to your dataset:
```powershell
python generate_dataset.py
```
This will append 1,000 new, unique URLs to `data/urls.csv` each time you run it. You can change the batch size in `generate_dataset.py` by editing `add_count`.

### 3. Train and evaluate models
```powershell
python model_training.py
```
This will train Logistic Regression, Random Forest, and XGBoost models, print their metrics, and save the best model as `best_model.pkl`.

### 4. Run the Streamlit app
```powershell
streamlit run app.py
```
This launches the web interface. Enter a URL to get a real-time phishing/legitimate prediction.

### 5. Customization
- To use your own dataset, replace or edit `data/urls.csv`.
- To change the number of new URLs generated per run, edit `add_count` in `generate_dataset.py`.
- Feature extraction logic can be modified in `feature_extraction.py`.

## Project Structure

```
phishing_url/
├── data/
│   └── urls.csv                # Dataset: phishing & legitimate URLs
├── feature_extraction.py       # Feature engineering functions
├── model_training.py           # Model training & evaluation
├── phishing_detector.py        # Model loading & prediction
├── app.py                      # Streamlit user interface
├── generate_dataset.py         # Synthetic dataset generator
├── requirements.txt            # Dependencies
└── README.md                   # Project documentation
```
