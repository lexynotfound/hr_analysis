import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
file_path = "employee_data.csv"
df = pd.read_csv(file_path)

# Data Cleaning
df_cleaned = df.dropna(subset=['Attrition']).copy()
df_cleaned.loc[:, 'Attrition'] = df_cleaned['Attrition'].astype(int)

# Feature Selection
features = ['Age', 'DistanceFromHome', 'JobSatisfaction', 'WorkLifeBalance', 'MonthlyIncome',
            'TotalWorkingYears', 'YearsAtCompany', 'YearsWithCurrManager']
X = df_cleaned[features]
y = df_cleaned['Attrition']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Feature Importance
feature_importances = model.feature_importances_
importances_df = pd.DataFrame({'features': features, 'importances': feature_importances})
importances_df = importances_df.sort_values(by='importances', ascending=False)


# Visualizations
# Visualizations
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

sns.boxplot(x='Attrition', y='MonthlyIncome', data=df_cleaned, ax=axes[0, 0])
axes[0, 0].set_title("Monthly Income vs Attrition")

sns.boxplot(x='Attrition', y='DistanceFromHome', data=df_cleaned, ax=axes[0, 1])
axes[0, 1].set_title("Distance From Home vs Attrition")

sns.boxplot(x='Attrition', y='YearsAtCompany', data=df_cleaned, ax=axes[1, 0])
axes[1, 0].set_title("Years at Company vs Attrition")

sns.histplot(data=df_cleaned, x='JobSatisfaction', hue='Attrition', multiple="dodge", bins=4, ax=axes[1, 1])
axes[1, 1].set_title("Job Satisfaction vs Attrition")

plt.tight_layout()
plt.show()

# Save model for prediction

# Buat folder 'model' jika belum ada
model_folder = "model"
if not os.path.exists(model_folder):
    os.makedirs(model_folder)

# Simpan model kedalam folder 'model'
model_path = os.path.join(model_folder, "attration_model.pkl")
joblib.dump(model, model_path)

