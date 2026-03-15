# ✈️ AirFly Insights: Data Visualization and Analysis of Airline Operations

## 📌 Project Overview

AirFly Insights is a **data visualization project focused on large-scale airline flight data**. The project analyzes airline operational performance to identify **delay patterns, route congestion, seasonal trends, and airport-level activity** through visual analysis.

The objective is to transform aviation datasets into **meaningful insights using data visualization techniques**, helping understand airline operations and performance.

This project was developed as part of the **Infosys Springboard Virtual Internship 6.0**.

---

# 🎯 Project Statement

The objective of this project is to **analyze large-scale airline flight data to uncover operational trends, delay patterns, and cancellation reasons using data visualization techniques**.

The goal is to help understand **airline and airport-level performance** and contribute to **actionable insights using visual analysis**.

---

# 🎓 Internship Context

This project is part of the **Infosys Springboard Virtual Internship 6.0**, where the objective is to apply **data analytics and visualization techniques** to a real-world aviation dataset.

The project demonstrates practical skills in:

* Data preprocessing and feature engineering
* Exploratory Data Analysis (EDA)
* Statistical visualization
* Airline operations analysis
* Interactive dashboard development

---

# 📂 Project Files

```id="9e5lg7"
AirFly-Insights
│
├── AirFly_Insights_Milestone1_Data_Cleaning.ipynb
├── AirFly_Insights_Milestone2_Visual_Analysis.ipynb
├── Milestone3_Route_Seasonal_Cancellation_Insights.ipynb
├── app.py
├── cleaned_flights.csv
└── README.md
```

---

# 🧰 Technologies Used

* **Python**
* **Pandas** – data manipulation and preprocessing
* **NumPy** – numerical operations
* **Matplotlib** – data visualization
* **Seaborn** – statistical visualization
* **Streamlit** – interactive dashboard development

---

# 📊 Expected Outcomes

The project aims to achieve the following outcomes:

* Understand and preprocess aviation datasets for analysis
* Explore trends in flight schedules, delays, cancellations, and routes
* Visualize key metrics using bar charts, time series, heatmaps, maps, and comparisons
* Provide insights for stakeholders including airline operators and analysts
* Summarize findings through a final visual report and presentation

---

# 📅 Week-wise Implementation Plan

## 🔹 Milestone 1: Data Foundation and Cleaning

### Week 1: Project Initialization and Dataset Setup

Key activities performed:

* Define project goals, KPIs, and workflow
* Load flight datasets using Pandas
* Explore dataset schema, column types, dataset size, and null values
* Perform sampling and memory optimization for efficient analysis

### Week 2: Preprocessing and Feature Engineering

Key tasks performed:

* Handle missing values in delay and cancellation columns
* Create derived features including:

  * Month
  * Day of Week
  * Hour
  * Route (Origin → Destination)
* Format datetime columns
* Save a cleaned dataset for analysis

### Deliverables

* Cleaned dataset
* Summary of preprocessing logic
* Feature dictionary

---

## 🔹 Milestone 2: Visual Exploration and Delay Trends

### Week 3: Univariate and Bivariate Visual Analysis

Analysis tasks include:

* Identifying top airlines by number of flights
* Identifying busiest routes
* Analyzing flight distribution across months and hours
* Exploring airport activity patterns

Visualization techniques used:

* Bar charts
* Histograms
* Boxplots
* Line charts

### Week 4: Delay Analysis – Airline and Weather

Analysis tasks include:

* Comparing delay causes by airline
* Exploring carrier delays, weather delays, and NAS delays
* Visualizing delay patterns by time of day and airport

### Deliverables

* A set of visualizations (minimum 8)
* Observations identifying peak delays and delay-prone airlines

---

## 🔹 Milestone 3: Route, Cancellation, and Seasonal Insights

### Week 5: Route and Airport-Level Analysis

Key analyses include:

* Identification of top 10 origin-destination route pairs
* Delay heatmaps by airport and route
* Visualization of busiest airports and delay patterns

### Week 6: Seasonal and Cancellation Analysis

Analysis tasks include:

* Monthly cancellation trends
* Cancellation type analysis (carrier, weather, security, NAS)
* Analysis of seasonal patterns such as winter months and holidays

### Deliverables

* Seasonal visual summaries
* Insights on route congestion and operational trends

---

# 📊 Interactive Dashboard

An **interactive analytics dashboard** was built using **Streamlit** to explore airline operational insights dynamically.

The dashboard allows users to analyze:

* Airline performance
* Route congestion patterns
* Airport delay trends
* Seasonal patterns
* Delay causes

---

# ▶️ Running the Dashboard

Install dependencies:

```id="fd5p7i"
pip install streamlit pandas matplotlib seaborn
```

Run the dashboard:

```id="ty1xv3"
streamlit run app.py
```

The dashboard will launch in your browser at:

```id="dz2hve"
http://localhost:8501
```

---

# 👩‍💻 Author

**Suma**
Data Science Student

Project completed as part of the **Infosys Springboard Virtual Internship 6.0**


