# 🔍 CRM Data Health & Pipeline Leakage Auditor

> A professional data analytics and CRM auditing project designed to detect, analyze, and prevent marketing budget wastage caused by dirty data, duplicate leads, and fraudulent/suspended accounts.

---

## 🎯 Project Overview
As companies scale their marketing and sales pipelines (via platforms like HubSpot or Marketo), poor data quality often results in skewed campaign metrics, high email bounce rates, and wasted ad spend. This project acts as an automated **CRM Data Health Auditor** to profile customer databases, calculate financial risk, and highlight pipeline leakages.

---

## 📊 Key Metrics & Findings (The Hero Numbers)
* **Data Health Score:** **31.8%** (Only 159 out of 500 accounts are Active/Clean).
* **Pipeline Leakage:** **68.2%** of records are either Suspended or Fraudulent (341 accounts).
* **Financial Impact / Cost of Waste:** **₹8.35 Lakhs** out of ₹12.54 Lakhs total pipeline value is locked/wasted in bad or high-risk accounts.
* **Regional Risk Hotspots:** **Africa (~42% Fraudulent)** and **South America (~39% Fraudulent)** generate the highest proportion of risky records.

---

## 🛠️ Tech Stack & Skills Demonstrated
* **Python (Pandas, Seaborn, Matplotlib):** Data profiling, automated cleaning, anomaly detection, and visualization generation.
* **Advanced SQL (Window Functions):** Using `ROW_NUMBER()`, `PARTITION BY`, and conditional aggregation to segment regional pipelines and rank high-value leads.
* **SQLite:** In-memory database processing for executing complex multi-row queries.
* **Business Intelligence & Consulting:** Translating raw database flags into actionable corporate strategy.
* **Data Studio for Dashboard report.

---

## 📂 Project Structure
```text
├── CRM_Cleaned_Audited_Data.csv   # Cleaned and audit-tagged dataset
├── crm_health_audit_chart.png     # Visual fragmentation chart by region
├── crm_queries.sql                # Advanced SQL Window Functions & summary queries
├── run_sql.py                     # Python script to execute and test SQL logic
|___Dashboard report               # Data Studio/ Looker Studio
└── README.md                      # Project documentation
