# Soccer Match Prediction Model

**Created:** May 9, 2026

## Overview

This project implements a machine learning-based soccer match prediction system using Logistic Regression. It demonstrates a complete workflow for building a binary classification model that predicts whether a soccer team will win or lose/draw based on match statistics and contextual factors.

## What It Does

The script trains a Logistic Regression classifier to predict match outcomes (Win vs. Lose/Draw) using three key features:

- **Goals Scored**: The number of goals the team has scored in the match
- **Goals Conceded**: The number of goals the opposing team has scored
- **Home Advantage**: A binary indicator (1 for home games, 0 for away games)

The model learns patterns from historical match data and can make predictions on new matches based on these features.

## Requirements

This project requires Python 3.x and the following packages:

- **NumPy**: For numerical computations and array handling
- **scikit-learn**: For machine learning algorithms and model evaluation tools

### Installation

Install the required packages using pip:

```bash
python -m pip install numpy scikit-learn
```

## How to Use

### Running the Script

Execute the script from the command line:

```bash
python predict_soccer.py
```

### Expected Output

```Prediction for the new match: Win
```

The output will display either "Win" or "Lose or Draw" based on the model's prediction for the example match.

## Code Walkthrough

### 1. Data Preparation

The script starts with a small dataset containing six match records. Each record has three features:

```python
X = np.array([
    [2, 1, 1],  # Team A: scored 2, conceded 1, home game
    [1, 2, 0],  # Team B: scored 1, conceded 2, away game
    [3, 1, 1],  # scored 3, conceded 1, home game
    [0, 2, 0],  # scored 0, conceded 2, away game
    [1, 1, 1],  # scored 1, conceded 1, home game
    [2, 3, 0],  # scored 2, conceded 3, away game
])

y = np.array([1, 0, 1, 0, 1, 0])  # Outcomes: 1=Win, 0=Lose/Draw
```

### 2. Train-Test Split

The data is divided into training and test sets with an 80/20 split:

```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```

This ensures the model is evaluated on unseen data, helping assess generalization performance.

### 3. Model Training

A Logistic Regression model is instantiated and trained:

```python
model = LogisticRegression()
model.fit(X_train, y_train)
```

Logistic Regression is chosen for its simplicity, interpretability, and effectiveness for binary classification tasks.

### 4. Making Predictions

The trained model predicts outcomes for new matches:

```python
new_match = np.array([[2, 1, 1]])  # Example: team scores 2, concedes 1, home game
prediction = model.predict(new_match)
```

### 5. Result Interpretation

The prediction (0 or 1) is converted to human-readable output:

```python
result = "Win" if prediction[0] == 1 else "Lose or Draw"
print("Prediction for the new match:", result)
```

## Example Scenarios

### Scenario 1: Strong Home Team

- **Input:** [3, 1, 1] (scores 3, concedes 1, home advantage)
- **Likely Prediction:** Win
- **Reasoning:** Good offense, strong defense, home advantage

### Scenario 2: Struggling Away Team

- **Input:** [1, 3, 0] (scores 1, concedes 3, away game)
- **Likely Prediction:** Lose or Draw
- **Reasoning:** Weak offense, poor defense, no home advantage

### Scenario 3: Balanced Away Match

- **Input:** [2, 2, 0] (scores 2, concedes 2, away game)
- **Likely Prediction:** Uncertain (depends on model weights)
- **Reasoning:** Balanced stats but no home advantage

## Limitations and Considerations

### 1. Minimal Training Data

With only six match records, the model has extremely limited data for learning. This will likely result in overfitting—the model may memorize the training data rather than learning generalizable patterns.

### 2. Oversimplified Feature Set

Real soccer outcomes depend on many factors not captured here:

- Team strength ratings
- Player injuries or absences
- Recent form and momentum
- Head-to-head history
- Weather conditions
- Referee bias
- Tactical formations
- Player fatigue from previous matches

### 3. No Model Validation

The script doesn't evaluate model performance on test data or calculate metrics like accuracy, precision, recall, or F1-score.

### 4. Binary Classification Only

The model only predicts Win vs. Lose/Draw. A three-class model (Win/Draw/Loss) would provide more nuanced predictions.

## Future Improvements

To make this model more practical and reliable, consider:

1. **Expand Dataset**: Collect hundreds or thousands of historical match records
2. **Feature Engineering**: Add features like team ratings, player statistics, and recent performance
3. **Model Evaluation**: Calculate accuracy, precision, recall, and F1-score on test data
4. **Hyperparameter Tuning**: Optimize model parameters for better performance
5. **Cross-Validation**: Use k-fold cross-validation to ensure robust evaluation
6. **Advanced Models**: Experiment with Random Forest, Gradient Boosting, or Neural Networks
7. **Probability Scores**: Use `predict_proba()` to get confidence scores instead of binary predictions
8. **Class Balance**: Handle potential class imbalance in win vs. lose/draw outcomes

## Educational Value

This script serves as an excellent introduction to machine learning workflows, demonstrating:

- Data preparation and feature representation
- Train-test splitting methodology
- Model training and fitting
- Making predictions on new data
- Binary classification fundamentals

## Notes

- The model requires scikit-learn 0.24+ for compatibility
- NumPy arrays are used for efficient numerical operations
- Logistic Regression is a linear classifier—for complex patterns, nonlinear models may perform better
- This is a proof-of-concept implementation and not suitable for actual betting or serious sports analysis

## Author

Created: May 9, 2026

---

For questions or improvements, feel free to modify the dataset, features, or model architecture to suit your needs!
