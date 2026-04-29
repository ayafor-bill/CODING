import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Example data: [goals_scored, goals_conceded, home_advantage (1 or 0)]
X = np.array([
    [2, 1, 1],  # Team A
    [1, 2, 0],  # Team B
    [3, 1, 1],
    [0, 2, 0],
    [1, 1, 1],
    [2, 3, 0],
])

# Labels: 1 = Win, 0 = Lose/Draw
y = np.array([1, 0, 1, 0, 1, 0])

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict on new match
# Example: team with 2 goals scored, 1 goal conceded, and home advantage
new_match = np.array([[2, 1, 1]])
prediction = model.predict(new_match)

# Output result
result = "Win" if prediction[0] == 1 else "Lose or Draw"
print("Prediction for the new match:", result)