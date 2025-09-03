"""
feature_extraction.py
---------------------
Functions for extracting features from URLs for phishing detection.
"""
import re
import pandas as pd
from urllib.parse import urlparse

def extract_features(url):
    """Extracts features from a single URL."""
    parsed = urlparse(url)
    features = {}
    features['url_length'] = len(url)
    features['domain_length'] = len(parsed.netloc)
    features['has_https'] = int(parsed.scheme == 'https')
    features['count_dots'] = url.count('.')
    features['count_hyphens'] = url.count('-')
    features['count_at'] = url.count('@')
    features['count_question'] = url.count('?')
    features['count_equal'] = url.count('=')
    features['count_percent'] = url.count('%')
    features['count_slash'] = url.count('/')
    features['count_digits'] = len(re.findall(r'\d', url))
    features['has_ip'] = int(bool(re.match(r"^(http[s]?://)?(\d{1,3}\.){3}\d{1,3}", url)))
    features['has_redirect'] = int('//' in url[8:])  # after http(s)://
    return features

def build_feature_dataframe(urls):
    """Builds a DataFrame of features for a list of URLs."""
    feature_list = [extract_features(url) for url in urls]
    return pd.DataFrame(feature_list)
