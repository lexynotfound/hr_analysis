import joblib
import pandas as pd
import numpy as np

# 1. Load the model
model = joblib.load('model/attrition_model.pkl')

# Display header
print("\n" + "="*50)
print("EMPLOYEE ATTRITION PREDICTION SYSTEM")
print("="*50)

# 2. Your full sample data (for display purposes)
full_data = {
    "Age": [35],
    "BusinessTravel": [2],
    "DailyRate": [800],
    "Department": [1],
    "DistanceFromHome": [5],
    "Education": [3],
    "EducationField": [2],
    "EnvironmentSatisfaction": [3],
    "Gender": [1],
    "HourlyRate": [60],
    "JobInvolvement": [3],
    "JobLevel": [2],
    "JobRole": [4],
    "JobSatisfaction": [4],
    "MaritalStatus": [1],
    "MonthlyIncome": [7000],
    "MonthlyRate": [14000],
    "NumCompaniesWorked": [2],
    "OverTime": [1],
    "PercentSalaryHike": [14],
    "PerformanceRating": [3],
    "RelationshipSatisfaction": [3],
    "StockOptionLevel": [1],
    "TotalWorkingYears": [10],
    "TrainingTimesLastYear": [3],
    "WorkLifeBalance": [3],
    "YearsAtCompany": [5],
    "YearsInCurrentRole": [3],
    "YearsSinceLastPromotion": [2],
    "YearsWithCurrManager": [3]
}

# Display complete employee profile
df_full = pd.DataFrame(full_data)
print("\nCOMPLETE EMPLOYEE PROFILE:")
print("-"*50)
for col in df_full.columns:
    print(f"{col:<25} : {df_full[col].values[0]}")

# 3. Create a new DataFrame with ONLY the 8 features the model expects
model_features = [
    "Age",
    "DistanceFromHome",
    "JobSatisfaction",
    "WorkLifeBalance",
    "MonthlyIncome",
    "TotalWorkingYears",
    "YearsAtCompany",
    "YearsWithCurrManager"
]

# Extract only the features the model needs
prediction_data = {}
for feature in model_features:
    prediction_data[feature] = full_data[feature]

# Create the prediction DataFrame
df_prediction = pd.DataFrame(prediction_data)

# Display features used for prediction
print("\nFEATURES USED FOR PREDICTION:")
print("-"*50)
for col in df_prediction.columns:
    print(f"{col:<25} : {df_prediction[col].values[0]}")

# 4. Make prediction
prediction = model.predict(df_prediction)
probability = model.predict_proba(df_prediction)

# 5. Determine result and probability
is_leaving = prediction[0] == 1
stay_probability = probability[0][0] * 100  # Probability of staying
leave_probability = probability[0][1] * 100 if len(probability[0]) > 1 else 0  # Probability of leaving

# 6. Display results
print("\nPREDICTION RESULTS:")
print("-"*50)
if is_leaving:
    result = "AKAN KELUAR dari perusahaan"
    risk_level = "TINGGI"
else:
    result = "TIDAK AKAN keluar dari perusahaan"
    risk_level = "RENDAH"

print(f"Status Prediksi      : Karyawan {result}")
print(f"Tingkat Risiko       : {risk_level}")
print(f"Probabilitas Bertahan: {stay_probability:.2f}%")
print(f"Probabilitas Keluar  : {leave_probability:.2f}%")
print("\n" + "="*50 + "\n")