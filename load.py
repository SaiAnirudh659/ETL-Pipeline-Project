def load_to_csv(df, output_path):
    try:
        df.to_csv(output_path, index=False)
        print(f"✅ Data loaded successfully to {output_path}")
    except Exception as e:
        print("❌ Loading failed:", e)
