"""Scenario 5: Hyperparameter Tuning
Task: Use GridSearchCV to find the best max_depth (values: [3, 5, 7]) and n_estimators 
(values: [50, 100]) for a Random Forest classifier."""
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

# Load sample data
iris = load_iris()
X = iris.data
y = iris.target

# Create the model
model = RandomForestClassifier()

# Define parameters to try
params = {
    'max_depth': [3, 5, 7],
    'n_estimators': [50, 100]
}

# Grid search
grid = GridSearchCV(model, params)
grid.fit(X, y)

# Print best results
print("Best Parameters:", grid.best_params_)
print("Best Score:", grid.best_score_)
