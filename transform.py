import pandas as pd
def transform_data(df):
    try:
        # Convert 'name' to uppercase
        df['name'] = df['name'].str.upper()

        # Convert 'signup_date' to datetime
        df['signup_date'] = pd.to_datetime(df['signup_date'])

        print("✅ Data transformed successfully!")
        return df
    except Exception as e:
        print("❌ Transformation failed:", e)
        return None
