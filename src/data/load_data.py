import pandas as pd
import os

def load_csv(filename):
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
    path = os.path.join(base_path, 'data', 'raw', filename)
    print("Full path:", path)  # Tambahan debug
    return pd.read_csv(path)