# Data Analysis Agent – Automated EDA using AI Agents

## 📌 Project Overview
This project implements an AI-powered Data Analysis Agent that automates Exploratory Data Analysis (EDA).  
It reduces manual effort for data scientists by automatically profiling datasets, generating visualizations, detecting anomalies, suggesting features, and recommending machine learning models.

---

## 🎯 Objectives
- Automate repetitive EDA tasks
- Reduce analysis time using metadata compression (ScaleDown)
- Generate human-readable insights using AI agents
- Improve data scientist productivity

---

## 🧠 System Architecture
The system follows an agent-based architecture:

- **Data Ingestion Agent** – Loads CSV, SQL, Parquet data
- **ScaleDown Agent** – Compresses metadata by ~75%
- **Profiling Agent** – Computes statistics and data summaries
- **Visualization Agent** – Generates plots automatically
- **Anomaly Detection Agent** – Identifies outliers and inconsistencies
- **Insight Generator Agent** – Produces natural language insights
- **AutoML Agent** – Recommends suitable ML models
- **Report Generator** – Creates HTML EDA reports

---

## 📂 Supported Inputs
- CSV files
- SQL databases
- Parquet files

---

## ⚙️ Technologies Used
- Python
- Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn
- AutoML (PyCaret)
- AI/LLM-based insight generation
