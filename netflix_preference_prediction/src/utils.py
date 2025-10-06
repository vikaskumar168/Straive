import os
import pandas as pd

def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory created: {path}")
    else:
        print(f"Directory already exists: {path}")

def load_csv(path, **kwargs):
    print(f"Loading CSV file from: {path}")
    df = pd.read_csv(path, **kwargs)
    print(f"Loaded {df.shape[0]} rows and {df.shape[1]} columns")
    return df

def save_csv(df, path):
    df.to_csv(path, index=False)
    print(f"Saved DataFrame with {df.shape[0]} rows and {df.shape[1]} columns to: {path}")
