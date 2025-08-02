# Interim Report: Birhan Energies - Brent Oil Price Analysis

## 1. Defining the Data Analysis Workflow

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
    * Implement a Bayesian Change Point model using PyMC3 on the Brent oil price (or log returns) series.
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