# Healthcare Data Analysis & Streamlit Dashboard

This project focuses on analyzing healthcare data to discover useful insights about patient demographics, medical conditions, hospital admissions, and billing trends.

The project uses Python for data analysis and Streamlit to build an interactive dashboard for visualization.

---

# Table of Contents

1. Project Overview
2. Project Description
3. Key Features
4. Tools & Technologies
5. Dataset Information
6. Exploratory Data Analysis (EDA)
7. Dashboard Overview
8. Project Structure
9. Installation & Setup
10. Author

---

# 1. Project Overview

The Healthcare Data Analysis project explores patient healthcare records to identify patterns in:

- Patient demographics
- Medical conditions
- Admission types
- Billing amounts
- Hospital performance
- Correlation between variables

The project demonstrates the use of data science techniques such as data preprocessing, feature engineering, and visualization to extract meaningful insights from healthcare datasets.

---

# 2. Project Description

This project analyzes a healthcare dataset containing patient information such as:

- Patient ID
- Name
- Age
- Gender
- Blood Type
- Medical Condition
- Date of Admission
- Hospital Name
- Doctor Name
- Insurance Provider
- Billing Amount
- Admission Type
- Medication
- Test Results

The dataset was analyzed using Python libraries such as Pandas, Matplotlib, and Seaborn. After performing Exploratory Data Analysis (EDA), an interactive dashboard was created using Streamlit to visualize important insights.

---

# 3. Key Features

- Data cleaning and preprocessing
- Feature engineering (Age Group column)
- Exploratory Data Analysis (EDA)
- Data visualization using charts
- Streamlit interactive dashboard
- Correlation heatmap
- Hospital billing comparison
- Yearly billing trend analysis
- Download processed dataset option

---

# 4. Tools & Technologies

Python  
Pandas  
NumPy  
Matplotlib  
Seaborn  
Streamlit  
Jupyter Notebook  
Excel Dataset  

---

# 5. Dataset Information

The dataset contains healthcare records with information about patient demographics, hospital details, and billing data.

Dataset characteristics:

- Rows: 55,000+
- Columns: 15+
- Data types: Numerical and Categorical
- Time range: Multiple years

Key variables include:

- Age
- Gender
- Medical Condition
- Admission Type
- Billing Amount
- Hospital
- Doctor
- Test Results

---

# 6. Exploratory Data Analysis (EDA)

EDA was performed to understand data distribution and identify trends.

Types of analysis performed:

### Univariate Analysis
- Gender distribution
- Age group distribution
- Medical condition frequency
- Admission type frequency

### Bivariate Analysis
- Billing amount vs medical condition
- Hospital vs billing comparison
- Year vs billing trend

### Correlation Analysis
- Relationship between Age, Billing Amount, and Room Number

---

# 7. Dashboard Overview

The Streamlit dashboard presents visual insights including:

- Gender Distribution Chart
- Age Group Distribution Chart
- Medical Condition Distribution
- Admission Type Distribution
- Average Billing Amount by Medical Condition
- Yearly Billing Trend Line Chart
- Top Hospital Billing Comparison
- Correlation Heatmap

The dashboard allows quick understanding of healthcare trends using interactive visualizations.

---

# 8. Project Structure

Health_Data_Trend_Project

├── README.md

├── app.py

├── health_analysis.ipynb

├── app.pyhealthcare_dataset.xlsx

---

# 9. Installation & Setup

Clone the repository:

git clone https://github.com/your-username/Health-Data-Trend-Report.git



Install required libraries:

pip install pandas numpy matplotlib seaborn streamlit openpyxl



Run the Streamlit dashboard:

streamlit run app.py
