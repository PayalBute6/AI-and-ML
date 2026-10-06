"""
Question: Write a program to implement a Voting Classifier by combining multiple machine learning models such as Logistic Regression and Decision Tree.
"""

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = load_iris()

X = data.data
Y = data.target

# Split data
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

# Create models
model1 = LogisticRegression(max_iter=200)
model2 = DecisionTreeClassifier(random_state=42)

# Combine models
voting_model = VotingClassifier(
    estimators=[
        ('lr', model1),
        ('dt', model2)
    ],
    voting='hard'
)

# Train Voting Classifier
voting_model.fit(X_train, Y_train)

# Predict
prediction = voting_model.predict(X_test)

# Accuracy
accuracy = accuracy_score(Y_test, prediction)

print("Predicted Values:", prediction)
print("Actual Values:", Y_test)
print("Voting Classifier Accuracy:", accuracy)
