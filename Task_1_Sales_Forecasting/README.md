# Sales & Demand Forecasting System
**Task 1: Future Interns Program (2026)**

## Overview
This project implements a sales forecasting system using Machine Learning. It predicts future product demand based on historical sales data, helping businesses plan inventory and manage cash flow.

## Project Structure
- `data/`: Contains the sales dataset (`retail_sales_simulated.csv`).
- `Forecasting_Analysis.ipynb`: Jupyter Notebook containing the full analysis, visualization, and modeling.
- `requirements.txt`: List of Python dependencies.

## Key Features
- **Data Analysis**: Visualization of daily sales trends and seasonality.
- **Feature Engineering**: Creating time-based features (Day of Week, Month, Lag features).
- **Forecasting Model**: Using Random Forest Regressor to predict demand.
- **Evaluation**: Measuring accuracy with MAE and RMSE.

## How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Open the notebook:
   ```bash
   jupyter notebook Forecasting_Analysis.ipynb
   ```
3. Run all cells to see the analysis and forecasts.

## Dataset
The project uses a simulated retail dataset representing daily sales for 5 products across 3 stores over a 2-year period.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
Copyright (c) 2026 Yogesh Badigineni. All rights reserved.
