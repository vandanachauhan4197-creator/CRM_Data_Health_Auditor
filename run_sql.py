import sqlite3
import pandas as pd

# 1.Loading the cleaned csv and uploading in database
df = pd.read_csv('CRM_Cleaned_Audited_Data.csv')
conn = sqlite3.connect(':memory:')
df.to_sql('crm', conn, index=False, if_exists='replace')

print('--- SQL QUERY 1: Regional Breakdown & Leakage ---')
query1 = """
SELECT 
    User_ID,
    Region,
    Account_Status,
    Bet_Amount,
    ROW_NUMBER() OVER (PARTITION BY Region ORDER BY Bet_Amount DESC) as regional_rank,
    SUM(Bet_Amount) OVER (PARTITION BY Region) as total_region_pipeline,
    SUM(CASE WHEN Account_Status != 'Active' THEN Bet_Amount ELSE 0 END) OVER (PARTITION BY Region) as wasted_pipeline_by_region
FROM crm
LIMIT 5;
"""
print(pd.read_sql(query1, conn))

print('\n--- SQL QUERY 2: High-Risk / Fraud Summary by Region ---')
query2 = """
SELECT 
    Region,
    Account_Status,
    COUNT(User_ID) as total_users,
    SUM(Bet_Amount) as total_bet_amount
FROM crm
GROUP BY Region, Account_Status
ORDER BY total_bet_amount DESC;
"""
print(pd.read_sql(query2, conn))

conn.close()