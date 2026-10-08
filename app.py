import pandas as pd
import numpy as np

# 1. Load data from local directory
# Replace the path below with your local file path if necessary
file_path = "FurahaAdmissionsAllClinics (2).xlsx"
data = pd.read_excel(file_path)

# 2. Inspect DataFrame basic details and summary
print("--- Data Head ---")
print(data.head())

print("\n--- Data Info ---")
data.info()

print("\n--- Data Summary Statistics ---")
print(data.describe())

# 3. Filter DataFrame for admission numbers starting with 'RI' or 'FCME'
data_filtered = data[
    data["AdmissionNumber"]
    .astype(str)
    .str.startswith(("RI", "FCME"), na=False)
]

print("\n--- Filtered Data Head (Starts with RI or FCME) ---")
print(data_filtered.head())

# 4. Remove rows where AdmissionNumber starts with 'FCMER'
data = data[~data["AdmissionNumber"].str.startswith("FCMER", na=False)]

print("\n--- Data Head after removing FCMER prefix ---")
print(data.head())

# 5. Inspect tail of filtered data
print("\n--- Filtered Data Tail ---")
print(data_filtered.tail())
