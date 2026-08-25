import pandas as pd

# 1. Load data
df = pd.read_csv('CRM_Data.csv')
# 2. Standardize text columns (strip spaces if any)
df['Region'] = df['Region'].str.strip()
df['Account_Status'] = df['Account_Status'].str.strip()
df['Customer_Type'] = df['Customer_Type'].str.strip()

# 3. Convert Signup_Date to datetime and extract Year-Month for trend analysis
df['Signup_Date'] = pd.to_datetime(df['Signup_Date'])
df['Signup_YearMonth'] = df['Signup_Date'].dt.to_period('M')

# 4. Create Audit Flag (The Core Cleaning/Auditing Logic)
# Active = Clean Data, Suspended/Fraudulent = Pipeline Leakage / Bad Data
df['Data_Health_Status'] = df['Account_Status'].apply(
    lambda x: 'Clean' if x == 'Active' else 'Pipeline_Leakage'
)

# 5. Save the cleaned/audited dataset
df.to_csv('CRM_Cleaned_Audited_Data.csv', index=False)

print('Data cleaning and audit tagging completed successfully!')
print(df['Data_Health_Status'].value_counts())
print('\nCleaned dataset saved as "CRM_Cleaned_Audited_Data.csv". Ready for'' SQL & Visualization!')