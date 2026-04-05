# ✈️ Airline Revenue Operations Analytics

An end-to-end data science and business intelligence project analyzing U.S. airline operations data to identify route-level risk, validate operational differences using hypothesis testing, and build stakeholder-friendly dashboard views.

## 📌 Project Highlights
- Cleaned and analyzed 1.65M+ flight records from BTS On-Time Performance data
- Performed EDA, hypothesis testing, and regression modeling
- Built a route-level risk framework using delay and cancellation behavior
- Created an interactive BI dashboard for operational monitoring

## 📌 Project Overview

Airlines operate in a highly complex environment where operational inefficiencies such as delays and cancellations can significantly impact revenue and customer experience.

In this project, I analyze airline operational data to identify route-level inefficiencies and quantify operational risk using statistical analysis and regression modeling.

---

## 🎯 Objective

The goal of this project is to:

* Identify routes with high operational risk
* Analyze delay and cancellation patterns
* Validate differences using statistical testing
* Build models to understand key drivers of delay
* Provide actionable business recommendations

---

## 📊 Dataset

* U.S. Bureau of Transportation Statistics (BTS) On-Time Performance Data
* Time Period: Q1 2024
* ~1.65 million flight records

---

## 🧠 Methodology

### 1. Data Preparation

* Selected relevant operational features
* Combined monthly datasets
* Handled missing values using domain logic
* Removed diverted flights for consistency

### 2. Exploratory Data Analysis

* Analyzed delay distributions
* Compared departure vs arrival delay behavior
* Identified busiest routes
* Conducted route-level delay and cancellation analysis

### 3. Feature Engineering

* Created route-level dataset
* Computed average delay, cancellation rate, and flight count
* Built a combined route risk score

### 4. Statistical Analysis

* Formulated hypotheses
* Checked assumptions (normality)
* Used Mann-Whitney U tests
* Found statistically significant differences between high-risk and low-risk routes

### 5. Modeling

* Built linear regression models
* Identified target leakage and corrected it
* Compared multiple models
* Evaluated using MAE, RMSE, and R²

---

## 🔍 Key Insights

* Airline delays are **right-skewed**, with most flights near on-time but some extreme delays
* Flights tend to **recover delays during transit**
* Operational performance varies significantly across routes
* High-risk routes show:

  * higher average delays
  * higher cancellation rates
* Cancellation rate is the **strongest predictor of delay**
* Route distance has a **moderate impact**
* Delay behavior is influenced by multiple external factors beyond this dataset

---

## 📈 Model Performance

| Model          | MAE  | RMSE | R²    |
| -------------- | ---- | ---- | ----- |
| Revised Model  | 4.41 | 5.45 | 0.035 |
| Expanded Model | 4.36 | 5.35 | 0.070 |

---

## 💡 Business Recommendations

* Prioritize high-risk routes for operational improvement
* Focus on reducing cancellations to improve overall performance
* Investigate consistently delayed routes for root causes
* Incorporate additional data such as weather and congestion
* Build route-level monitoring systems for proactive intervention

---

## ⚠️ Limitations

* Revenue is not directly modeled (no fare/passenger integration yet)
* External factors such as weather and airport congestion are not included
* Route-level aggregation may hide flight-level variation

---

## 🔮 Future Work

* Integrate fare and passenger data for revenue modeling
* Add weather and airport congestion features
* Build predictive models for delay and revenue
* Develop interactive dashboards

---

## 🛠️ Tools Used

* Python (pandas, numpy, matplotlib, seaborn, sklearn, scipy)
* SQL (for data thinking and aggregation logic)
* Jupyter Notebook

---

## 🚀 Key Takeaway

This project demonstrates how operational data can be transformed into actionable insights using data science, statistical analysis, and business thinking to identify inefficiencies and improve decision-making.

---

## Interactive Dashboard

Tableau Public Dashboard: [View the dashboard here](https://public.tableau.com/views/Book1_17753627281980/Dashboard?:language=en-US&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)
