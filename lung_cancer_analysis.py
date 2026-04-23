import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# 1. Load the dataset
df = pd.read_csv('lung_cancer_risk_data.csv')

# 2. Binary Value Transformation
# Convert the target variable to numeric (0/1)
df['PULMONARY_DISEASE_NUM'] = df['PULMONARY_DISEASE'].map({'YES': 1, 'NO': 0})

# 3. Cleaning
# Handle duplicates and ensure data integrity
df = df.drop_duplicates()
# Standardize column names to lowercase for easier coding if preferred
df.columns = [col.lower() for col in df.columns]

# 4. Standardize Continuous Variables (for analysis purposes)
scaler = StandardScaler()
# Keeping original values in the main DF for Issa's tooltips, 
# but creating scaled columns for ranking/modeling
continuous_vars = ['age', 'energy_level', 'oxygen_saturation']
df[[f'{col}_scaled' for col in continuous_vars]] = scaler.fit_transform(df[continuous_vars])

# 5. Export Cleaned Dataset for Issa (Visualization Engineer)
# This file will be the "Single Source of Truth" for your team's Altair charts
df.to_csv('cleaned_lung_cancer_data.csv', index=False)

print("Preprocessing complete. 'cleaned_lung_cancer_data.csv' has been generated.")

# 6. Factor Ranking (Analyst Duty)
# Calculate correlation to see which factors most influence the outcome
rankings = df.select_dtypes(include=[np.number]).corr()['pulmonary_disease_num'].sort_values(ascending=False)
print("\n--- Primary Risk Factors (Ranked by Correlation) ---")
print(rankings)

# 7. Co-occurrence Detection (Analyst Duty - for Heatmap)
risk_factors = ['smoking', 'exposure_to_pollution', 'breathing_issue', 'chest_tightness', 'family_history']
co_occurrence = df[risk_factors].corr()
print("\n--- Co-occurrence Matrix (Risk Factors) ---")
print(co_occurrence)