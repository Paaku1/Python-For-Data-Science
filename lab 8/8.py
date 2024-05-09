import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("D:\Karthikyan\SECRET\Python\lab 8\diabetes - diabetes.csv")  # Adjust path accordingly

# Split dataset into features and target variable
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize classifiers
models = {
    "Decision Tree": DecisionTreeClassifier(),
    "Random Forest": RandomForestClassifier(n_estimators=100),
    "Naive Bayes": GaussianNB()
}

# Train and evaluate models
results = {}
for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    cm = confusion_matrix(y_test, predictions)
    results[name] = (accuracy, cm)

# Plotting function for confusion matrices
def plot_confusion_matrix(cm, model_name, accuracy):
    plt.figure(figsize=(5, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap='Blues')
    plt.title(f'{model_name} - Accuracy: {accuracy:.2f}')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()

# Display results
for name, (accuracy, cm) in results.items():
    print(f"{name} Model Accuracy: {accuracy:.4f}")
    plot_confusion_matrix(cm, name, accuracy)

# Determine the best model
best_model = max(results, key=lambda x: results[x][0])
best_accuracy = results[best_model][0]
print(f"The best model is: {best_model} with an accuracy of {best_accuracy:.4f}")
