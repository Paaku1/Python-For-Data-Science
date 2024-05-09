import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error, r2_score

# Load data
data = pd.read_csv('D:\Karthikyan\SECRET\Python\lab 9\petrol_consumption - petrol_consumption.csv')  # Adjust the path to your dataset

# Define features and target variable
X = data.drop('Petrol_Consumption', axis=1)
y = data['Petrol_Consumption']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Initialize and train models
models = {
    "Linear Regression": LinearRegression(),
    "Random Forest Regression": RandomForestRegressor(n_estimators=100, random_state=0),
    "Support Vector Regression": SVR()
}

# Dictionary to store results
results = {}

# Train and evaluate each model
for name, model in models.items():
    model.fit(X_train, y_train)  # Train model
    y_pred = model.predict(X_test)  # Make predictions
    mse = mean_squared_error(y_test, y_pred)  # Calculate mean squared error
    r2 = r2_score(y_test, y_pred)  # Calculate R-squared value
    results[name] = (mse, r2)

# Output results
for model_name, metrics in results.items():
    print(f"{model_name} - MSE: {metrics[0]:.2f}, R2: {metrics[1]:.2f}")
