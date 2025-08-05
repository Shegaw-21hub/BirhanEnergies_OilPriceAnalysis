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

