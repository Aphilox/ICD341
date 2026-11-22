# Lab 17: Interactive Statistical Dashboard

## Project Overview
This project is a Streamlit-based interactive dashboard developed for ICD 341 (Advanced Statistical Computing). It demonstrates how to deploy a reproducible statistical simulation of maize production data. 

## Features
- **Reproducible Data Generation:** Uses a user-defined random seed to ensure results are exactly reproducible.
- **Interactive Controls:** Users can adjust the sample size, mean, and standard deviation of the simulated data via a sidebar.
- **Dynamic Visualizations:** Automatically updates summary metrics and a histogram based on user input.
- **Data Export:** Includes a built-in button to download the generated dataset as a CSV file.

## Project Structure
- `app.py`: The main Python script containing the Streamlit dashboard code.
- `requirements.txt`: Lists the Python packages required to run the dashboard.
- `README.md`: Instructions and documentation (this file).

## Installation and Setup

To run this dashboard locally, follow these steps:

1. **Activate your virtual environment** (e.g., Conda or venv).
   ```bash
   conda activate ICD341