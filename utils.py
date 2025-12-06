import pandas as pd

def load_words(csv_path="words.csv"):
    """CSVから英単語データを読み込む"""
    return pd.read_csv(csv_path)