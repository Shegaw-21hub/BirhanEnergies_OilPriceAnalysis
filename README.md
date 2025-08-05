# Birhan Energies: Brent Oil Price Analysis

This repository contains the analysis of **Brent oil prices** to identify significant change points and associate them with major **geopolitical** and **economic events**.

The project is structured into three main tasks:

1. **Data Foundation**  
2. **Change Point Modeling**  
3. **Interactive Dashboard Development**
## Project Structure

- data/: Contains raw and processed datasets.
- docs/: Project reports and documentation.
- notebooks/: Jupyter notebooks for EDA and model development.
- src/: Source code for data processing, modeling, and dashboard applications.
- tests/: Unit tests for various modules.
- .github/workflows/: CI/CD pipelines using GitHub Actions.
## Task 1: Laying the Foundation for Analysis

This task focused on establishing a robust foundation for the entire project. The primary goal was to ensure a clean, well-understood dataset and a clear analytical plan before moving on to complex modeling.
### Key Accomplishments

#### 1. Data Preparation  
The `src/data_preparation/clean_data.py` script was developed and executed to process the raw `BrentOilPrices.csv` file. This script handles date formatting, fills missing values, and calculates log returns. The log returns are crucial as they create a stationary time series, which is a fundamental requirement for our statistical change point model. The output, `brent_oil_clean.csv`, now serves as the canonical dataset for all subsequent analysis.

#### 2. Event Data Compilation  
A comprehensive dataset of 13 major events was researched and compiled into `data/processed/events.csv`. These events span economic crises, geopolitical conflicts, and significant OPEC decisions, providing a critical contextual layer for interpreting the statistical change points.
#### 3. Exploratory Data Analysis (EDA)  
An EDA notebook (`notebooks/EDA.ipynb`) was used to analyze the time series properties of the data. This analysis visually confirmed the non-stationary nature of the raw prices and the stationary nature of the log returns. A formal Augmented Dickey-Fuller (ADF) test on the log returns confirmed stationarity with a p-value of 0.000000, providing strong statistical evidence that the data is ready for modeling.
## Task 2: Change Point Modeling and Insight Generation

This task focuses on applying a Bayesian change point model to the cleaned Brent oil price data to identify significant shifts in market volatility. The core analysis, conducted in a Jupyter notebook, runs a PyMC model to detect these changes and associate them with historical events.
### Key Achievements

- **Bayesian Change Point Modeling**: A Bayesian model was implemented using the PyMC library to identify a change in the volatility of Brent oil price log returns. The model runs in a modular fashion, with the core sampling logic contained in `src/models/bayesian_changepoint.py` and the analysis and visualization in `notebooks/ChangePoint_Model.ipynb`.

- **Change Point Identification**: The model's output provides a posterior distribution for the change point (`tau`), pinpointing the most probable date when the market's volatility regime shifted. This is a crucial step in understanding structural breaks in the time series.

- **Interpretation and Quantification**: By analyzing the model's parameters, specifically the volatility before (`sigma_1`) and after (`sigma_2`) the change point, we can quantify the magnitude of the shift. This data will be used to associate the statistical findings with major historical events and quantify their impact.

#### Current Status

The model is currently running the MCMC sampling process. This is a computationally intensive step that can take a significant amount of time. Once completed, the notebook will generate a summary of the results, including the most probable change point date and a plot visualizing the change.

#### Next Steps

Upon completion of the model's run, the next steps are to:

1. **Interpret the Results**: Analyze the output to identify the precise date of the change point and the corresponding change in volatility.

2. **Associate with Events**: Cross-reference the detected date with the historical events from Task 1 to formulate a hypothesis about the cause of the volatility shift.

3. **Document Findings**: Record the key insights and quantitative impacts for use in the final report and dashboard.

