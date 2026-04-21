# PROGRAM: IQR Outlier Detection (Limited Output)

import pandas as pd

# Load dataset
df = pd.read_csv('4laptops.csv', engine='python', on_bad_lines='skip')

# Take only first 50 rows (VERY IMPORTANT)
df = df.head(50)

# Convert RAM if needed
if 'RAM' in df.columns:
    df['RAM'] = df['RAM'].astype(str).str.replace('GB', '')
    df['RAM'] = pd.to_numeric(df['RAM'], errors='coerce')

# Select only ONE numeric column (to avoid long output)
num_cols = df.select_dtypes(include=['int64', 'float64'])

# Pick first numeric column only
col = num_cols.columns[0]

# IQR calculation
Q1 = num_cols[col].quantile(0.25)
Q3 = num_cols[col].quantile(0.75)
IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

# Get outliers
outliers = num_cols[(num_cols[col] < lower) | (num_cols[col] > upper)]

# PRINT ONLY FEW LINES
print("Column:", col)
print("Total Outliers:", len(outliers))

print("\nSample Outliers (only 5 rows):")
print(outliers[[col]].head(5))

print("\n Program Finished Successfully")
