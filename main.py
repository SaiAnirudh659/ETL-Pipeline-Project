from extract import extract_from_csv
from transform import transform_data
from load import load_to_csv

def main():
    # Step 1: Extract Data
    df = extract_from_csv('data/sample_data.csv')
    if df is None:
        return

    # Step 2: Transform Data
    df_transformed = transform_data(df)
    if df_transformed is None:
        return

    # Step 3: Load Data
    load_to_csv(df_transformed, 'data/cleaned_data.csv')

if __name__ == "__main__":
    main()
