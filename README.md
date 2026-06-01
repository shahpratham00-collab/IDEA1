<div align="center">

# 💧 HydroInsight — Hydration Risk Analytics Platform

### *A Python analytics system that processes 30,000 real-world health records to classify hydration risk, uncover behavioural patterns, and deliver actionable public health insights through statistical analysis, multi-panel visualisation, and an interactive desktop GUI.*

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![NumPy](https://img.shields.io/badge/NumPy-1.x-013243?style=flat-square&logo=numpy&logoColor=white)](https://numpy.org)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.x-11557c?style=flat-square)](https://matplotlib.org)
[![Seaborn](https://img.shields.io/badge/Seaborn-0.13-4c72b0?style=flat-square)](https://seaborn.pydata.org)
[![Tkinter](https://img.shields.io/badge/Tkinter-GUI-FF6F00?style=flat-square)](https://docs.python.org/3/library/tkinter.html)
[![License: MIT](https://img.shields.io/badge/License-MIT-22c55e?style=flat-square)](LICENSE)

</div>

---

## Executive Summary

HydroInsight is an end-to-end Python data analytics platform built on a real-world dataset of 30,000 individuals across diverse demographic, environmental, and lifestyle profiles. The system ingests raw CSV data, executes a structured cleaning and feature-engineering pipeline, applies rule-based hydration risk classification at multiple severity tiers, performs multi-dimensional statistical analysis, and surfaces findings through a suite of interactive visualisations and a live Tkinter desktop application.

The project addresses a practical public health question — *who is underhydrated, and why?* — and delivers quantified, segmentable answers. It demonstrates production-oriented Python development: modular function design, vectorised data operations, context-aware classification logic, and a user-facing GUI that allows non-technical stakeholders to explore filtered subsets in real time.

**Built with:** Python · Pandas · NumPy · Matplotlib · Seaborn · Tkinter  
**Dataset:** 30,000 records · 7 features · 975 KB  
**Pipeline:** Ingestion → Cleaning → Feature Engineering → Analysis → Visualisation → Interactive GUI

---

## Project Highlights

✅ &nbsp;Processed and cleaned **30,000 real-world health records** — identified 338 duplicates and zero post-cleaning null values  
✅ &nbsp;Engineered **3 derived classification features** from raw intake data using vectorised Pandas operations  
✅ &nbsp;Built a **context-aware hydration classifier** accounting for weather and activity level simultaneously  
✅ &nbsp;Quantified that **44% of low-activity individuals** are poorly hydrated vs. only **1% of high-activity individuals** — a 43-percentage-point spread  
✅ &nbsp;Identified **320 critical dehydration cases** (hot weather + intake < 2.0 L) for targeted risk intervention  
✅ &nbsp;Isolated **10,807 at-risk individuals** (36% of dataset) consuming below the 2.5 L safety threshold  
✅ &nbsp;Delivered **7 distinct visualisations** including histograms, box plots, grouped bar charts, count plots, and pie charts  
✅ &nbsp;Developed a **fully interactive Tkinter GUI** with dynamic filtering, live summary statistics, and embedded Matplotlib chart rendering  
✅ &nbsp;Structured entire codebase using **reusable, testable functions** encapsulating all core analytical logic  
✅ &nbsp;Managed project using **Git version control** with full change history

---

## Business Problem

Inadequate daily water intake is a widespread health risk linked to cognitive decline, cardiovascular stress, and reduced physical performance — yet most individuals have no awareness of whether their consumption is appropriate for their specific context. A person who drinks 2.8 litres may be well-hydrated in cold weather at rest, but dangerously underhydrated during hot-weather physical training.

Existing hydration guidance is generic and does not account for the interplay between environmental conditions, activity levels, and individual physiology. This project builds a data-driven framework that:

- **Segments** populations by risk tier based on personalised intake thresholds
- **Quantifies** how weather and activity independently and jointly drive consumption behaviour
- **Flags** high-risk individuals for targeted health interventions
- **Enables** exploration by demographic or environmental subgroup via a non-technical interface

**Real-world applications:** corporate wellness programmes, sports performance nutrition, NHS preventive health screening, wearable health technology, and public health campaign targeting.

---

## Technical Skills Demonstrated

### Programming & Software Engineering
- Python 3.9+ — object-oriented and functional programming patterns
- Modular function design with separation of concerns
- Lambda functions, `apply()`, and vectorised DataFrame operations
- Row-level iteration using `iterrows()` and `df.at[]` assignment

### Data Engineering
- CSV ingestion and schema inspection (`pandas`, `df.info()`, `df.dtypes`)
- Missing value detection and median imputation
- Duplicate identification and removal
- Multi-tier feature engineering with conditional logic

### Data Analysis & Statistics
- Descriptive statistics (`describe()`, `mean()`, `std()`, quartile analysis)
- Multi-dimensional `groupby` aggregation across 3 categorical variables
- Threshold-based risk classification and binary encoding
- Comparative subgroup analysis (gender, weather, activity, age cohort)

### Data Visualisation
- Matplotlib — bar charts, histograms, multi-panel subplot figures
- Seaborn — `histplot`, `barplot`, `boxplot`, `countplot` with hue mapping
- 2×2 subplot dashboard construction with `plt.subplots()`
- Pie chart composition for categorical distribution analysis

### GUI & Application Development
- Tkinter desktop application with `ttk.Combobox` dropdown filters
- `FigureCanvasTkAgg` Matplotlib-to-Tkinter canvas embedding
- Dynamic chart re-rendering and stateful filter management
- Event-driven button architecture (`filter_data`, `plot_hydration_pie`, `reset_selection`)

### Version Control & Documentation
- Git — commit tracking, version history, repository management
- GitHub — remote hosting, README documentation, portfolio presentation
- Inline code commenting and Markdown narrative documentation

---

## Project Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      RAW INPUT                              │
│         dataset.csv  ·  30,000 records  ·  975 KB          │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                   DATA INGESTION                            │
│   pd.read_csv()  ·  schema inspection  ·  df.info()        │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                   DATA CLEANING                             │
│  Missing value detection  ·  Median imputation             │
│  Duplicate identification (338 found)  ·  Deduplication    │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                FEATURE ENGINEERING                          │
│  Hydration Risk  (3-tier: Major / Moderate / Minimal)      │
│  Hydration Output  (binary: 0=Poor, 1=Good)                │
│  Hydration Result  (context-aware: weather + activity)     │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                STATISTICAL ANALYSIS                         │
│  groupby aggregation  ·  subgroup comparison               │
│  Dehydration risk flagging  ·  Population segmentation     │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                   VISUALISATION                             │
│  Histogram  ·  Bar charts  ·  Box plots  ·  Count plots    │
│  Pie charts  ·  Multi-panel 2×2 dashboards                 │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│             INTERACTIVE GUI APPLICATION                     │
│  Tkinter desktop app  ·  Dynamic filtering                 │
│  Live statistics  ·  Embedded Matplotlib charts            │
└──────────────────────────┬──────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────┐
│                INSIGHTS & OUTPUTS                           │
│  Quantified risk segmentation  ·  Behavioural trends       │
│  At-risk population identification  ·  Recommendations     │
└─────────────────────────────────────────────────────────────┘
```

---

## Dataset Overview

| Attribute | Detail |
|---|---|
| **Source** | [Kaggle — Daily Water Intake & Hydration Patterns](https://www.kaggle.com/datasets/sonalshinde123/daily-water-intake-and-hydration-patterns-dataset) |
| **Records** | 30,000 individuals |
| **Features** | 7 (3 numeric, 4 categorical) |
| **File Size** | 975 KB (CSV) |
| **Age Range** | 18–69 years (mean: 43.5) |
| **Weight Range** | 45–109 kg (mean: 76.8 kg) |
| **Intake Range** | 1.5–5.43 litres/day (mean: 2.85 L) |
| **Missing Values** | None |
| **Duplicates Identified** | 338 |

### Feature Definitions

| Column | Type | Description |
|---|---|---|
| `Age` | Integer | Individual age (18–69) |
| `Gender` | Categorical | Male / Female (50.1% / 49.9%) |
| `Weight (kg)` | Integer | Body weight in kilograms |
| `Daily Water Intake (liters)` | Float | Self-reported daily consumption |
| `Physical Activity Level` | Categorical | Low / Moderate / High (~33% each) |
| `Weather` | Categorical | Cold / Normal / Hot (~33% each) |
| `Hydration Level` | Categorical | Good (79.7%) / Poor (20.3%) — **target variable** |

The near-equal distribution of weather and activity categories across the dataset provides strong statistical validity for subgroup comparisons, making findings robust rather than artefacts of sampling bias.

---

## Methodology

### 1. Data Collection & Ingestion
Loaded 30,000-record CSV using Pandas. Performed schema inspection (`df.info()`, `df.dtypes`, `df.describe()`) to understand data types, ranges, and initial quality indicators before any transformation.

### 2. Data Cleaning
- Audited all columns for null values — confirmed zero missing entries in raw data
- Identified and removed 338 duplicate rows using `df.duplicated()` and `df.drop_duplicates()`
- Implemented median imputation pattern for weight as a robust cleaning template for future data drift scenarios

### 3. Feature Engineering
Three new classification columns were derived programmatically:
- **Hydration Risk**: Three-tier severity flag (`Major` / `Moderate` / `Minimal`) applied via vectorised `df.loc[]` conditional indexing
- **Hydration Output**: Binary label (0/1) assigned through row-level iteration incorporating weather-adjusted intake thresholds
- **Hydration Result**: Context-aware classification via a custom `hydration_weather_activity()` function applied across the full DataFrame with `df.apply(lambda...)`

### 4. Statistical Analysis
Executed `groupby` aggregations across Gender, Weather, and Physical Activity Level to compute mean intake per segment. Deployed conditional iteration to flag 320 critical dehydration cases (hot weather, intake < 2.0 L). Filtered and quantified subpopulations by intake threshold and age cohort for targeted insight extraction.

### 5. Visualisation
Constructed seven chart types in Matplotlib and Seaborn: distribution histogram, 2×2 multi-panel analytical dashboard (horizontal bar, grouped bar, box plot, count plot), and a 2×2 pie chart panel for categorical distribution profiling. All charts include labelled axes, titles, and grid overlays for professional readability.

### 6. Application Development
Built a fully functional Tkinter desktop GUI enabling dynamic data exploration. Users filter by Gender and Weather via dropdowns; the application computes and displays descriptive statistics for the filtered subset and renders an embedded Matplotlib pie chart of hydration level distribution in real time. Includes reset and exit controls.

---

## Key Findings & Insights

> *All figures derived directly from the 30,000-record dataset. No values estimated or extrapolated.*

### 🔴 Critical Population Risk
- **20.3% of the population (6,085 individuals)** is classified as `Poor` hydration — one in five people in this dataset is at measurable health risk
- **36% of individuals (10,807 people)** consume below the 2.5 L/day general health threshold
- **320 individuals** are in a critical risk state: hot-weather exposure combined with intake below 2.0 L/day

### 🏃 Physical Activity is the Strongest Predictor
- High-activity individuals drink **38.6% more water** than low-activity individuals (3.32 L vs 2.40 L average)
- **44% of low-activity individuals** are poorly hydrated — compared to just **1% of high-activity individuals**
- This 43-percentage-point gap is the largest observed differential across any variable in the dataset

### 🌡️ Weather Drives Consumption But Not Enough
- Hot weather correlates with a **39.5% higher average intake** than cold weather (3.40 L vs 2.44 L)
- Despite this, 320 individuals in hot conditions remain critically underhydrated — suggesting behavioural or awareness gaps that cannot be explained by environment alone

### 👥 Gender Shows Minimal Variance
- Female average: **2.858 L/day** | Male average: **2.847 L/day**
- Difference of 0.011 L is statistically negligible — gender is not a meaningful predictor of hydration behaviour in this dataset
- Interventions targeting intake should focus on activity and environment, not demographics

### 📊 Risk Classification Breakdown
| Risk Tier | Intake Threshold | Proportion |
|---|---|---|
| Minimal Risk | ≥ 4.0 L/day | ~25% of population |
| Moderate Risk | 3.0–3.99 L/day | ~28% of population |
| Major Risk | < 3.0 L/day | ~47% of population |

---

## Visualisations Included

| # | Chart Type | Purpose |
|---|---|---|
| 1 | **Bar chart** — Daily Water Intake by Age | Visualises hydration variance across the full 18–69 age span |
| 2 | **Histogram** — Intake Distribution | Reveals intake distribution shape, common ranges (2.5–3.5 L), and outliers |
| 3 | **Horizontal bar** — Hydration Level Count | Quantifies Good vs Poor population split |
| 4 | **Grouped bar** — Average Intake by Gender | Directly compares male/female hydration side-by-side |
| 5 | **Box plot** — Intake by Weather Condition | Shows median, IQR, and outlier structure for Hot / Normal / Cold cohorts |
| 6 | **Count plot** — Hydration Level by Activity | Stacked view of Good/Poor distribution across Low/Moderate/High activity |
| 7 | **2×2 Pie chart panel** | Categorical proportions: Gender · Hydration Level · Weather · Activity Level |

Charts 3–6 are assembled into a single 2×2 subplot figure (14×10 inch), providing a publication-ready analytical dashboard in one view.

---

## Interactive GUI Application

The **Hydration Data Explorer** is a desktop application developed with Python's Tkinter framework, enabling real-time exploratory analysis without requiring any coding knowledge.

### Features
| Feature | Detail |
|---|---|
| **Gender Filter** | Dropdown selector — All / Male / Female |
| **Weather Filter** | Dropdown selector — All / Hot / Normal / Cold |
| **Summary Statistics** | Displays count, mean, std, min, max, and quartiles for filtered subset |
| **Live Pie Chart** | Renders embedded Matplotlib chart of hydration level distribution for current filter |
| **Reset Control** | Clears all filters and chart in one click |
| **Exit Control** | Clean application shutdown |

### How It Works
1. Select a Gender and Weather combination from the dropdowns
2. Click **Show Summary** → descriptive statistics populate instantly
3. Click **Show Hydration Chart** → pie chart renders inside the application window
4. Click **Reset** → clears everything for fresh analysis

The GUI bridges the gap between raw Python analytics and business stakeholder access, demonstrating practical software development skills beyond notebook-based data science.

---

## Repository Structure

```
hydroinsight/
│
├── 📓 NTU_N1364759.ipynb          # Full analysis notebook — all 6 sections
├── 📄 dataset.csv                 # Source dataset (30,000 records, 975 KB)
├── 📋 README.md                   # This file
├── 📦 requirements.txt            # Python dependencies
│
└── 📁 docs/
    └── NTU_N1364759.pdf           # Full PDF export with outputs and visualisations
```

---

## ⚠️ GitHub Preview Notice

This repository contains Jupyter Notebook and source files that **GitHub may not render directly** due to file-size or rendering limitations.

**If the notebook preview is unavailable:**

1. Clone the repository locally: `git clone <repo-url>`
2. Open `NTU_N1364759.ipynb` in **Jupyter Notebook**, **JupyterLab**, or **VS Code**
3. Alternatively, refer to the **included PDF documentation** (`docs/NTU_N1364759.pdf`)

The PDF contains the complete methodology, all code cells with outputs, all visualisations, and the full conclusion — ensuring the project is fully reviewable even without a live notebook environment.

---

## Why This Project Matters

This project demonstrates the complete data analyst workflow from a single raw file to stakeholder-ready outputs:

**Technical depth:** The codebase spans five distinct engineering domains in a single coherent project — data engineering, statistical analysis, functional programming, data visualisation, and GUI application development. Each section uses the most appropriate technique for the task (vectorised operations for bulk transformations, row-level iteration where per-record logic is required, lambda functions for apply pipelines).

**Analytical rigour:** Findings are grounded in real data. Every percentage and metric cited is computed from the 30,000-record dataset, not fabricated for presentation. The context-aware classification model (adjusting thresholds by weather and activity simultaneously) reflects how real-world health assessment works — not a naive single-threshold rule.

**Practical output:** The Tkinter GUI transforms a Jupyter notebook into a distributable tool. Non-technical stakeholders — a nurse, a wellness coach, an HR manager — can use it to explore findings without touching code. This is the step that separates a data science project from a data science product.

**Industry relevance:** The skills exercised here map directly to day-to-day analytics engineering work: data cleaning pipelines, feature derivation, segmented reporting, dashboard construction, and building interfaces that deliver analytical value to end users.

---

## Future Enhancements

| Enhancement | Description |
|---|---|
| **ML Classification Model** | Train a Random Forest or XGBoost classifier to predict `Hydration Level` from all features; evaluate with cross-validation and feature importance analysis |
| **Streamlit Web Dashboard** | Migrate GUI to Streamlit for browser-based access, eliminating Tkinter dependency and enabling cloud deployment |
| **Correlation & Hypothesis Testing** | Apply Pearson/Spearman correlation and ANOVA to formally validate observed group differences with p-values |
| **Personalised Recommendation Engine** | Compute individual target intake based on weight, age, activity, and weather forecast using evidence-based hydration formulae |
| **REST API** | Wrap analytical functions in a FastAPI service to enable programmatic access from mobile health apps |
| **Automated Reporting** | Schedule daily HTML/PDF report generation via `nbconvert` + `cron` for ongoing population monitoring |
| **Unit Testing** | Add `pytest` coverage for all analytical functions to validate behaviour under edge cases and dataset updates |

---

## Installation

### Prerequisites
- Python 3.9+
- `pip` package manager

### Setup

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/hydroinsight.git
cd hydroinsight

# Install dependencies
pip install -r requirements.txt
```

**`requirements.txt`**
```
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
seaborn>=0.13.0
jupyter>=1.0.0
```

> Tkinter is included with the Python standard library and requires no separate installation.

---

## Usage

### Run the Full Analysis Notebook

```bash
jupyter notebook NTU_N1364759.ipynb
```

Execute cells sequentially. Each section is self-contained with markdown documentation explaining purpose and expected outputs.

### Launch the Interactive GUI

Run the final notebook cell in Section 5, or execute directly:

```python
# Ensure df_clean is loaded from the notebook pipeline, then run:
root.mainloop()
```

The Hydration Data Explorer desktop window will open. Use the dropdowns to filter by Gender and Weather, then click **Show Summary** or **Show Hydration Chart**.

---

## Recruiter Quick Summary

This project demonstrates:

✔ &nbsp;**Python Programming** — Functions, control flow, OOP patterns, lambda expressions  
✔ &nbsp;**Data Cleaning & Wrangling** — Null handling, deduplication, median imputation  
✔ &nbsp;**Exploratory Data Analysis** — Descriptive stats, distribution analysis, outlier review  
✔ &nbsp;**Feature Engineering** — Derived columns, binary encoding, multi-condition classification  
✔ &nbsp;**Statistical Analysis** — Multi-dimensional groupby, subgroup comparison, threshold analysis  
✔ &nbsp;**Data Visualisation** — 7 chart types across Matplotlib and Seaborn  
✔ &nbsp;**GUI / Application Development** — Tkinter desktop app with live chart rendering  
✔ &nbsp;**Software Engineering Practices** — Modular functions, clean code, inline documentation  
✔ &nbsp;**Business Communication** — Translating analytical findings into plain-language insights  
✔ &nbsp;**Git Version Control** — Repository management, commit history, GitHub portfolio  

---

## LinkedIn Project Summary

> *Suitable for LinkedIn Featured Section, CV Projects, or Portfolio Website*

---

**HydroInsight — Hydration Risk Analytics Platform | Python · Pandas · Seaborn · Tkinter**

Built an end-to-end Python analytics platform to analyse hydration behaviour across 30,000 real-world health records, identifying at-risk populations and quantifying the impact of lifestyle and environmental factors on daily water intake.

The system delivers a complete data pipeline — from CSV ingestion and cleaning (removing 338 duplicate records) through multi-tier risk classification and statistical segmentation to a suite of 7 visualisations and a fully interactive Tkinter desktop application.

Key findings: 44% of low-activity individuals are poorly hydrated vs. 1% of high-activity individuals — a 43-point gap. Hot weather drives 39.5% higher average intake than cold, yet 320 individuals remain critically underhydrated even in hot conditions. Overall, 20.3% of the population (6,085 individuals) falls into the Poor hydration category.

The project demonstrates proficiency in Pandas, NumPy, Matplotlib, Seaborn, and GUI development with Tkinter, alongside clean software engineering practices: modular function design, vectorised operations, and context-aware classification logic that accounts for multiple variables simultaneously.

📌 *View repository →* [github.com/YOUR_USERNAME/hydroinsight]

---

## ATS Keywords

```
Python | Pandas | NumPy | Matplotlib | Seaborn | Tkinter | Jupyter Notebook |
Data Analysis | Exploratory Data Analysis | EDA | Data Cleaning | Data Wrangling |
Feature Engineering | Statistical Analysis | Data Visualisation | Dashboard |
Data Pipeline | ETL | CSV Processing | DataFrame Operations | GroupBy Aggregation |
Descriptive Statistics | Risk Classification | Binary Classification |
Population Segmentation | Health Analytics | Behavioural Analytics |
GUI Development | Desktop Application | Interactive Visualisation |
Histogram | Box Plot | Pie Chart | Bar Chart | Subplot Dashboard |
Git | GitHub | Version Control | Jupyter | VS Code |
Problem Solving | Analytical Thinking | Data-Driven Insights |
Python Developer | Data Analyst | Junior Data Scientist | Analytics Engineer |
```

---

<div align="center">

*Built with Python · Driven by Data · Designed for Impact*

</div>
