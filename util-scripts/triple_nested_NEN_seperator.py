import pandas as pd


def clean_multiline_csv_safe(file_path, output_path):
    # Try reading with tab delimiter first
    try:
        df = pd.read_csv(file_path, sep='\t', engine='python')
    except Exception:
        df = pd.read_csv(file_path, sep=',', engine='python')

    # Handle missing headers: assume file has no header row
    if set(df.columns) == {0, 1, 2} or df.columns.tolist()[0].startswith('Unnamed'):
        print("⛔ No valid headers found. Assigning default headers: subject, predicate, object.")
        df.columns = ['subject', 'predicate', 'object']

    # Check for correct number of columns
    if df.shape[1] != 3:
        raise ValueError(
            f"❌ Expected 3 columns, found {df.shape[1]} columns: {df.columns.tolist()}")

    # Clean and expand all rows
    expanded_rows = []
    for _, row in df.iterrows():
        subjects = str(row['subject']).split('\n')
        predicates = str(row['predicate']).split('\n')
        objects = str(row['object']).split('\n')

        for subj in subjects:
            for pred in predicates:
                for obj in objects:
                    expanded_rows.append((
                        subj.strip(), pred.strip(), obj.strip()
                    ))

    # Save to cleaned CSV
    cleaned_df = pd.DataFrame(expanded_rows, columns=[
                              'subject', 'predicate', 'object'])
    cleaned_df.to_csv(output_path, index=False)
    print(f"✅ Cleaned CSV saved to: {output_path}")


# 🔧 Replace these paths with your actual files
input_file = "/Users/chrisdavisj/graph-rag-iswc-2025/KWG/NEN/Complex/KWG-NEN.csv"
output_file = "cleaned_output_safe.csv"

clean_multiline_csv_safe(input_file, output_file)
