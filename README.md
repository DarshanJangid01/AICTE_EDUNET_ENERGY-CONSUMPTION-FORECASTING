# Household Energy Consumption Forecasting

## Project Overview
This project aims to forecast household electricity consumption using machine learning models.  
The forecasting task is framed as a regression problem, where past energy usage and calendar-based features are used to predict future consumption.  

---

## Workflow
1. Data Preprocessing  
   - Combined Date and Time into a single datetime index.  
   - Converted energy consumption values to numeric format.  
   - Resampled the dataset into hourly averages.  

2. Feature Engineering  
   - Created lag features (t-1, t-2, …) to incorporate historical consumption.  
   - Added calendar features such as hour of day, day of week, and month to capture temporal patterns.  

3. Model Selection  
   - Selected Random Forest Regressor for Week 2 submission.  
   - Reasons for selection:  
     - Handles non-linear relationships effectively.  
     - Incorporates both lagged and calendar features.  
     - Provides feature importance insights for interpretability.  

4. Model Training and Evaluation  
   - Split dataset into training and testing sets.  
   - Trained Random Forest on engineered features.  
   - Evaluated with Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).  

---

## Results
- Evaluation Metrics:  
  - MAE: ~0.40
  - RMSE: ~0.55  

- Insights:  
  - Model captures short-term consumption patterns well.  
  - Lag features (especially previous hour) are the most influential predictors.  
  - Calendar features (hour, weekday, month) improve accuracy.  

- Feature Importance Visualization:  
  The Random Forest highlights which features contribute most to energy consumption forecasts, providing valuable interpretability.  

---

## Next Steps
- Deploy the trained model as a web app or API for real-time energy consumption forecasting.  
- Explore additional models such as XGBoost and Linear Regression for benchmarking.  

---
