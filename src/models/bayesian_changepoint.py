import pymc as pm
import numpy as np
import pandas as pd
import arviz as az
import os

def run_changepoint_model(data_to_model):
    """
    Builds and runs a Bayesian change point model on log return data.
    This model detects a change in the volatility (standard deviation).

    Args:
        data_to_model (np.ndarray): The time series data (e.g., log returns).

    Returns:
        az.InferenceData: The output of the PyMC sampler.
    """
    with pm.Model() as bayesian_volatility_change_point_model:
        # Prior for the change point location (uniform over the time series)
        tau = pm.DiscreteUniform("tau", lower=0, upper=len(data_to_model) - 1)

        # Priors for the standard deviations (volatility) before and after the change point
        sigma_1 = pm.HalfNormal("sigma_1", sigma=0.1) # Volatility before change
        sigma_2 = pm.HalfNormal("sigma_2", sigma=0.1) # Volatility after change

        # Assume a constant mean for log returns, as they are centered around zero
        mu_log_return = pm.Normal("mu_log_return", mu=0, sigma=0.01)

        # Define the standard deviation for each data point based on the change point location
        idx = np.arange(len(data_to_model))
        sigma = pm.math.switch(idx < tau, sigma_1, sigma_2)

        # Likelihood of the observed data
        observation = pm.Normal("observation", mu=mu_log_return, sigma=sigma, observed=data_to_model)

        # Sample from the posterior distribution
        print("\nStarting PyMC sampling for Bayesian Volatility Change Point Detection...")
        trace = pm.sample(draws=2000, tune=1000, chains=2, random_seed=42, return_inferencedata=True, cores=1)
        print("PyMC Sampling Complete.")
        
    return trace