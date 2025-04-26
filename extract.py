import pandas as pd

def extract_from_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        print("✅ Data extracted successfully!")
        return df
    except Exception as e:
        print("❌ Extraction failed:", e)
        return None
