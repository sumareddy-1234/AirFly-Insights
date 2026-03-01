# ✈️ AirFly Insights – Data Cleaning and Operational Insights

---

## 📌 Project Overview

AirFly Insights is a data analytics project focused on analyzing airline flight operations to understand delay patterns, cancellations, climatic impact, and operational efficiency.

The project is divided into two major milestones:

- **Milestone 1:** Data Cleaning, Statistical Validation, and Feature Engineering  
- **Milestone 2:** Visual Exploration, Delay Trend Analysis, and Temporal Intelligence  

The objective is not just cleaning the data, but also understanding its distribution, skewness, seasonal patterns, delay causes, and operational behavior using visual storytelling techniques.

This project is part of my Infosys Springboard Virtual Internship 6.0 in Data Visualization and helps me build practical skills in handling real-world datasets and developing analytical dashboards.
---

## 🎯 Objectives

- Clean and preprocess airline flight dataset  
- Handle missing values using statistically justified methods  
- Analyze delay distributions using skewness  
- Perform aggregation analysis across airlines and routes  
- Engineer time-based and route-based features  
- Generate a clean dataset for downstream analytics and dashboards  

---

## 📂 Dataset

- **Source:** Kaggle Airlines Flights Dataset  
- Contains flight-level operational data including:
  - Airline
  - Origin and destination airports
  - Departure and arrival delays
  - Cancellation status
  - Delay reasons  
- Due to large size, **sampling and memory optimization** were applied  
- Final cleaned dataset saved as: `cleaned_flights.csv`

---

## 🧹 Milestone 1 – Data Cleaning & Statistical Preparation

---

### ✔ Tasks Completed

#### 1️⃣ Data Loading & Initial Inspection

- Loaded dataset using `pandas`
- Inspected structure using `.info()` and `.describe()`
- Identified missing values and data types
- Checked dataset size and memory usage

---

#### 2️⃣ Datetime Processing

- Converted `FL_DATE` from string to datetime format
- Extracted new time-based features:
  - `MONTH`
  - `DAY_OF_WEEK`
  - `HOUR`

---

#### 3️⃣ Missing Value Handling

- Filled `DEP_DELAY` and `ARR_DELAY` using **median**
  - Median chosen due to strong positive skewness
- Filled `CANCELLATION_CODE` with `"Not Cancelled"`
- Filled delay reason columns (`DELAY_DUE_*`) with `0`
- Removed duplicate records

---

#### 4️⃣ Data Normalization

- Standardized categorical columns:
  - Converted text to uppercase
  - Removed extra spaces
- Ensured valid and consistent values
- Removed invalid records where required for analysis

---

#### 5️⃣ Feature Engineering

Created new analytical features:

- `MONTH` – extracted from flight date  
- `DAY_OF_WEEK` – weekday of flight  
- `HOUR` – departure hour  
- `ROUTE` – combination of origin and destination  

These features enable time-based and route-based analysis.

---

#### 6️⃣ Skewness Analysis (Added Enhancement)

- Calculated skewness for:
  - Arrival Delay
  - Departure Delay

**Observations:**
- Both delays show **high positive skewness (~6.5)**
- Indicates presence of extreme delay values (long right tail)

**Conclusion:**
- Mean is heavily affected by outliers
- Median is more robust
- Justifies median-based imputation for delay columns

---

#### 7️⃣ Aggregation Analysis (Added Enhancement)

Performed grouped analysis using `groupby`:

- Airline-level delay averages
- Route-level total flights and average delays
- Delay reason totals
- Percentage of flights delayed more than 15 minutes
- Cancellation percentage

These aggregations help understand operational patterns before full EDA.

---

## 📊 Statistical Enhancements Included

| Analysis | Purpose |
|--------|--------|
| Skewness | Understand delay distribution shape |
| Aggregation | Identify operational trends |
| Correlation | Check relationship between delays |
| Delay % | Measure performance impact |
| Route Analysis | Identify high-delay routes |

---

## 📊 Feature Dictionary (Key Columns)

| Feature | Description |
|--------|------------|
| FL_DATE | Flight date |
| AIRLINE | Airline code |
| ORIGIN | Origin airport |
| DEST | Destination airport |
| DEP_DELAY | Departure delay (minutes) |
| ARR_DELAY | Arrival delay (minutes) |
| MONTH | Extracted month |
| DAY_OF_WEEK | Extracted weekday |
| HOUR | Departure hour |
| ROUTE | Origin–Destination route |

---

## 📈 Key Observations from Milestone 1

- Delay distributions are highly right-skewed
- Extreme delays significantly impact averages
- Strong correlation between departure and arrival delays
- Certain routes consistently experience higher delays
- Carrier and late aircraft delays contribute most to total delay minutes
- A small percentage of flights cause a large portion of delays

---

# 📊 Milestone 2 – Visual Exploration & Delay Trend Analysis

---

## 🎯 Objective

The goal of Milestone 2 is to perform structured exploratory data analysis (EDA) and identify delay trends using:

- Univariate Analysis
- Bivariate Analysis
- Delay Cause Analysis
- Climatic & Weather Impact Study
- Rolling Averages
- Data Transformations
- Temporal Intelligence Concepts

---

## ✔ Tasks Completed

### 1️⃣ Univariate Analysis

- Top airlines by flight volume
- Flight distribution by month
- Flight distribution by hour
- Route frequency analysis
- Arrival delay distribution (histogram & boxplot)

---

### 2️⃣ Bivariate Analysis

- Airline vs Average Arrival Delay
- Month vs Delay Trend
- Hour vs Delay Pattern
- Correlation between Departure and Arrival Delay
- Route vs Delay comparison

---

### 3️⃣ Delay Cause Analysis

Analyzed contribution of:

- Carrier Delay
- Weather Delay
- NAS (National Airspace System) Delay
- Late Aircraft Delay
- Security Delay

Key findings:
- Operational causes dominate total delay minutes
- Late aircraft delay contributes significantly
- Weather delays show seasonal variation

---

### 4️⃣ Climatic & Seasonal Impact

- Monthly weather delay trend analysis
- Comparison of operational vs climatic delay causes
- Identification of peak delay months

---

### 5️⃣ Rolling Average Analysis

- 3-month rolling average applied to smooth delay trends
- Helps identify long-term patterns instead of short-term fluctuations

---

### 6️⃣ Temporal Intelligence

- Month vs Hour heatmap analysis
- Delay severity categorization (>15 mins)
- Peak congestion time identification

---

## 📈 Key Observations from Milestone 2

- Delays are heavily right-skewed
- Departure delay strongly influences arrival delay
- Evening hours experience higher average delays
- Weather-related delays peak in specific months
- Operational inefficiencies contribute more than climatic factors
- A small percentage of flights cause a large portion of total delay minutes

---

## 📊 Advanced Analytical Techniques Used

| Technique | Purpose |
|-----------|----------|
| Rolling Average | Trend smoothing |
| Log Transformation | Handle skewed delay distribution |
| Heatmaps | Multi-dimensional temporal analysis |
| KPI (Delay Rate %) | Operational performance measurement |
| Correlation Matrix | Identify predictor relationships |

---

## 🛠 Tools & Technologies

- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Seaborn  
- Jupyter Notebook  
- Git & GitHub  

---

## 🚀 Future Work

The upcoming milestones will focus on deeper operational insights, cancellation patterns, and final analytical storytelling.

---

### 📊 Milestone 3 – Route, Cancellation & Seasonal Insights

#### Week 5: Route and Airport-Level Analysis
- Identify Top 10 origin-destination pairs
- Generate delay heatmaps by airport and route
- Visualize busiest airports using maps
- Analyze airport-level average delay performance
- Study route-level congestion patterns

#### Week 6: Seasonal & Cancellation Analysis
- Monthly cancellation trend analysis
- Breakdown of cancellation types:
  - Carrier-related
  - Weather-related
  - Security-related
  - NAS-related
- Analyze seasonal impact (winter, monsoon, peak travel months)
- Study effect of holidays and climatic conditions on cancellations

Deliverables:
- Seasonal visual summaries
- Route congestion insights
- Cancellation pattern analysis

---

### 📈 Milestone 4 – Final Report & Presentation

#### Week 7: Visual Report / Dashboard
- Combine all milestone visualizations into a coherent analytical storyline
- Build interactive Streamlit dashboard
- Ensure professional visualization standards:
  - Clear titles
  - Proper axis labels
  - Legends and annotations
  - Consistent styling

#### Week 8: Documentation & Final Presentation
- Create final analytical report (README / PDF)
- Develop presentation slide deck
- Record walkthrough explaining:
  - Key insights
  - Business implications
  - Recommendations
- Summarize operational findings and improvement suggestions

---

## 🙌 Learning Outcome

This milestone helped me gain hands-on experience in:

- Real-world data preprocessing
- Handling missing values correctly
- Using skewness for statistical decisions
- Feature engineering for analytics
- Aggregation and KPI-based understanding
- Structuring an end-to-end data analytics workflow

---

## 👩‍💻 Author

**Suma Satti**  
B.Tech CSE (Data Science)  
Aspiring Data Analyst  

---
