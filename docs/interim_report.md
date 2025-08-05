# Interim Project Report: Brent Oil Price Analysis

**Project Title:** Brent Oil Price Analysis: Identifying and Attributing Volatility Change Points

**Author:** Shegaw Adugna
**Date:** August 5, 2025

---

### **1. Introduction**

This report documents the progress made on the Brent Oil Price Analysis project, covering all aspects of **Task 1: Project Foundation and Data Preparation** and the initial implementation of **Task 2: Change Point Modeling and Insight Generation**. The primary objective is to build a robust analytical framework to identify significant shifts in Brent oil price volatility, link these changes to historical events, and present the findings in an accessible manner. The work is structured to be modular and reproducible, ensuring a strong foundation for the final deliverables.

---

### **2. Defining the Data Analysis Workflow**

The analysis of Brent oil prices to identify change points and associate them with significant events will follow these sequential steps:

1.  **Data Ingestion & Initial Cleaning:**
    * Load raw Brent oil price data.
    * Parse 'Date' column to datetime objects.
    * Handle missing values (if any).
    * Sort data by date.
2.  **Exploratory Data Analysis (EDA):**
    * Visualize raw price series to identify trends, seasonality, and initial periods of high volatility.
    * Analyze stationarity using statistical tests (e.g., Augmented Dickey-Fuller).
    * Transform price data (e.g., log returns) to achieve stationarity, if necessary, especially for volatility analysis.
    * Visualize log returns to observe volatility clustering.
3.  **Event Data Compilation:**
    * Systematic research of major geopolitical events, OPEC decisions, economic shocks, and sanctions.
    * Compile relevant events into a structured dataset with approximate start dates.
4.  **Bayesian Change Point Modeling:**
    * Implement a Bayesian Change Point model using PyMC on the Brent oil price (or log returns) series.
    * Define appropriate priors for model parameters (e.g., means/standard deviations before and after change, and the change point location).
    * Run MCMC sampling to infer posterior distributions of parameters.
5.  **Change Point Identification & Interpretation:**
    * Analyze the posterior distribution of the change point (`tau`) to determine the most probable dates of structural breaks.
    * Interpret changes in model parameters (e.g., mean price, volatility) before and after detected change points.
6.  **Event Association & Impact Quantification:**
    * Compare detected change points with the compiled list of key events.
    * Formulate hypotheses linking specific events to observed price shifts.
    * Quantify the impact of these events (e.g., percentage change in average price or volatility).
7.  **Advanced Analysis (Optional / Future Work):**
    * Explore incorporating external macroeconomic variables.
    * Consider more complex time series models (e.g., VAR, Markov-Switching).
8.  **Reporting & Dashboard Development:**
    * Summarize findings in a clear, data-driven report.
    * Develop an interactive dashboard using Flask (backend) and React (frontend) to visualize results and allow stakeholder exploration.

---

### **3. Task 1: Project Foundation and Data Preparation**

This foundational phase successfully implemented the first three steps of the defined workflow.

#### **3.1 Repository Structure**
The project follows a standard, modular directory structure to ensure clarity and maintainability. Key directories and files include:
* `data/processed/`: Stores the cleaned dataset (`brent_oil_clean.csv`) and researched event data (`events.csv`).
* `src/data_preparation/`: Contains the `clean_data.py` script for preprocessing.
* `notebooks/`: Houses Jupyter notebooks for exploratory data analysis (`EDA.ipynb`) and model implementation.
* `docs/`: Contains project documentation and analysis workflows.
```
BirhanEnergies_OilPriceAnalysis
├── data/
│   ├── processed/          # Cleaned data and model output
│   └── raw/                # Original raw data
│
├── docs/                   # Project documentation, reports, and workflows
│
├── notebooks/              # Jupyter Notebooks for analysis and visualization
│
├── src/
│   ├── data_preparation/   # Scripts for data cleaning
│   └── models/             # Scripts for model implementation
│
├── .gitignore
├── README.md
└── requirements.txt
├── .github/
└── test/
```

#### **3.2 Data Preparation and Cleaning**
The `src/data_preparation/clean_data.py` script was executed to process the raw Brent oil price data. This script performed crucial steps to make the data suitable for time series analysis:
* **Missing Value Handling:** Missing values were handled using time-based interpolation to maintain data continuity.
* **Log Returns Calculation:** The raw price series was converted to **log returns** to transform the non-stationary price data into a **stationary** series, a prerequisite for the change point model.

#### **3.3 Exploratory Data Analysis (EDA)**
A dedicated notebook, `notebooks/EDA.ipynb`, was created to validate the data. The EDA confirmed that the raw price series exhibits clear trends and is non-stationary. In contrast, a visual inspection of the log returns showed a series centered around zero with periods of volatility clustering. A formal **Augmented Dickey-Fuller (ADF) test** on the log returns yielded a p-value of **0.000000**, providing strong statistical evidence of stationarity. This finding justifies the use of log returns for the subsequent change point modeling.

---

### **4. Task 2: Change Point Modeling and Insight Generation**

This task, which corresponds to steps 4 through 6 of the defined workflow, involves applying a Bayesian model to the cleaned data to identify structural breaks.

#### **4.1 Methodology and Implementation**
A **Bayesian change point detection model** was chosen for its ability to not only identify a change point but also quantify the uncertainty around its location and the magnitude of the change. The model, implemented using the `PyMC` library, detects a shift in the **volatility (standard deviation)** of the log returns. The core model logic is encapsulated in the modular script `src/models/bayesian_changepoint.py`, which is then called and analyzed within the `notebooks/ChangePoint_Model.ipynb` notebook.

#### **4.2 Preliminary Findings and Analysis**
While the MCMC sampling process is currently running, the final analysis will follow a clear interpretive strategy. Based on the model's output, we expect to identify a significant change point (represented by `tau`) and a corresponding shift in volatility. For instance, a probable change point date is around **March 2020**. This date is strongly associated with the **COVID-19 pandemic** and the **Saudi-Russia oil price war**, which triggered a period of extreme market volatility. The model's `sigma_1` and `sigma_2` parameters will quantify this impact by showing a substantial increase in volatility after this event.

---

### **5. Conclusion**

The project has successfully completed its foundational tasks. The data has been cleaned, validated, and prepared for analysis according to the defined workflow. The Bayesian change point model is implemented in a modular fashion, and the sampling is underway. The project is well-positioned to produce meaningful insights by linking statistical findings to real-world events. The next phase will involve finalizing the model's output and developing an interactive dashboard to visualize these results.