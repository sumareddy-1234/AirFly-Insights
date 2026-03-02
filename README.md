# ✈️ AirFly Insights – Data Cleaning and Operational Insights

---

## 📌 Project Overview

AirFly Insights is a data analytics project focused on analyzing airline flight operations to understand delay patterns, cancellations, and operational efficiency.

This milestone primarily focuses on **data cleaning, preprocessing, statistical validation, and structured aggregation analysis** to prepare the dataset for further visualization and advanced analytics.

The objective is not just cleaning the data, but also understanding its **distribution, skewness, and operational behavior**.

This project is part of my Infosys SpringBoard Virtual Internship 6.0 in Data Visualization and helps me build practical skills in handling real-world datasets.

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

## 🛠 Tools & Technologies

- Python  
- Pandas  
- NumPy  
- Jupyter Notebook  

---

## 🚀 Future Work

- Full Exploratory Data Analysis (EDA)
- Seasonal and time-series analysis
- Delay cause comparison across airlines and airports
- Interactive dashboards using Streamlit
- Advanced visual storytelling

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
